import glob
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
env_override_files = glob.glob('.env.dev*')

for env in env_override_files:
    if os.path.exists(env):
        load_dotenv(dotenv_path=env, override=True)

DB_NAME = os.getenv('DB_NAME')
