<template lang="pug">
  #app
    .card(v-for="note in notes")
      .card-header
        .card-subtitle(style="text-align:left;") {{ note.date}}
        .card-title(style="text-align:left;") {{  note.author }}
      .card-body.align-left(style="text-align:left;") {{ note.body }}
</template>
<script>
import { mapGetters } from 'Vuex'
export default {
  name: 'note-list',
  computed: mapGetters(['notes']),
  beforeMount () {
    this.$store.dispatch('getNotes')
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
