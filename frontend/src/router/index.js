import Router from 'vue-router'
import Vue from 'vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'MainPageRout',
      component: () =>
                import ('../../views/MainPage')
    },
    {
      path: '/login',
      name: 'AuthorizationPageRout',
      component: () =>
                import ('../../views/AuthorizationPage')
    },
    {
      path: '/registration',
      name: 'RegistrationPageRout',
      component: () =>
                import ('../../views/RegistrationPage')
    },
    {
      path: '/profile',
      name: 'ProfilePageRout',
      component: () =>
                import ('../../views/ProfilePage')
    },
  ]
})
