from flask import request
from flask_classful import FlaskView as Resource, route
from flask_orator import jsonify

from models import Choice, Survey, Question


class SurveyView(Resource):

    @route('', methods = ['GET', 'POST'])
    def all(self):
        if request.method == 'GET':
            surveys = Survey.all()
            return jsonify([s.to_dict() for s in surveys])
        elif request.method == 'POST':
            data = request.get_json()
            survey = Survey(name = data['name'])
            questions = []
            for q in data['questions']:
                question = Question(text = q['text'])
                question.choices = [Choice(text = c) for c in q['choices']]
                questions.append(question)
            survey.questions = questions
            survey.save()
            return jsonify(survey.to_dict()), 201


    @route('/<int:id_>', methods = ('GET', 'PUT'))
    def one(self, id_):
        if request.method == 'GET':
            survey = Survey.query.get(id_)
            return jsonify(survey.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            for q in data['questions']:
                choice = Choice.query.get(q['choice'])
                choice.selected = choice.selected + 1
                choice.save()
            survey = Survey.find(data['id'])
            return jsonify(survey.to_dict()), 201
