from base import Base, db
from sqlalchemy import Column, Integer, Text, Boolean, text
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

    def __init__(self, organization_id=None, timestamp=None, limit_name=None, limit_capacity=None, limit_duration_s=None, percentage_used=None,
                 is_reported=None):
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

    def get_event_count_since(self, minutes, organization_id, limit_name):
        return (
            self.db.query(ThrottlingEvent.organization_id)
                .filter(ThrottlingEvent.organization_id == organization_id)
                .filter(ThrottlingEvent.limit_name == limit_name)
                .filter(ThrottlingEvent.timestamp >= text("strftime('%s', 'now') - 60*{}".format(minutes)))
        ).count()
