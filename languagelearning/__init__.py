from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "dev"

    app.config.from_prefixed_env()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import posts
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint='index_posts')

    from . import wordbook
    app.register_blueprint(wordbook.bp)

    return app
