import os
from dotenv import load_dotenv

load_dotenv()

COINMARKET_API = os.getenv("COINMARKET_API")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DBNAME = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


#kokchun brukar skapa en sån här constants folder typ som filsökvägar. env 
#då kan andra filer importera från denna fil.