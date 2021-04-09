import { AUTH } from './common'

export const Auth = {
  register (config) {
    return AUTH.post('register/', config).then(response => {
      return response.data
    })
  },
  login (config) {
    return AUTH.post('api-token-auth/', config).then(response => {
      return response.data
    })
  },
  getUserByToken(config) {
    return AUTH.post('whoami/', config).then(response => {
      return response.data
    })
  },

}
