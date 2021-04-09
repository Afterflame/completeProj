<template  lang="pug">
  .column.col-10.col-md-10.text-left
    button.btn.float-left(@click="LogOut()") Log Out
    router-link.btn(class="nav-link" to="/") Main
    header.text-left
      hr
      h2 Yep, that's me!
      profile-form
</template>

<script>
  import ProfileForm from '@/components/ProfileForm'

  export default {
  name: 'ProfileTemp',
  components: {
    'profile-form': ProfileForm
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

