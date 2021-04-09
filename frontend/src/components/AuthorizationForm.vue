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
        input.form-input(type="password" v-model="password" placeholder="Password")
    .form-group
      .col-2
      .col-9
        button.btn.btn-primary(type="submit") Go!
    hr
    .form-group
      .col-2
      .col-9
        router-link.btn.btn-primary(class="nav-link" to="/registration") Create Fresh Account!
</template>
<script>
export default {
  name: 'authorization-form',
  data() {
    return {
      'username': '',
      'password': ''
    }
  },
  methods: {
    signIn() {
      this.$store.dispatch('signIn', {username: this.username, password: this.password})
      .then()
    },
    submitForm(event) {
      this.signIn()
      this.password = ''
      event.preventDefault()
    },
  },
}
</script>
