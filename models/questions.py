from orator.orm import has_many

from config.settings import Model
from .choices import Choice


class Question(Model):
    __table__ = 'questions'
    __fillable__ = [
        'text',
        'survey_id'
    ]

    @has_many
    def choices(self):
        return Choice
