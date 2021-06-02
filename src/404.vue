<template>
  <div>
    <h1>(404) Síða fannst ekki. / Page not found.</h1>
  </div>
</template>

<script>
export default {
  name: "404NotFound",
  metaInfo() {
    return {
      title: "404 - Síða fannst ekki / page not found",
      meta: [{ name: "robots", content: "noindex" }],
    };
  },
  data() {
    return {
      loading: false,
    };
  },
  created() {
    console.log(this.$route.params);
    console.log(this.$route.query);
  },
};
</script>