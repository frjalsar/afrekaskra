<template>
  <div>
    <div class="card bg-light mt-4">
      <div class="card-body">
        <h4 class="card-title"><img src="./assets/FRI-Logo-Black-RGB.png" style="height: 1em;vertical-align: baseline;"> Afrekaskrá FRÍ</h4>
        <p>
          Hér er haldið utan tölfræði á afrekum í frjálsum íþróttum. Öll gögn koma úr <a href="http://thor.fri.is">Þór</a>
          mótaforriti <a href="http://www.fri.is">Frjálsíþróttasambands Íslands</a>.
        </p>
      </div>
    </div>
    <!---->
    <div class="card bg-light mt-4">
      <h4 class="card-header"><i class="fas fa-user"></i> Finna iðkanda</h4>
      <div class="card-body">
        <p class="card-text">
          Byrjaðu að slá inn nafn iðkanda og afrekaskráin hjálpar þér að finna hana
          eða hann. Smelltu <router-link :to="{ path: 'keppandi' }">hér</router-link> til að fá upp ýtarlegri leit.
        </p>
        <KeppandiSearch />
      </div>
    </div>
    <!---->
    <div class="card bg-light mt-4">
      <h4 class="card-header"><i class="fas fa-list-ol"></i> Top listar</h4>
      <div class="card-body">
        <FrontTopList />
      </div>
    </div>
    <!---->
    <div class="card bg-light mt-4">
      <h4 class="card-header"><i class="fas fa-flag"></i> Íslandsmet</h4>
      <div class="card-body">
        <!--<p class="card-text">
          Todo: Listi yfir Íslandsmet sem voru nýlega sett?
        </p>-->
        <!--<p class="card-text">Todo: Listi yfir elstu Íslandsmetin??</p>-->
        <!--<p class="card-text">Todo: Listi yfir þá sem eiga flest Íslandsmet?</p>-->
        <ISLRecordBirtdayList />
      </div>
    </div>
    <!---->
    <!--<div class="card bg-light mt-4">
      <h4 class="card-header">Fyrirspurn</h4>
      <div class="card-body">
        <p class="card-text">
          Ertu með flóknari fyrirspurn. Prófaðu að spyrja Þór með því að smella
          <a href="http://mot.fri.is/MotFRI/Statistics.aspx"
            >hér <i class="fas fa-external-link-alt"></i></a
          >.
        </p>
      </div>
    </div>-->
  </div>
</template>

<script>
import KeppandiSearch from "./keppandi/components/Search.vue";
import ISLRecordBirtdayList from "./islmet/ISLRecordBirtdayList.vue";
import FrontTopList from "./top/FrontTopList.vue";

export default {
  components: {
    KeppandiSearch,
    ISLRecordBirtdayList,
    FrontTopList,
  },
  mounted() {
    document.title = "Afrekaskrá FRÍ"; //Reset the title
  },
};
</script>