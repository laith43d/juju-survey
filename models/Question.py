from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.settings import Model
from facilities.databases.DBMixins import IDMixin


class Question(Model, IDMixin):
    __tablename__ = 'questions'

    text = Column(String(500), nullable = False)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    choices = relationship('Choice', backref = 'question', lazy = False)

    def to_dict(self):
        return dict(id = self.id,
                    text = self.text,
                    created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    survey_id = self.survey_id,
                    choices = [choice.to_dict() for choice in self.choices])
