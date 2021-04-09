<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-9
        input.form-input(type="text" v-model="username", readOnly)
      .col-2
        label.form-label - Login
    .form-group
      .col-9
        input.form-input(type="email" v-model="email", readOnly)
      .col-2
        label.form-label - Email
    hr
</template>
<script>
export default {
  name: 'profile-form',
  data() {
    return {
      'username': '',
      'email': '',
      'password': '',
      'repeat': '',
    }
  },
  methods: {
    changePassword() {
      if(this.password == this.repeat)
        this.$store.dispatch('changePassword', { password : this.password } )
    },
    submitForm(event) {
      this.changeProfileData()
      event.preventDefault()
    },
    LogOut() {
      this.$store.commit('CLEAR_TOKEN')
      this.$router.push('/login')
    },
    UpdateSigns() {
    this.first_name=this.$store.getters.first_name
    this.email=this.$store.getters.email
    this.username=this.$store.getters.username
    console.log(this.username)
    }
  },
  beforeMount() {
    this.UpdateSigns()
  }
}
</script>
