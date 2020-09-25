<template>
  <div>
    <div class="card mt-4">
      <div class="card-body">
        <h5 class="card-title">Velkominn til Sifjar</h5>
        <p>
          Sif heldur utan um afrekaskrá
          <a href="http://www.fri.is">Frjálsíþróttasambands Íslands</a> (FRÍ) og
          er eiginkona <a href="http://thor.fri.is">Þórs</a> mótaforrits FRÍ.
          <!--Þór var skapaður af
          <a href="/keppandi/2487">Friðrik Þór</a> til að safna saman gögnum um íslenska keppendur í frjálsum íþróttum.-->
          <!--Sif fær öll gögnin sín frá Þór og vinnur úr þeim.-->
          <!--Jötnarnir <a href="/keppandi/17364">Kristinn</a>, <a href="/keppandi/20844">Bergur</a> og <a href="/keppandi/76227">Þorsteinn</a> kenndu Sif að vinna
          úr gögnunum frá Þór.-->
        </p>
      </div>
    </div>
    <!---->
    <div class="card mt-4">
      <div class="card-header">Finna íþróttamann</div>
      <div class="card-body">
        <p class="card-text">
          Byrjaðu að slá inn nafn íþróttamanns og Sif hjálpar þér að finna hana
          eða hann.
        </p>
        <KeppandiList />
      </div>
    </div>
    <!---->
    <div class="card mt-4">
      <div class="card-header">Top listar</div>
      <div class="card-body">
        <p class="card-text">
          Veldu grein hér að neðan og Sif sýnir þér 100 bestu afrek hvers árs
          eða frá upphafi.
        </p>
        <p>To do: setja dropbox fyrir greinar</p>
      </div>
    </div>
    <!---->
    <div class="card mt-4">
      <div class="card-header">Íslandsmet</div>
      <div class="card-body">
        <p class="card-text">
          Todo: Listi yfir Íslandsmet sem voru nýlega sett?
        </p>
        <p class="card-text">Todo: Listi yfir elstu Íslandsmetin??</p>
        <p class="card-text">Todo: Listi yfir þá sem eiga flest Íslandsmet?</p>
        <ISLRecordBirtdayList />
      </div>
    </div>
    <!---->
    <div class="card mt-4">
      <div class="card-header">Fyrirspurn</div>
      <div class="card-body">
        <p class="card-text">
          Ertu með flóknari fyrirspurn. Prófaðu að spyrja Þór með því að smella
          <a href="http://mot.fri.is/MotFRI/Statistics.aspx"
            >hér <i class="fas fa-external-link-alt"></i></a
          >.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import KeppandiList from "./keppandi/list.vue";
import ISLRecordBirtdayList from "./islmet/ISLRecordBirtdayList.vue";

export default {
  components: {
    KeppandiList,
    ISLRecordBirtdayList,
  },
  mounted() {
    document.title = "Afrekaskrá FRÍ"; //Reset the title
  },
};
</script>