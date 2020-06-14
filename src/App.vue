<template>
  <div id="app">
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
      <a href="/#/">
        <img
          alt="Frjálsíþróttasamband Íslands"
          src="./fri-logo.png"
          class="logo"
        >
      </a>
      <a
        href="/#/"
        class="mr-md-auto title-link"
      >
        <h5 class="my-0 font-weight-normal">
          Afrekaskrá FRÍ
        </h5>
      </a>
      <nav class="my-2 my-md-0 mr-md-3">
        <router-link
          to="/top"
          class="p-2 text-dark"
        >
          Top listar
        </router-link>
        <router-link
          to="/islmet"
          class="p-2 text-dark"
        >
          Íslandsmet
        </router-link>
        <router-link
          to="/arsbest"
          class="p-2 text-dark"
        >
          Ársbest
        </router-link>
        <router-link
          to="/keppandi"
          class="p-2 text-dark"
        >
          Keppandi
        </router-link>
    </div>
    <div class="container">
      <div class="my-5 p-3 bg-white rounded shadow">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style>
img.logo {
  margin-right: 10px;
  width: 50px
}
h1 {
  text-transform: uppercase;
}
</style>

<style>
a.title-link {
  text-decoration: none;
  color: #343a40;
}

</style>
