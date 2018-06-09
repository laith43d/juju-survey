from config.settings import Model


class Choice(Model):
    __table__ = 'choices'
    __fillable__ = [
        'text',
        'selected',
        'question_id'
    ]
