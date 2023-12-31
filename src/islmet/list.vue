<template>
  <div>
    <a href="http://mot.fri.is/MotFRI/Islandsmet.aspx">Íslands- og aldursflokkamet</a>
    <br />
    <br />
    <a href="http://mot.fri.is/MotFRI/Oldungamet.aspx">Öldungamet</a>
  </div>
</template>

<script>
export default {
  name: "IslmetList",
  data() {
    return {
      isReady: false,
    };
  },
  //   mounted() {
  //}
};
</script>

<style scoped>
.html,
body {
  height: 100%;
  width: 100%;
  margin: 0;
}

.h_iframe iframe {
  width: 100%;
  height: 100%;
}

.h_iframe {
  height: auto;
  width: 100%;
}

.contentFrame {
  border: none;
  padding: 0;
  margin: 0;
  background-color: pink;
  height: 100%;
  vertical-align: bottom;
}
</style>