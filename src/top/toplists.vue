<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="row mb-4">
          <div class="col">
            <ul
              class="nav nav-pills nav-fill card-header-tabs pull-right"
              id="myTab"
              role="tablist"
            >
              <!-- https://codepen.io/surjithctly/pen/PJqKzQ -->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  id="navbarDropdownMenuLink"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >{{eventText}}</a>
                <ul
                  v-on:click="event_change($event)"
                  class="dropdown-menu"
                  aria-labelledby="navbarDropdownMenuLink"
                >
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===1)}"
                      class="dropdown-item dropdown-toggle"
                    >Stökkgreinar</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_jump">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===2)}"
                      class="dropdown-item dropdown-toggle"
                    >Kastgreinar</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_throw">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===3)}"
                      class="dropdown-item dropdown-toggle"
                    >Spretthlaup</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_sprint">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===4)}"
                      class="dropdown-item dropdown-toggle"
                    >Grindarhlaup</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_hurdle">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===5)}"
                      class="dropdown-item dropdown-toggle"
                    >Millivegalengdir</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_middle">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===6)}"
                      class="dropdown-item dropdown-toggle"
                    >Langhlaup</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_long">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{active: (event_type===7)}"
                      class="dropdown-item dropdown-toggle"
                    >Þrautagreinar</a>
                    <ul class="dropdown-menu">
                      <li v-for="i in events_athlon">
                        <a
                          v-bind:class="{active: (event_id===i.id)}"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                        >{{i.name}}</a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <!-- Women = 2, Men = 1-->
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-toggle="dropdown" role="button"
              aria-haspopup="true" aria-expanded="false">{{sexText}}</a>
            <div class="dropdown-menu" id="sexDropdown">
              <a v-on:click="toogle_sex($event, 2)" class="dropdown-item" id="1">Konur</a>
              <a v-on:click="toogle_sex($event, 1)" class="dropdown-item" id="2">Karlar</a>
            </div>
              </li>
              <!---->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                >{{yearText}}</a>
                <div
                  v-on:click="year_change($event)"
                  class="dropdown-menu dropdown-menu-long"
                  id="activeyearDropdown"
                >
                  <a v-bind:class="{active: year===0}" class="dropdown-item" id="0">Öll ár</a>
                  <a
                    v-bind:class="{active: year===i}"
                    v-for="i in year_list"
                    class="dropdown-item"
                    :id="i"
                  >{{i}}</a>
                </div>
              </li>
              <!---->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                >{{ageText}}</a>
                <div v-on:click="age_change($event)" class="dropdown-menu" id="ageDropdown">
                  <a
                    v-for="i in ageGroups"
                    v-bind:class="{active: ageGroup===i.id}"
                    class="dropdown-item"
                    :id="i.id"
                  >{{i.name}}</a>
                </div>
              </li>
              <!---->
            </ul>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <div class="row justify-content-center">
              <div class="col-md-4 col-sm-12 mb-3 text-center">
                <div class="custom-control custom-switch">
                  <input
                    v-on:click="toggle_bestbyath($event)"
                    type="checkbox"
                    class="custom-control-input"
                    id="customSwitch2"
                    :checked="isBestByAthActive"
                  />
                  <label
                    class="custom-control-label"
                    for="customSwitch2"
                  >Birta bara besta afrek íþróttamanns</label>
                </div>
              </div>
              <div class="col-md-4 col-sm-12 mb-3 text-center">
                <div class="custom-control custom-switch">
                  <input
                    v-on:click="toggle_legalresults($event)"
                    type="checkbox"
                    class="custom-control-input"
                    id="customSwitch1"
                    :checked="!isLegalActive"
                  />
                  <label class="custom-control-label" for="customSwitch1">Birta ólöglegan árangur</label>
                </div>
              </div>
              <div class="col-md-4 col-sm-12 mb-3 text-center">
                <div class="custom-control custom-switch">
                  <input
                    v-on:click="toggle_isl($event)"
                    type="checkbox"
                    class="custom-control-input"
                    id="customSwitch3"
                    :checked="!isISLActive"
                  />
                  <label class="custom-control-label" for="customSwitch3">Birta öll þjóðerni</label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Outdoor = 0, Indoor = 1 -->
        <div class="row">
          <div class="col">
            <div class="row justify-content-center">
              <div class="col-md-4 col-sm-12 mb-3 text-center">
                <div class="btn-group btn-group-toggle" data-toggle="buttons">
                  <label class="btn" v-bind:class="{'btn-primary': (outin===1), 'btn-secondary': (outin!==1)}">
                    <input v-on:click="toogle_innout($event, 1)" type="radio" name="options" id="option1" autocomplete="off" /> Innanhús
                  </label>
                  <label class="btn" v-bind:class="{'btn-primary': (outin===2), 'btn-secondary': (outin!==2)}">
                    <input v-on:click="toogle_innout($event, 2)" type="radio" name="options" id="option2" autocomplete="off" /> Innan og utanhús
                  </label>
                  <label class="btn" v-bind:class="{'btn-primary': (outin===0), 'btn-secondary': (outin!==0)}">
                    <input v-on:click="toogle_innout($event, 0)" type="radio" name="options" id="option3" autocomplete="off" /> Utanhús
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card-body">
        <div class="tab-content" id="myTabContent">
          <div
            class="tab-pane fade show active"
            id="datatab"
            role="tabpanel"
            aria-labelledby="data-tab"
          >
            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------- -->
            <table class="table table-striped table-responsive-sm">
              <thead>
                <tr>
                  <th class="d-none d-sm-table-cell" scope="col">#</th>
                  <th scope="col">Árangur</th>
                  <th v-bind:class="{'d-none': !hasWind}" scope="col">Vindur</th>
                  <th scope="col">Nafn</th>
                  <th class="d-none d-sm-table-cell" scope="col">Aldur</th>
                  <th class="d-none d-sm-table-cell" scope="col">Félag</th>
                  <th class="d-none d-xl-table-cell" scope="col">Mót</th>
                  <th class="d-none d-md-table-cell" scope="col">Dags.</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(competitor, index) in data">
                  <th class="d-none d-sm-table-cell" scope="row">{{index+1}}</th>
                  <td>{{competitor.results}}</td>
                  <td v-bind:class="{'d-none': !hasWind}">{{competitor.wind}}</td>
                  <td>
                    <a v-bind:href="'/keppandi/' + competitor.competitor_code">{{competitor.name}}</a>
                  </td>
                  <td class="d-none d-sm-table-cell">{{competitor.age}}</td>
                  <td class="d-none d-sm-table-cell">{{competitor.club}}</td>
                  <td class="d-none d-xl-table-cell">
                    <a
                      v-bind:href="'http://mot.fri.is/MotFRI/SelectedCompetitionResults.aspx?Code=' + competitor.competition_id"
                    >{{competitor.competition_name}}</a>
                  </td>
                  <td class="d-none d-md-table-cell">{{competitor.date}}</td>
                </tr>
              </tbody>
            </table>
            <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
            <p align="center">{{message}}</p>
            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------- -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "TopLists",
  components: {
    PulseLoader
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",
      loading: false,

      data: [],
      event: [],
      message: "",

      isBestByAthActive: true,
      isLegalActive: true,
      isISLActive: true,

      event_id: 154, // Event_id
      event_type: 1, //Jumps = 1, Throws = 2, Sprint = 3, Hurdles = 4, Middle = 5, Long = 6, -athlon = 7
      outin: 1, // Outdoor = 0, Indoor = 1
      gender: 2, // Women = 2, Men = 1
      year: new Date().getFullYear(), // Year
      year_list: [],
      ageGroup: 0,
      ageStart: 0, // Start age
      ageEnd: 999, // End age
      legal: 1, // Only legal = 1, all = 0
      isl: 0, // Icelandic = 0, Everybody = 1
      bestbyath: 1,

      events_jump: [
        { id: 124, type: 1, name: "Hástökk" },
        { id: 125, type: 1, name: "Hástökk án atrennu" },
        { id: 154, type: 1, name: "Langstökk" },
        { id: 155, type: 1, name: "Langstökk án atrennu" },
        { id: 197, type: 1, name: "Stangarstökk" },
        { id: 204, type: 1, name: "Þrístökk" }
      ],
      events_throw: [
        { id: 129, type: 2, name: "Kringlukast (2,0 kg)" },
        { id: 130, type: 2, name: "Kringlukast (1,5 kg)" },
        { id: 131, type: 2, name: "Kringlukast (1,0 kg)" },
        { id: 135, type: 2, name: "Kringlukast (1,75kg)" },
        { id: 138, type: 2, name: "Kúluvarp (7,26 kg)" },
        { id: 139, type: 2, name: "Kúluvarp (6,00 kg)" },
        { id: 140, type: 2, name: "Kúluvarp (5,0 kg)" },
        { id: 142, type: 2, name: "Kúluvarp (4,0 kg)" },
        { id: 143, type: 2, name: "Kúluvarp (2,0 kg)" },
        { id: 144, type: 2, name: "Kúluvarp (3,0 kg)" },
        { id: 176, type: 2, name: "Sleggjukast (7,26 kg)" },
        { id: 177, type: 2, name: "Sleggjukast (4,0 kg)" },
        { id: 178, type: 2, name: "Sleggjukast (2,0 kg)" },
        { id: 179, type: 2, name: "Sleggjukast (3,0 kg)" },
        { id: 181, type: 2, name: "Sleggjukast (5,0 kg)" },
        { id: 183, type: 2, name: "Sleggjukast (6,0 kg)" },
        { id: 187, type: 2, name: "Spjótkast (800 gr)" },
        { id: 189, type: 2, name: "Spjótkast (600 gr)" },
        { id: 190, type: 2, name: "Spjótkast (400 gr)" },
        { id: 191, type: 2, name: "Spjótkast (500 gr)" }
      ],
      events_sprint: [
        { id: 74, type: 3, name: "60 m" },
        { id: 6, type: 3, name: "100 m" },
        { id: 25, type: 3, name: "200 m" },
        { id: 31, type: 3, name: "300 m" },
        { id: 44, type: 3, name: "400 m" },
        { id: 50, type: 3, name: "4x100 m boðhlaup" },
        { id: 52, type: 3, name: "4x200 m boðhlaup" },
        { id: 54, type: 3, name: "4x400 m boðhlaup" },
        { id: 5, type: 3, name: "1000 m boðhlaup" }
      ],
      events_hurdle: [
        { id: 7, type: 4, name: "100 m gr. (84 cm)" },
        { id: 8, type: 4, name: "100 m gr. (76,2 cm)" },
        { id: 11, type: 4, name: "100 m gr. (91,4 cm)" },
        { id: 15, type: 4, name: "110 m gr. (106,7 cm)" },
        { id: 16, type: 4, name: "110 m gr. (91,4 cm)" },
        { id: 17, type: 4, name: "110 m gr. (99,1 cm)" },
        { id: 45, type: 4, name: "400 m gr. (91,4 cm)" },
        { id: 46, type: 4, name: "400 m gr. (84 cm)" },
        { id: 47, type: 4, name: "400 m gr. (76,2 cm)" },
        { id: 75, type: 4, name: "60 m gr. (106,7 cm)" },
        { id: 77, type: 4, name: "60 m gr. (91,4 cm)" },
        { id: 78, type: 4, name: "60 m gr. (99,1 cm)" },
        { id: 80, type: 4, name: "60 m gr. (76,2 cm)" },
        { id: 82, type: 4, name: "60 m gr. (84,0 cm)" }
      ],
      events_middle: [
        { id: 18, type: 5, name: "1500 m" },
        { id: 28, type: 5, name: "3000 m" },
        { id: 30, type: 5, name: "3000 m hindrun" },
        { id: 73, type: 5, name: "600 m" },
        { id: 86, type: 5, name: "800 m" }
      ],
      events_long: [
        { id: 3, type: 6, name: "10.000 metra hlaup" },
        { id: 12, type: 6, name: "10 km götuhlaup (flögutímar)" },
        { id: 13, type: 6, name: "10 km götuhlaup" },
        { id: 57, type: 6, name: "5000 metra hlaup" },
        { id: 122, type: 6, name: "Hálft maraþon" },
        { id: 123, type: 6, name: "Hálft maraþon (flögutímar)" },
        { id: 166, type: 6, name: "Maraþon" },
        { id: 167, type: 6, name: "Maraþon (flögutímar)" }
      ],
      events_athlon: [
        { id: 1001, type: 7, name: "Fimmtarþraut" },
        { id: 1002, type: 7, name: "Fimmtarþr. unglingastig" },
        { id: 1003, type: 7, name: "Fimmtarþraut (76 cm gr.)" },
        { id: 1004, type: 7, name: "Fimmtarþraut pilta 15 ára" },
        { id: 1011, type: 7, name: "Sjöþraut" },
        { id: 1012, type: 7, name: "Sjöþraut (6 kg kúla)" },
        { id: 1013, type: 7, name: "Sjöþraut (5 kg kúla)" },
        { id: 1014, type: 7, name: "Sjöþraut meyjaáhöld" },
        { id: 1021, type: 7, name: "Tugþraut" },
        { id: 1022, type: 7, name: "Tugþraut 16-17 ára" },
        { id: 1023, type: 7, name: "Tugþraut U20 (Norðurlönd)" }
      ],
      ageGroups: [
        { id: 0, name: "Allir aldursflokkar", ageStart: 0, ageEnd: 999 },
        { id: 1, name: "20-22 ára", ageStart: 20, ageEnd: 22 },
        { id: 2, name: "18-19 ára", ageStart: 18, ageEnd: 19 },
        { id: 3, name: "16-17 ára", ageStart: 16, ageEnd: 17 },
        { id: 4, name: "15 ára", ageStart: 15, ageEnd: 15 },
        { id: 5, name: "14 ára", ageStart: 14, ageEnd: 14 },
        { id: 6, name: "13 ára", ageStart: 13, ageEnd: 13 },
        { id: 7, name: "12 ára", ageStart: 12, ageEnd: 12 }
      ]
    };
  },
  mounted() {
    //let extScript = document.createElement('script')
    //extScript.setAttribute('src', 'static/extScript.js')
    //document.head.appendChild(extScript)

    var scriptTag = document.createElement("script");
    scriptTag.type = "text/javascript";
    scriptTag.text = `$('.dropdown-menu a.dropdown-toggle').on('click', function (e) {
    if (!$(this).next().hasClass('show')) {
      $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
    }
    var $subMenu = $(this).next(".dropdown-menu");
    $subMenu.toggleClass('show');

    $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function (e) {
      $('.dropdown-submenu .show').removeClass("show");
    });

    return false;
  });`;
    document.body.appendChild(scriptTag);
  },
  computed: {
    testPar: function() {
      //return 'Hello'
      return this.$route.params.test;
    },
    ageText: function() {
      return this.ageGroups[this.ageGroup].name;
    },
    yearText: function() {
      if (this.year === 0) {
        return "Öll ár";
      } else {
        return this.year.toString();
      }
    },
    sexText: function() {
      if (this.gender === 1) {
        var sexText = "Karlar";
      } else {
        var sexText = "Konur";
      }

      return sexText;
    },
    eventText: function() {
      if (this.event_type === 1) {
        var index = this.events_jump.findIndex(p => p.id == this.event_id);
        return this.events_jump[index].name;
      } else if (this.event_type === 2) {
        var index = this.events_throw.findIndex(p => p.id == this.event_id);
        return this.events_throw[index].name;
      } else if (this.event_type === 3) {
        var index = this.events_sprint.findIndex(p => p.id == this.event_id);
        return this.events_sprint[index].name;
      } else if (this.event_type === 4) {
        var index = this.events_hurdle.findIndex(p => p.id == this.event_id);
        return this.events_hurdle[index].name;
      } else if (this.event_type === 5) {
        var index = this.events_middle.findIndex(p => p.id == this.event_id);
        return this.events_middle[index].name;
      } else if (this.event_type === 6) {
        var index = this.events_long.findIndex(p => p.id == this.event_id);
        return this.events_long[index].name;
      } else if (this.event_type === 7) {
        var index = this.events_athlon.findIndex(p => p.id == this.event_id);
        return this.events_athlon[index].name;
      }
    },
    titleText: function() {
      var my_str =
        "Sif - Afrek " +
        this.eventText +
        " " +
        this.outinsexText +
        " í " +
        this.ageText +
        " fyrir " +
        this.yearText;

      return my_str;
    },
    hasWind: function() {
      if ((this.outin === 0) || (this.outin === 2)) {
        // We are outdoor. Does the current selected event have wind?
        if (this.event["HasWind"] === 1) {
          return true;
        } else {
          return false;
        }
      } else {
        return false; // We are indoor, no wind
      }
    }
  },
  created() {
    var year_start = 1909;
    var year_end = this.year;
    this.year_list = [];
    while (year_end + 1 > year_start) {
      this.year_list.push(year_end--);
    }

    var parameters = this.$route.query;
    if ("y" in parameters) {
      this.year = Number(this.$route.query.y);
    }
    if ("a" in parameters) {
      this.ageGroup = Number(this.$route.query.a);
      this.ageStart = this.ageGroups[this.ageGroup].ageStart;
      this.ageEnd = this.ageGroups[this.ageGroup].ageEnd;
    }
    if ("g" in parameters) {
      this.gender = Number(this.$route.query.g);
    }
    if ("i" in parameters) {
      this.outin = Number(this.$route.query.i);
    }
    if ("l" in parameters) {
      this.legal = Number(this.$route.query.l);

      if (this.legal === 1) {
        this.isLegalActive = true;
      } else {
        this.isLegalActive = false;
      }
    }
    if ("b" in parameters) {
      this.bestbyath = Number(this.$route.query.b);

      if (this.bestbyath === 1) {
        this.isBestByAthActive = true;
      } else {
        this.isBestByAthActive = false;
      }
    }
    if ("isl" in parameters) {
      this.isl = Number(this.$route.query.isl);

      if (this.isl === 0) {
        this.isISLActive = true;
      } else {
        this.isISLActive = false;
      }
    }
    if ("t" in parameters) {
      this.event_type = Number(this.$route.query.t);
    }
    if ("e" in parameters) {
      this.event_id = Number(this.$route.query.e);
    }

    this.get_data(null);
  },
  methods: {
    get_data: function(event) {
      this.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.data = [];

      const url = this.global_API_URL + 
        "/api/top_list/" +
        this.event_id +
        "/" +
        this.outin +
        "/" +
        this.gender +
        "/" +
        this.year +
        "/" +
        this.ageStart +
        "/" +
        this.ageEnd +
        "/" +
        this.legal +
        "/" +
        this.isl +
        "/" +
        this.bestbyath +
        "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.data = response[0]["data"]["TopList"];

            this.event = response[0]["data"]["EventInfo"];

            if (this.data.length === 0) {
              this.message =
                "Engin gögn fundust fyrir " +
                this.eventText +
                " " +
                this.outinsexText +
                " í " +
                this.ageText +
                " fyrir " +
                this.yearText +
                " 😟";
            } else {
              this.message = "";
              if (this.year !== 0) {
                this.data = this.cut_year(this.data);
              }
              this.data = this.convert_to_timeformat(
                this.event["Units"],
                this.data
              );
              if (this.outin === 2) {
              this.data = this.add_inndoor_sign(this.data);
            }
            }
          })
        )
        .catch(error => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
        })
        .finally(() => {
          this.loading = false;
          document.title = this.titleText;
        });
    },
    cut_year: function(my_data) {
      //Klippa út árið úr dags. ef eitt ár er valið
      var dataLen = my_data.length;
      for (var i = 0; i < dataLen; i++) {
        var split = my_data[i]["date"].split(" ");
        if (split.length === 3) {
          my_data[i]["date"] = split[0] + " " + split[1];
        }
      }

      return my_data;
    },
    add_inndoor_sign: function(my_data) {
      var dataLen = my_data.length;

      for (var i = 0; i < dataLen; i++)
      {
        if (my_data[i]['outdoor_indoor'] === 1) {
          my_data[i]["results"] = my_data[i]["results"] + ' (i)'
        }
      }

      return my_data;
    },
    convert_to_timeformat: function(unit, my_data) {
      // Breyta tíma úr sek í mm:ss,dd eða hh:mm:ss,dd eftir því hvaða grein er valin.
      //0, # No units!
      //'metrar': 1, # Meters
      //'sek.': 2, # ss,dd
      //'mín.': 3, # mm:ss,dd
      //'klst.': 4, # hh:mm:ss,dd
      //'stig': 5, # Points
      //'Ungl.stig': 6 # Points junior
      if (unit === 3 || unit === 4) {
        var dataLen = my_data.length;
        for (var i = 0; i < dataLen; i++) {
          var f = Number(my_data[i]["results"]);
          if (unit === 4) {
            // This unit has hours
            var h = Math.floor(f / 3600);
            f = f - h * 3600;
          } else {
            var h = 0;
          }
          var m = Math.floor(f / 60);
          var s = f - m * 60;
          var s_str;
          var m_str;
          var h_str;

          if (s < 10) {
            s_str = "0" + s.toFixed(2);
          } else {
            s_str = s.toFixed(2);
          }

          if (m < 10) {
            m_str = "0" + m.toFixed(0);
          } else {
            m_str = m.toFixed(0);
          }

          if (h < 10) {
            h_str = "0" + h.toFixed(0);
          } else {
            h_str = h.toFixed(0);
          }

          if (unit === 3) {
            my_data[i]["results"] = m_str + ":" + s_str;
          } else {
            my_data[i]["results"] = h_str + ":" + m_str + ":" + s_str;
          }
        }
      }

      return my_data;
    },
    test: function(event) {
      alert(event.target.id);
      console.log("Hi");
    },
    //Outdoor = 0, Indoor = 1
    //Women = 2, Men = 1 -->
    outinsex_change: function(event, outin, gender) {
      this.outin = outin;
      this.gender = gender;

      this.$router.push({ query: { ...this.$route.query, g: gender, i: outin } });
      this.get_data(event);
    },
    toogle_sex: function(event, gender) {
      this.gender = gender

      this.$router.push({ query: { ...this.$route.query, g: gender} });
      this.get_data(event);
    },
    toogle_innout(event, outin) {
      this.outin = outin

      this.$router.push({ query: { ...this.$route.query, i: outin } });
      this.get_data(event);
    },
    toggle_legalresults: function(event) {
      this.isLegalActive = !this.isLegalActive;
      if (this.isLegalActive === true) {
        this.legal = 1;
      } else {
        this.legal = 0;
      }

      this.$router.push({ query: { ...this.$route.query, l: this.legal } });
      this.get_data(event);
    },
    toggle_isl: function(event, isl) {
      this.isISLActive = !this.isISLActive;
      if (this.isISLActive === true) {
        this.isl = 0;
      } else {
        this.isl = 1;
      }

      this.$router.push({ query: { ...this.$route.query, isl: this.isl } });
      this.get_data(event);
    },
    toggle_bestbyath: function(event) {
      this.isBestByAthActive = !this.isBestByAthActive;
      if (this.isBestByAthActive === true) {
        this.bestbyath = 1;
      } else {
        this.bestbyath = 0;
      }

      this.$router.push({ query: { ...this.$route.query, b: this.bestbyath } });
      this.get_data(event);
    },
    year_change: function(event) {
      this.year = Number(event.target.id);
      //this.yearText = event.target.textContent

      this.$router.push({ query: { ...this.$route.query, y: this.year } });
      this.get_data(event);
    },
    age_change: function(event) {
      this.ageGroup = Number(event.target.id);

      this.ageStart = this.ageGroups[this.ageGroup].ageStart;
      this.ageEnd = this.ageGroups[this.ageGroup].ageEnd;

      this.$router.push({ query: { ...this.$route.query, a: this.ageGroup } });
      this.get_data(event);
    },
    event_change: function(event) {
      this.event_id = Number(event.target.id);
      this.event_type = Number(event.target.dataset.eventType);

      this.$router.push({
        query: { ...this.$route.query, t: this.event_type, e: this.event_id }
      });
      this.get_data(event);
    }
  }
};
</script>

<style scoped>
.dropdown-menu-long {
  max-height: 500px;
  overflow-y: auto;
  overflow-x: hidden;
}

.dropdown-submenu {
  position: relative;
}

.dropdown-submenu a::after {
  transform: rotate(-90deg);
  position: absolute;
  right: 6px;
  top: 0.8em;
}

.dropdown-submenu .dropdown-menu {
  top: 0;
  left: 100%;
  margin-left: 0.1rem;
  margin-right: 0.1rem;
}

.v-spinner {
  text-align: center;
}
</style>