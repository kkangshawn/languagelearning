from languagelearning import create_app
import traceback
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LanguageLearningApp")

logger.info("--- Starting application... ---")
try:
    application = create_app()
    logger.info("--- Application created successfully. ---")
    app = application
except Exception as e:
    print(f"Error running application: {e}")
    traceback.print_exc()
    logger.error(f"--- Error running application: {e} ---")
    raise e

if __name__ == "__main__":
    application.run()