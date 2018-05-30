from orator.orm import belongs_to

from config.settings import Model
from models import Question


class Choice(Model):
    @belongs_to
    def question(self):
        return Question
