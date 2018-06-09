from flask import request
from flask_classful import FlaskView as Resource, route
from flask_orator import jsonify

from models import Survey, Question, Choice


class SurveyView(Resource):

    @route('', methods = ['GET', 'POST'])
    def all(self):
        if request.method == 'GET':
            surveys = Survey.all()
            questions = Question.all()
            choices = Choice.all()
            return jsonify({'surveys': [s.to_dict() for s in surveys],
                           'questions': [q.to_dict() for q in questions],
                           'choices': [c.to_dict() for c in choices]})
        elif request.method == 'POST':
            data = request.get_json()
            survey = Survey(name = data['name'])
            survey.save()
            for q in data['questions']:
                question = Question(text = q['text'])
                survey.questions().save(question)
                question.save()
                [question.choices().save(Choice(text = c['text'])) for c in q['choices']]
            return jsonify(survey.to_dict()), 201


    @route('/<int:id_>', methods = ('GET', 'PUT'))
    def one(self, id_):
        if request.method == 'GET':
            survey = Survey.find(id_)
            return jsonify(survey.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            for q in data['questions']:
                choice_selected = Choice.where('id', q['choice']).first()
                choice_selected.selected += 1
                choice_selected.save()
            survey = Survey.find(data['survey_id'])
            return jsonify(survey.to_dict()), 201
