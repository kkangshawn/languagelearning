from flask import Flask
import traceback
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LanguageLearningApp")

logger.info("--- Starting application... ---")
try:
    app = Flask(__name__)
    app.secret_key = "dev"

    app.config.from_prefixed_env()

    from languagelearning import auth
    app.register_blueprint(auth.bp)

    from languagelearning import posts
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint='index_posts')

    from languagelearning import wordbook
    app.register_blueprint(wordbook.bp)

    logger.info("--- Application created successfully. ---")
except Exception as e:
    print(f"Error running application: {e}")
    traceback.print_exc()
    logger.error(f"--- Error running application: {e} ---")
    raise e

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)