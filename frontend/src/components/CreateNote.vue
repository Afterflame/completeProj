<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-1
      .col-10
        input.form-input(v-model="author", placeholder="Enter Nickname")
    .form-group
      .col-1
      .col-10
        textarea.form-input(v-model="body" rows=8 placeholder="Let 'em know")
    .form-group
      .col-1
      .col-10
        button.btn.btn-primary(type="submit") Create
</template>
<script>
export default {
  name: 'create-note',
  data () {
    return {
      'author': '',
      'body': ''
    }
  },
  methods: {
    createNote () {
      this.$store.dispatch('createNote', { author:this.author, body: this.body})
    },
    submitForm (event) {
      this.createNote()
      this.body = ''
      event.preventDefault()
    },
  },
}
</script>
