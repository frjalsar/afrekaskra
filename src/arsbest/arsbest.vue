<template>
  <div>
      <p>Ársbest {{ myID }}</p>
  </div>
</template>

<script>
export default {
  name: 'Arsbest',
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