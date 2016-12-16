from base import Base, db
from sqlalchemy import Column, Integer, Text, Boolean, DateTime
from sqlalchemy.sql import not_, text


class ThrottlingAbuse(Base):
    __tablename__ = 'throttling_abuse'

    organization_id = Column(Text, primary_key=True, nullable=False)
    limit_name = Column(Text, primary_key=True, nullable=False)
    last_abuse_timestamp = Column(DateTime, nullable=False)

    def __init__(self):
        self.db = db()

    def update(self, throttling_abuse):
        self.db.merge(throttling_abuse)
        self.db.commit()

    def last_abuse_since(self, minutes, organization_id, limit_name):
        return (
            self.db.query(ThrottlingAbuse.organization_id)
                .filter(ThrottlingAbuse.organization_id == organization_id)
                .filter(ThrottlingAbuse.limit_name == limit_name)
                .filter(ThrottlingAbuse.last_abuse_timestamp >= text("strftime('%s', 'now') - 60*{}".format(minutes)))
        ).count() > 0
