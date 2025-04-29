from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Leer la URL de conexión desde el entorno
rds_postgresql_url = os.getenv("DATABASE_URL_RDS")

# Crear el engine
engine = create_engine(rds_postgresql_url, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Inicializar la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


 