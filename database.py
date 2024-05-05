from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://tcc-puc_owner:0OwWilKFq1Mk@ep-wispy-mouse-a635vsp4.us-west-2.aws.neon.tech/tcc-puc?sslmode=require"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def test():
    return ""