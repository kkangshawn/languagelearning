from flask import Blueprint, request, flash, redirect, url_for, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from bson.objectid import ObjectId
import functools

from .languageDB import get_collection, Collections

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    action = request.form['action']
    collection = get_collection(Collections.USERS)
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    else:
        if action == "Login":
            user = collection.find_one({"username" : username})
            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user['password'], password):
                error = 'Incorrect password.'
            else:
                session.clear()
                session['username'] = user['username']
        else:
            user = collection.find_one({"username" : username})
            if user is not None:
                error = f"User {username} is already registered."
            else:
                collection.insert_one({
                    "username" : username,
                    "password" : generate_password_hash(password)
                })
                session.clear()
                session['username'] = username
    if error is not None:
        flash(error)

    return redirect(request.referrer)

@bp.before_app_request
def load_logged_in_user():
    username = session.get('username')

    if username is None:
        g.user = None
    else:
        g.user = get_collection(Collections.USERS).find_one({"username" : username})

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(request.referrer)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(request.referrer)
        return view(**kwargs)
    return wrapped_view