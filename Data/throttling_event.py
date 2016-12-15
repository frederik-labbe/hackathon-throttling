from base import Base, db
from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.sql import not_


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

    def __init__(self):
        self.db = db()

    def update(self, throttling_event):
        self.db.merge(throttling_event)
        self.db.commit()

    def get_all_unreported(self):
        return (
            self.db.filter(not_(ThrottlingEvent.is_reported))
        ).all()
