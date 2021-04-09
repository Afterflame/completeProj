import axios from 'axios'

export const AUTH = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
})
