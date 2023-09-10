from sqlalchemy import Column, String, Integer, Float

from app.database.database import base, session


class ActivityModel(base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    activity = Column(String(120), nullable=False)
    type = Column(String(120), nullable=False)
    participants = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    link = Column(String(120), nullable=True)
    key = Column(Integer, nullable=False)
    accessibility = Column(Float, nullable=False)

    @classmethod
    def return_latest_activities(cls):
        """
        Return all activities
        :return: list of dict representations of activities
        """
        activities = session.query(cls).order_by(cls.id.desc()).limit(5)

        return [cls.to_dict(activity) for activity in activities]

    def save_to_db(self):
        """
        Save model instance to database
        :return: None
        """
        session.add(self)
        session.commit()

    @staticmethod
    def to_dict(activity):
        """
        Represent model instance (activity) information
        :param activity: model instance
        :return: dict representation of activity info
        """
        return {
            "id": activity.id,
            "activity": activity.activity,
            "type": activity.type,
            "participants": activity.participants,
            "price": activity.price,
            "link": activity.link,
            "key": activity.key,
            "accessibility": activity.accessibility,
        }
