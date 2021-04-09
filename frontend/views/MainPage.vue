<template  lang="pug">
  .column.col-15.col-md-2

    button.btn.float-left(@click="LogOut()") Log Out
    router-link.btn(class="nav-link" to="/profile") Account
    header.text-center
      h1 1Dch
      create-note
    header.text-center
      h2 Wall
      note-list
</template>

<script>
  import CreateNote from '@/components/CreateNote'
  import NoteList from '@/components/NoteList'

  export default {
  name: 'MainTemp',
  components: {
    'create-note': CreateNote,
    'note-list': NoteList
  },
  methods: {
    LogOut() {
      this.$store.commit('CLEAR_TOKEN')
      this.$router.push('/login')
    },
  },beforeMount() {
    if (this.$store.getters.token=="")
      this.LogOut()
    }
}
</script>

