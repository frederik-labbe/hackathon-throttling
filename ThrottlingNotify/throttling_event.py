class ThrottlingEvent:
    def __init__(self, organization_id, timestamp, limit_name, limit_capacity, limit_duration, percentage_used, reported):
        self.organizationId = organization_id;
        self.timestamp = timestamp;
        self.limit_name = limit_name;
        self.limit_capacity = limit_capacity;
        self.limit_duration = limit_duration;
        self.percentage_used = percentage_used;
        self.reported = reported;