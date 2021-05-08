<template>
  <div>
    <div v-if="loading">
      <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
    </div>
    <div v-if="!loading">
    <p>Top list stuff</p>
    <div>
  </div>
</template>

<script>
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  components: {
    PulseLoader,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      loading: false,
      message: "",
    };
  },
  created() {
    //
  },
  computed: {
      //
  },
  methods: {
      //
  },
};
</script>

<style scoped>
.v-spinner {
  text-align: center;
}
</style>
