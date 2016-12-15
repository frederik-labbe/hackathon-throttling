from base import Base, db
from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.sql import not_


class ThrottlingEvent(Base):
    __tablename__ = 'throttling_event'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    organization_id = Column(Text, nullable=False)
    timestamp = Column(Integer, nullable=False)
    limit_name = Column(Text, nullable=False)
    limit_capacity = Column(Integer, nullable=False)
    limit_duration_s = Column(Integer, nullable=False)
    percentage_used = Column(Integer, nullable=False)
    is_reported = Column(Boolean, nullable=False)

    def __init__(self, organization_id, timestamp, limit_name, limit_capacity, limit_duration_s, percentage_used, is_reported):
        self.db = db()
        self.organization_id = organization_id
        self.timestamp = timestamp
        self.limit_name = limit_name
        self.limit_capacity = limit_capacity
        self.limit_duration_s = limit_duration_s
        self.percentage_used = percentage_used
        self.is_reported = is_reported

    def update(self, throttling_event):
        self.db.merge(throttling_event)
        self.db.commit()

    def get_all_unreported(self):
        return (
            self.db.filter(not_(ThrottlingEvent.is_reported))
        ).all()
