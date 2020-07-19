from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

env_path = Path('.')
load_dotenv(dotenv_path=env_path)
