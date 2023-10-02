from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from bson.objectid import ObjectId

from .languageDB import get_collection, Collections
from .auth import login_required

bp = Blueprint('posts', __name__)

@bp.route('/')
def index():
    g.posts = "active"
    g.wordbook = ""
    phrases = get_collection(Collections.GERMAN_PHRASES).find().sort("_id", -1)
    return render_template("deutschsatz.html", phrases=phrases)

@bp.route('/insert', methods=['POST'])
@login_required
def insert():
    phrase = request.form['phrase']
    meaning = request.form['meaning']
    error = None
        
    if not phrase:
        error = 'Phrase is missing.'
        flash(error)
    else:
        collection = get_collection(Collections.GERMAN_PHRASES)
        collection.insert_one({
            "phrase" : phrase,
            "meaning" : meaning,
            "author" : g.user['username']
            })
        print("added by " + g.user['username'])
    return redirect(url_for('posts.index'))

@bp.route('/<id>/delete', methods=['POST'])
@login_required
def delete(id):
    collection = get_collection(Collections.GERMAN_PHRASES)
    collection.delete_one({
        "_id" : ObjectId(id)
        })
    return redirect(url_for('posts.index'))

@bp.route('/<id>/modify', methods=['POST'])
@login_required
def modify(id):
    phrase = request.form['phrase']
    meaning = request.form['meaning']
    error = None
    
    if not phrase:
        error = 'Phrase is missing.'
        flash(error)
    else:
        collection = get_collection(Collections.GERMAN_PHRASES)
        collection.update_one({
            "_id" : ObjectId(id)
        }, {
            "$set" : {
                "phrase" : phrase,
                "meaning" : meaning
            }
        })
    return redirect(url_for('posts.index'))