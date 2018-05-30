from orator.orm import belongs_to, has_many

from config.settings import Model
from models import Choice, Survey


class Question(Model):
    @has_many
    def choices(self):
        return Choice

    @belongs_to
    def survey(self):
        return Survey
