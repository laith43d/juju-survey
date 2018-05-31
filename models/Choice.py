import datetime

from sqlalchemy import Column, ForeignKey, Integer, String

from config.settings import Model
from facilities.databases.DBMixins import IDMixin


class Choice(Model, IDMixin):
    __tablename__ = 'choices'

    text = Column(String(100), nullable = False)
    selected = Column(Integer, default = 0)
    question_id = Column(Integer, ForeignKey('questions.id'))

    def to_dict(self):
        return dict(id = self.id,
                    text = self.text,
                    created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    question_id = self.question_id)
