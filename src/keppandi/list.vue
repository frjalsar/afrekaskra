<template>
  <div>
      <p>Keppenda listi {{ myID }}</p>
  </div>
</template>

<script>
export default {
  name: 'KeppandiList',
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