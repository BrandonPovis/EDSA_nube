from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

# Leer la URL desde las variables de entorno
MONGO_URL = os.getenv("MONGO_URL")

# Conectar con MongoDB
client = MongoClient(MONGO_URL)

# Usar la base de datos y colección
db = client.edsa_db
collection_name = db["edsa_collection"]


