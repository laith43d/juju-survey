from orator.orm import has_many

from config.settings import Model
from .questions import Question


class Survey(Model):
    __table__ = 'surveys'
    __fillable__ = [
        'name'
    ]

    @has_many
    def questions(self):
        return Question
