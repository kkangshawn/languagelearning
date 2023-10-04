from flask import Blueprint, render_template, g, request, flash, url_for, redirect, jsonify
from bson.objectid import ObjectId
from bson.json_util import dumps
from json import loads

from .languageDB import get_collection, Collections
from .auth import login_required

bp = Blueprint('wordbook', __name__, url_prefix='/wordbook')
collection = None

@bp.route('/')
def index():
    g.posts = ""
    g.wordbook = "active"
    words = None
    cardsets = ([], [], [], [], [], [])
    cardqty = []
    global collection
    collection = get_collection(Collections.GERMAN_WORDS)
    if g.user:
        words = list(collection.find({"author" : g.user['username']}))
        for item in words:
            item['_id'] = str(item['_id'])
            cardsets[item['level']].append(item)
        for cardset in cardsets:
            cardqty.append(len(cardset))
        cardsets = dumps(cardsets)
        cardsets = loads(cardsets)
    return render_template('wordbook.html', words=words, cardsets=cardsets, cardqty=cardqty)

@bp.route('/insert', methods=['POST'])
@login_required
def insert():
    word = request.form['word']
    meaning = request.form['meaning']
    error = None
        
    if not word:
        error = 'Word is missing.'
        flash(error)
    else:
        global collection
        if collection is None:
            collection = get_collection(Collections.GERMAN_WORDS)
        collection.insert_one({
            "word" : word,
            "meaning" : meaning,
            "level" : 1,
            "author" : g.user['username']
            })
    return redirect(url_for('wordbook.index'))

@bp.route('/<id>/delete', methods=['POST'])
@login_required
def delete(id):
    global collection
    if collection is None:
        collection = get_collection(Collections.GERMAN_WORDS)
    collection.delete_one({
        "_id" : ObjectId(id)
        })
    return redirect(url_for('wordbook.index'))

@bp.route('/<id>/modify', methods=['POST'])
@login_required
def modify(id):
    word = request.form['word']
    meaning = request.form['meaning']
    level = int(request.form['level'])
    error = None
    
    if not word:
        error = 'Word is missing.'
        flash(error)
    else:
        global collection
        if collection is None:
            collection = get_collection(Collections.GERMAN_WORDS)
        collection.update_one({
            "_id" : ObjectId(id)
        }, {
            "$set" : {
                "word" : word,
                "meaning" : meaning,
                "level" : level
            }
        })
    return redirect(url_for('wordbook.index'))

@bp.route('/levelChange', methods=['POST'])
@login_required
def levelChange():
    id = request.form['id']
    level = int(request.form['level']) + int(request.form['updown'])
    
    if 0 < level < 6:
        global collection
        if collection is None:
            collection = get_collection(Collections.GERMAN_WORDS)
        item = collection.find_one_and_delete({
        "_id" : ObjectId(id)
        })
        item['level'] = level
        collection.insert_one(item)

    return jsonify({'status': 'OK'})
