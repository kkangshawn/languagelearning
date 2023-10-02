from flask import Blueprint, render_template, g, request, flash, url_for, redirect
from bson.objectid import ObjectId

from .languageDB import get_collection, Collections
from .auth import login_required

bp = Blueprint('wordbook', __name__, url_prefix='/wordbook')

@bp.route('/')
def index():
    g.posts = ""
    g.wordbook = "active"
    words = None
    if g.user:
        print(g.user['username'])
        words = get_collection(Collections.GERMAN_WORDS).find({"author" : g.user['username']})

    return render_template('wordbook.html', words=words)

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
        collection = get_collection(Collections.GERMAN_WORDS)
        collection.insert_one({
            "word" : word,
            "meaning" : meaning,
            "level" : 1,
            "author" : g.user['username']
            })
        print("added by " + g.user['username'])
    return redirect(url_for('wordbook.index'))

@bp.route('/<id>/delete', methods=['POST'])
@login_required
def delete(id):
    print("DELETE CALLED")
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
    level = request.form['level']
    error = None
    
    if not word:
        error = 'Word is missing.'
        flash(error)
    else:
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