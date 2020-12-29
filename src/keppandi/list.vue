<template>
  <div>
    <div class="card bg-light mt-4">
      <h4 class="card-header">Finna íþróttamann</h4>
      <div class="card-body">
        <p class="card-text">
          Byrjaðu að slá inn nafn íþróttamanns og Sif hjálpar þér að finna hana
          eða hann.
        </p>
        <KeppandiSearch />
      </div>
    </div>
  </div>
</template>

<script>
import KeppandiSearch from "./components/Search.vue";

export default {
  components: {
    KeppandiSearch,
  },
  mounted() {
    document.title = "Afrekaskrá FRÍ"; //Reset the title
  },
};
</script>