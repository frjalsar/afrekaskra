<template>
    <div>
      <!-- <div class="search-div">
        <p>Sláðu inn nafn til að leita af öðrum keppanda</p>
        <KeppandiList />
      </div> -->
      <!-- LOADING -->
      <div v-if="!isReady">
        <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
        <p style="text-align: center">{{ message }}</p>
        <!--<img src="../assets/fri-loading-1.gif" alt="Hleð síðu" width=100%>-->
        <video autoplay loop muted playsinline width="100%">
          <source src="../assets/fri-loading-1.webm" type="video/webm" />
        </video>
      </div>
        <div>
            Hello
        </div>
      </div>
    <!--</div>-->
  </template>
  
  <script>
  import axios from "axios";
  import PulseLoader from "vue-spinner/src/PulseLoader.vue";
  
  export default {
    name: "Compare",
    components: {
      PulseLoader,
    },
    data() {
      return {
        color: "#0275d8",
        size: "15px",
        margin: "2px",
        radius: "100%",
  
        competitor_info: [],
        event_info: [],
        club_history: [],
        isReady: false,
        competitorID: null,
        message: "",
        api_url_prefix: this.global_api_url_prefix,
        showClubLogo: true,
      };
    },
    created() {
      this.get_data();
    },
    methods: {
      get_data: function () {
        this.message = "Næ í gögn ekki stökkva langt 😉";
  
        this.data = [];
        //console.log('Getting data')

        this.isReady = true;
      },
    },
  };
  </script>
  
  <style scoped>
  /* center spinner */
  .v-spinner {
    text-align: center;
  }
  
  .search-div {
    margin-bottom: 10px;
  }
  
  .action-div {
    position: relative;
  }
  
  .topleft {
    position: absolute;
    top: 8px;
    left: 16px;
    color: #ffffff;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.75);
  }
  
  .bottomleft {
    position: absolute;
    bottom: 8px;
    left: 16px;
  }
  
  .bottomright {
    position: absolute;
    bottom: 8px;
    right: 16px;
  }
  
  .img-action {
    width: 100%;
    height: auto;
  }
  
  /* xs */
  .img-club {
    background: transparent;
    width: 50px;
    height: auto;
  }
  
  /* sm */
  @media (min-width: 768px) {
    .img-club {
      width: 75px;
    }
  }
  
  /* md */
  @media (min-width: 992px) {
    .img-club {
      width: 100px;
    }
  }
  
  /* lg */
  @media (min-width: 1200px) {
    .img-club {
      width: 125px;
    }
  }
  
  /* xs */
  .img-profile {
    width: 50px;
    height: auto;
  }
  
  /* sm */
  @media (min-width: 768px) {
    .img-profile {
      width: 75px;
    }
  }
  
  /* md */
  @media (min-width: 992px) {
    .img-profile {
      width: 100px;
    }
  }
  
  /* lg */
  @media (min-width: 1200px) {
    .img-profile {
      width: 125px;
    }
  }
  </style>