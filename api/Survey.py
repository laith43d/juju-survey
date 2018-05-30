from flask_classful import FlaskView as Resource, route
from flask_orator import jsonify

from models import Survey, Question


class SurveyView(Resource):

    @route('', methods = ['GET'])
    def all(self):
        survey = Survey.find(1)
        print(survey.questions.choices)
        return jsonify({'1': '1'})