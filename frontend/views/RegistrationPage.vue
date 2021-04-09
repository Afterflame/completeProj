<template  lang="pug">
  .column.col-8.col-md-12
    header.text-center
      h2 Create New Account!
      registration-form
</template>

<script>
  import RegistrationForm from '@/components/RegistrationForm'

  export default {
  name: 'RegistrationTemp',
  components: {
    'registration-form': RegistrationForm
  },
  methods: {
    LogOut() {
      this.$store.commit('CLEAR_TOKEN')
      this.$router.push('/login')
    },
  },
    beforeMount() {
    if (this.$store.getters.token=="")
      this.LogOut()
    }
}
</script>

