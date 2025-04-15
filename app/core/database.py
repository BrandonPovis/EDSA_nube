from sqlmodel import SQLModel,Field, Session, create_engine, select
from sqlalchemy.orm import sessionmaker


# Create the PostgreSQL databse and engine
rds_postgresql_url = "postgresql://rootuser:edsa123456@edsa.cr82ieywavu2.sa-east-1.rds.amazonaws.com:5432/postgres"

engine=create_engine(rds_postgresql_url,echo=True)
SessionLocal = sessionmaker(bind=engine)

# Initialize the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()