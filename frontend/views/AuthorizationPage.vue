<template  lang="pug">
  .column.col-8.col-md-12
    header.text-center
      h2 Log Me In!
      authorization-form
</template>

<script>

  import AuthorizationForm from '@/components/AuthorizationForm'

  export default {
  name: 'AuthorizationTemp',
  components: {
    'authorization-form': AuthorizationForm
  },
}
</script>

