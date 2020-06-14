<template>
  <div>
      <h1>(404) Síða fannst ekki.</h1>
  </div>
</template>

<script>
export default {
  name: '404NotFound',
  data () {
    return {
      disabled: true,
      myID: 'Nothing'
    }
  },
  created() {
      console.log(this.$route.params)
      console.log(this.$route.query)
  }
}
</script>