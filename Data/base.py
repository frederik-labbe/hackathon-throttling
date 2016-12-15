from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(r'sqlite:///throttling-event.db')
Base.metadata.create_all(engine, checkfirst=True)
db = sessionmaker(bind=engine)
