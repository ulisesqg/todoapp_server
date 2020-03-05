import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.abspath(os.path.dirname(__name__)), ".env")
load_dotenv(dotenv_path=env_path)
print("Load configs with env file: {}".format(env_path))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
