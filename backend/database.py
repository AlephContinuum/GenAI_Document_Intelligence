
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

engine=create_engine("sqlite:///docs.db")
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()

class Document(Base):
    __tablename__="documents"
    id=Column(Integer,primary_key=True)
    raw_text=Column(Text)
    summary=Column(Text)
    explanation=Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_document(raw, summary, explanation):
    init_db()
    doc=Document(raw_text=raw, summary=summary, explanation=explanation)
    session.add(doc)
    session.commit()
