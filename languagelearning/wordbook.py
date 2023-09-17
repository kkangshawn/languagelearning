from flask import Blueprint, render_template, g

bp = Blueprint('wordbook', __name__, url_prefix='/wordbook')

@bp.route('/')
def index_wordbook():
    g.posts = ""
    g.wordbook = "active"
    return render_template('wordbook.html')