<template>
  <div>
    <div v-if="loading">
      <hr />
      <pulse-loader
        :loading="loading"
        :color="color"
        :size="size"
      ></pulse-loader>
    </div>
    <div v-if="!loading">
      <hr />
      <h2 class="display-4"><i class="fas fa-exchange-alt"></i> Félagasaga</h2>
      <p>
        <small
          >Félagasaga er byggð á skráðum afrekum. Hún getur verið röng ef afrek
          hafa ekki verið skráð á félag keppanda. Stundum eru afrek skráð á
          hérðaðssamband, landslið eða lið í bikarkeppni.
        </small>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "ClubHistory",
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

      history: [],
    };
  },
};
</script>

<style scoped>
/* center spinner */
.v-spinner {
  text-align: center;
}
</style>
