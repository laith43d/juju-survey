from orator.orm import has_many

from config.settings import Model
from models import Question


class Survey(Model):
    @has_many
    def questions(self):
        return Question
