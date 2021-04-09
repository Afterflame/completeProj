import {AUTH, NOTES} from './common'
import axios from "axios";
import router from "../router";

export const Note = {
  create (config, token) {
    return axios.create({
      baseURL: 'http://localhost:8000/api/v1/',
      headers: {
        Authorization: 'Token '+ token
      }
    })
      .post('/notes/', config).then(response => {
        console.log('Token '+ token);
      return response.data
    })
      .then()
      .catch(error => {
        console.log(error);
      })
  },
  delete (note, token) {
    return axios.create({
      baseURL: 'http://localhost:8000/api/v1/',
      headers: {
        Authorization: 'Token '+ token
      }
    })
      delete(`/notes/${note.id}/`)
  },
  changePassword(data, token) {
    return axios.create({
      baseURL: 'http://localhost:8000/api/v1/',
      headers: {
        Authorization: 'Token '+ token
      }
    })
  },
  list (token) {
    return axios.create({
      baseURL: 'http://localhost:8000/api/v1/',
      headers: {
        Authorization: 'Token '+ token
      }
    })
      .get('/notes/').then(response => {
      return response.data
    })
  }
}
