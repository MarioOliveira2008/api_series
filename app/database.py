
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}"
SERVER_URL = "mysql+pymysql://root:admin@localhost"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()

# DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_db"
# DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"
DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"

# Criar um "motor" que fara o gerenciamento da conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Criando uma sessao para executar os comandos SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria um objeto da base de dados manipulavel pelo Python
Base = declarative_base()

# injeção de dependência: injeta a sessão do banco de dados em cada rota que for criada
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()