import os
import joblib
from dotenv import load_dotenv

# Load .env file
load_dotenv(override=True)

# Get variables
APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv('APP_VERSION')



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_FOLDER_PATH = os.path.join(BASE_DIR, "artifacts")

# Models
forest_model = joblib.load(os.path.join(ARTIFACTS_FOLDER_PATH, 'rfc_best_model.pkl'))
xgboost_model = joblib.load(os.path.join(ARTIFACTS_FOLDER_PATH, 'xgb_best_model.pkl'))

