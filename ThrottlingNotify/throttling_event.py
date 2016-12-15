from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean

Base = declarative_base()


class ThrottlingEvent(Base):
    __tablename__ = 'ThrottlingEvent'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    organization_id = Column(Text, nullable=False)
    timestamp = Column(Integer, nullable=False)
    limit_name = Column(Text, nullable=False)
    limit_capacity = Column(Integer, nullable=False)
    limit_duration_s = Column(Integer, nullable=False)
    percentage_used = Column(Integer, nullable=False)
    is_reported = Column(Boolean, nullable=False)
