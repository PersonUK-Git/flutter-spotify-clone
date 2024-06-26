from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = 'postgresql://postgres:Prateek006@localhost:5432/musicapp'
DATABASE_URL = "postgresql://musicapp_gy3r_user:KFugeM6IFckXYzcNGDlPfCsvXwSjwijX@dpg-cptr5308fa8c738p38o0-a/musicapp_gy3r"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
