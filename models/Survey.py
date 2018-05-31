from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship

from config.settings import Model
from facilities.databases.DBMixins import IDMixin


class Survey(Model, IDMixin):
    __tablename__ = 'surveys'

    name = Column(Text)
    questions = relationship('Question', backref = "survey", lazy = False)

    def to_dict(self):
        return dict(id = self.id,
                    name = self.name,
                    created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    questions = [question.to_dict() for question in self.questions])
