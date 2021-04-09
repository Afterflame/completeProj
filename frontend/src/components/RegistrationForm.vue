<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-2
        label.form-label Login
      .col-9
        input.form-input(type="text" v-model="username" placeholder="Login")
    .form-group
      .col-2
        label.form-label Password
      .col-9
        input.form-input(type="email" v-model="email" placeholder="E-mail")
    .form-group
      .col-2
        label.form-label Password
      .col-9
        input.form-input(type="password" v-model="password" placeholder="Password")
    .form-group
      .col-2
        label.form-label ..And Again
      .col-9
        input.form-input(type="password" v-model="repeat" placeholder="Repeat Password")
    .form-group
      .col-2
      .col-9
        button.btn.btn-primary(type="submit") Go!
    hr
    .form-group
      .col-2
      .col-9
        router-link.btn.btn-primary(class="nav-link" to="/login") I will try Log In Again...
</template>
<script>
export default {
  name: 'registration-form',
  data () {
    return {
      'username': '',
      'email': '',
      'password': '',
      'repeat': ''
    }
  },
  methods: {
    registration() {
      if (this.password==this.repeat)
        this.$store.dispatch('register',
          { username: this.username,
          email: this.email,
          password: this.password})
        .then()
        .catch()
    },
    submitForm(event) {
      this.registration()
      this.password = ''
      this.repeat = ''
      event.preventDefault()
    },
  }
}
</script>
