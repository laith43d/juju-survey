import Vue from 'vue'
import vuex from 'vuex'

import { fetchSurveys, fetchSurvey, saveSurveyResponse } from '../api'

Vue.use(vuex)

const state = {

  surveys: [],
  currentSurvey: []
}

const actions = {

  loadSurveys(context) {
    return fetchSurveys()
      .then((response) => context.commit('setSurveys', {surveys: response}))
  },

  loadSurvey (context, {id}) {
    return fetchSurvey(id)
      .then((response) => context.commit('setSurvey', {survey: response}))
  },

  addSurveyResponse(context) {
    return saveSurveyResponse(context.state.currentSurvey)
  }


}

const mutations = {

  setSurveys(state, payload) {
    state.surveys = payload.surveys
  },

  setSurvey(state, payload) {
    const nQuestions = payload.survey.questions.length
    for(let i=0; i<nQuestions; i++) {
      payload.survey.questions[i].choice = null
    }
    state.currentSurvey = payload.survey
  },

  setChoice(state, payload) {
    const {questionId, choice} = payload
    const nQuestions = state.currentSurvey.questions.length
    for (let i = 0; i<nQuestions; i++) {
      if (state.currentSurvey.questions[i].id === questionId) {
        state.currentSurvey.question[i].choice = choice
        break
      }
    }
  }

}

const getters = {

}

const store = new vuex.Store({
  state, actions, mutations, getters
})

export default store
