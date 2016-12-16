from base import Base, db
from sqlalchemy import Column, Integer, Text, Boolean, DateTime
from sqlalchemy.sql import not_, text


class ThrottlingAbuse(Base):
    __tablename__ = 'throttling_abuse'

    organization_id = Column(Text, primary_key=True, nullable=False)
    limit_name = Column(Text, primary_key=True, nullable=False)
    last_abuse_timestamp = Column(Integer, nullable=False)

    def __init__(self, organization_id=None, limit_name=None, last_abuse_timestamp=None):
        self.db = db()
        self.organization_id = organization_id
        self.limit_name = limit_name
        self.last_abuse_timestamp = last_abuse_timestamp

    def update(self, last_abuse_timestamp):
        self.last_abuse_timestamp = last_abuse_timestamp
        self.db.merge(self)
        self.db.commit()

    def last_abuse_since(self, minutes, organization_id, limit_name):
        return (
            self.db.query(ThrottlingAbuse.organization_id)
                .filter(ThrottlingAbuse.organization_id == organization_id)
                .filter(ThrottlingAbuse.limit_name == limit_name)
                .filter(ThrottlingAbuse.last_abuse_timestamp >= text("strftime('%s', 'now') - 60*{}".format(minutes)))
        ).count() > 0
