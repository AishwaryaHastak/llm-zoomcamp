# constants.py

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
# load_dotenv() 
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

# Index Constants
text_fields=["question", "answer"]
keyword_fields=["topic","id"]
index_name = "python-qa-index"

# Model Constants 
model_name = 'google/flan-t5-small' 
embedding_model = 'multi-qa-MiniLM-L6-cos-v1'
embedding_size = 128

# Path to the SQLite database file
# DATABASE_PATH = 'database.db'


# Get database credentials from environment variables
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST', 'localhost')  # Default to localhost if not set
DB_PORT = os.getenv('DB_PORT', '5432')  # Default to 5432 if not set

# Construct the database URI
DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'