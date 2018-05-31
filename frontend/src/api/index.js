import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export function fetchSurveys () {
  return axios.get(`${API_URL}/survey/`)
}

export function fetchSurvey (surveyId) {
  return axios.get(`${API_URL}/survey/${surveyId}/`)
}

export function saveSurveyResponse (surveyResponse) {
  return axios.put(`${API_URL}/survey/${surveyResponse.id}/`, surveyResponse)
}

export function postNewSurvey (survey) {
  return axios.post(`${API_URL}/survey/`, survey)
}
