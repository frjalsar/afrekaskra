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
          >Félagasaga er byggð á skráðum afrekum. Stundum eru afrek skráð á
          hérðaðssamband, landslið eða lið í bikarkeppni, en ekki félag
          keppanda. Því getur félagasaga verið röng í sumum tilfellum.
          Félagaskipti birtast ekki hér fyrr en keppt hefur verið fyrir nýja
          félagið.
        </small>
      </p>
      <table
        class="table table-striped table-hover table-responsive-sm table-sm"
      >
        <!--<caption>Listi yfir óvirk Íslandsmet</caption>-->
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col">Félag</th>
            <th scope="col">Frá</th>
            <th scope="col">Til</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in club_history">
            <th scope="row">
              {{ i.club }}
              &nbsp;&nbsp;
              <img
                class="img-club"
                v-bind:src="'/api/img/club/' + i.club"
                alt=""
              />
            </th>
            <td>{{ i.from | formatDate }}</td>
            <td>{{ i.to | formatDate }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  props: ["club_history"],
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

.img-club {
  height: 25px;
}
</style>
