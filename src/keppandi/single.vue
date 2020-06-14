<template>
  <div>
      <p>Keppandi {{ myID }}</p>
  </div>
</template>

<script>
export default {
  name: 'KeppandiSingle',
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