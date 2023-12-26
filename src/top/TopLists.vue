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
                  >{{ eventText }}</a
                >
                <ul
                  v-on:click="event_change($event)"
                  class="dropdown-menu"
                  aria-labelledby="navbarDropdownMenuLink"
                >
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 1 }"
                      class="dropdown-item dropdown-toggle"
                      >Stökkgreinar</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_jump">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 2 }"
                      class="dropdown-item dropdown-toggle"
                      >Kastgreinar</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_throw">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 3 }"
                      class="dropdown-item dropdown-toggle"
                      >Spretthlaup</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_sprint">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 4 }"
                      class="dropdown-item dropdown-toggle"
                      >Grindarhlaup</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_hurdle">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 5 }"
                      class="dropdown-item dropdown-toggle"
                      >Millivegalengdir</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_middle">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 6 }"
                      class="dropdown-item dropdown-toggle"
                      >Langhlaup</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_long">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown-submenu">
                    <a
                      v-bind:class="{ active: event_type === 7 }"
                      class="dropdown-item dropdown-toggle"
                      >Þrautagreinar</a
                    >
                    <ul class="dropdown-menu">
                      <li v-for="i in events_athlon">
                        <a
                          v-bind:class="{ active: event_id === i.id }"
                          :id="i.id"
                          :data-event-type="i.type"
                          class="dropdown-item"
                          >{{ i.name }}</a
                        >
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <!-- Women = 2, Men = 1-->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  >{{ sexText }}</a
                >
                <div class="dropdown-menu" id="sexDropdown">
                  <a
                    v-on:click="toogle_sex($event, 2)"
                    class="dropdown-item"
                    id="1"
                    v-bind:class="{ active: gender === 2 }"
                    >Konur</a
                  >
                  <a
                    v-on:click="toogle_sex($event, 1)"
                    class="dropdown-item"
                    id="2"
                    v-bind:class="{ active: gender === 1 }"
                    >Karlar</a
                  >
                </div>
              </li>
              <!-- Dropdown for indoor, outdoor or both select-->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  >{{ inoutText }}</a
                >
                <div class="dropdown-menu" id="outinDropdown">
                  <a
                    v-on:click="toogle_innout($event, 1)"
                    class="dropdown-item"
                    id="1"
                    v-bind:class="{ active: outin === 1 }"
                    >Innanhúss</a
                  >
                  <a
                    v-on:click="toogle_innout($event, 2)"
                    class="dropdown-item"
                    id="2"
                    v-bind:class="{ active: outin === 2 }"
                    >Innan- og utanhúss</a
                  >
                  <a
                    v-on:click="toogle_innout($event, 0)"
                    class="dropdown-item"
                    id="0"
                    v-bind:class="{ active: outin === 0 }"
                    >Utanhúss</a
                  >
                </div>
              </li>
              <!---->
              <!--
                <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  >{{ yearText }}</a
                >
                <div
                  v-on:click="year_change($event)"
                  class="dropdown-menu dropdown-menu-long"
                  id="activeyearDropdown"
                >
                  <a
                    v-bind:class="{ active: year === 0 }"
                    class="dropdown-item"
                    id="0"
                    >Öll ár</a
                  >
                  <a
                    v-bind:class="{ active: year === i }"
                    v-for="i in year_list"
                    class="dropdown-item"
                    :id="i"
                    >{{ i }}</a
                  >
                </div>
              </li>
              -->
              <!---->
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  data-toggle="dropdown"
                  role="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  >{{ ageText }}</a
                >
                <div
                  v-on:click="age_change($event)"
                  class="dropdown-menu"
                  id="ageDropdown"
                >
                  <a
                    v-for="i in ageGroups"
                    v-bind:class="{ active: ageGroup === i.id }"
                    class="dropdown-item"
                    :id="i.id"
                    >{{ i.name }}</a
                  >
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
                  <label class="custom-control-label" for="customSwitch2"
                    >Birta bara besta afrek íþróttamanns</label
                  >
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
                  <label class="custom-control-label" for="customSwitch1"
                    >Birta ólöglegan árangur</label
                  >
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
                  <label class="custom-control-label" for="customSwitch3"
                    >Birta öll þjóðerni</label
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Outdoor = 0, Indoor = 1 -->
        <!-- <div class="row">
          <div class="col">
            <div class="row justify-content-center">
              <div class="col-md-4 col-sm-12 mb-3 text-center">
                <div class="btn-group btn-group-toggle" data-toggle="buttons">
                  <label
                    class="btn"
                    v-bind:class="{
                      'btn-primary': outin === 1,
                      'btn-secondary': outin !== 1,
                    }"
                  >
                    <input
                      v-on:click="toogle_innout($event, 1)"
                      type="radio"
                      name="options"
                      id="option1"
                      autocomplete="off"
                    />
                    Innanhúss
                  </label>
                  <label
                    class="btn"
                    v-bind:class="{
                      'btn-primary': outin === 2,
                      'btn-secondary': outin !== 2,
                    }"
                  >
                    <input
                      v-on:click="toogle_innout($event, 2)"
                      type="radio"
                      name="options"
                      id="option2"
                      autocomplete="off"
                    />
                    Innan- og utanhúss
                  </label>
                  <label
                    class="btn"
                    v-bind:class="{
                      'btn-primary': outin === 0,
                      'btn-secondary': outin !== 0,
                    }"
                  >
                    <input
                      v-on:click="toogle_innout($event, 0)"
                      type="radio"
                      name="options"
                      id="option3"
                      autocomplete="off"
                    />
                    Utanhúss
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>-->
        <!-- Datepickers -->
        <div class="row">
          <div class="col">
            <div class="row justify-content-center">
              <div class="col-md-auto col-sm-12 mb-3 text-center">
                <!--:shortcuts="shortcutsFromDate"-->
                    Dags. frá: 
                    <date-picker
                    v-model:value="fromDate"
                    v-bind:value="fromDate"
                    valueType="format"
                    @change="setFromDate"
                    :editable="false"
                    :clearable="false"
                    :shortcuts="shortcutsFromDate"
                    :disabled-date="disabledBefore1900AndAfterThisYear"
                    >
                  </date-picker>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="row justify-content-center">
              <div class="col-md-auto col-sm-12 mb-3 text-center">
                    Dags. til: 
                    <date-picker
                    v-model:value="toDate"
                    v-bind:value="toDate"
                    valueType="format"
                    @change="setToDate"
                    :editable="false"
                    :clearable="false"
                    :shortcuts="shortcutsToDate"
                    :disabled-date="disabledBefore1900AndAfterThisYear"
                    ></date-picker>
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
                  <th v-bind:class="{ 'd-none': !hasWind }" scope="col">Vindur</th>
                  <th scope="col">Nafn</th>
                  <th class="d-none d-sm-table-cell" scope="col">Aldur</th>
                  <th class="d-none d-sm-table-cell" scope="col">Félag</th>
                  <th class="d-none d-xl-table-cell" scope="col">Mót</th>
                  <th class="d-none d-md-table-cell" scope="col">Dags.</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(competitor, index) in data">
                  <th class="d-none d-sm-table-cell" scope="row">
                    {{ index + 1 }}
                  </th>
                  <td>{{ competitor.results }}</td>
                  <td v-bind:class="{ 'd-none': !hasWind }">
                    {{ competitor.wind }}
                  </td>
                  <td>
                    <router-link
                      :to="{
                        name: 'CompetitorProfile',
                        params: { competitorID: competitor.competitor_code },
                      }"
                    >
                      <a>{{ competitor.name }}</a>
                    </router-link>
                    <!--<a v-bind:href="'/keppandi/' + competitor.competitor_code">{{competitor.name}}</a>-->
                  </td>
                  <td class="d-none d-sm-table-cell">{{ competitor.age }}</td>
                  <td class="d-none d-sm-table-cell"><img
                      class="img-club"
                      v-bind:src="'/api/img/club/' + competitor.club.split('-')[0].split('/')[0]"
                      v-bind:alt="competitor.club"
                    />
                  </td>
                  <td class="d-none d-xl-table-cell">
                    <a
                      v-bind:href="
                        'http://mot.fri.is/MotFRI/SelectedCompetitionResults.aspx?Code=' +
                        competitor.competition_id
                      "
                      >{{ competitor.competition_name }}</a
                    >
                  </td>
                  <td class="d-none d-md-table-cell">{{ competitor.date }}</td>
                </tr>
              </tbody>
            </table>
            <pulse-loader
              :loading="loading"
              :color="color"
              :size="size"
            ></pulse-loader>
            <p align="center">{{ message }}</p>
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
import DatePicker from 'vue-datepicker-next';
import 'vue-datepicker-next/index.css';

export default {
  name: "TopLists",
  components: {
    PulseLoader,
    DatePicker,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",
      loading: false,
      time0: null,

      data: [],
      event: [],
      message: "",
      api_url_prefix: this.global_api_url_prefix,

      isBestByAthActive: true,
      isLegalActive: true,
      isISLActive: true,

      event_id: 143, // Event_id
      event_type: 1, //Jumps = 1, Throws = 2, Sprint = 3, Hurdles = 4, Middle = 5, Long = 6, -athlon = 7
      outin: 2, // Outdoor = 0, Indoor = 1
      gender: 2, // Women = 2, Men = 1
      year: new Date().getFullYear(), // Year
      fromDate: "2023-01-01",
      toDate: "2023-12-31",
      toMaxDate: "2023-12-31",
      year_list: [],
      ageGroup: 0,
      ageStart: 0, // Start age
      ageEnd: 999, // End age
      legal: 1, // Only legal = 1, all = 0
      isl: 0, // Icelandic = 0, Everybody = 1
      bestbyath: 1,

      shortcutsFromDate: [
        {
          text: 'Frá upphafi',
          onClick() {
            // Set date to 1900-01-01
            const date = new Date();
            date.setFullYear(1900);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: 'Ársbyrjun',
          onClick() {
            // Get Jan 1st of current year
            const date = new Date();
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
          {
          text: (new Date().getFullYear() - 1).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 1);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 2).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 2);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 3).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 3);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 4).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 4);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 5).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 5);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 6).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 6);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 7).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 7);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 8).toString(),
          onClick() {
            // From date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 8);
            date.setMonth(0);
            date.setDate(1);

            return date;
          },
        },
      ],

      shortcutsToDate: [
        {
          text: 'Í dag',
          onClick() {
            const date = new Date();
            // return a Date
            return date;
          },
        },
        {
          text: "Árslok",
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 0);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 1).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 1);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 2).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 2);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 3).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 3);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 4).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 4);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 5).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 5);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 6).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 6);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 7).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 7);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
        {
          text: (new Date().getFullYear() - 8).toString(),
          onClick() {
            // To date
            const date = new Date();
            date.setFullYear(date.getFullYear() - 8);
            date.setMonth(11);
            date.setDate(31);

            return date;
          },
        },
      ],

      events_jump: [
        { id: 143, type: 1, name: "Hástökk" },
        { id: 144, type: 1, name: "Hástökk án atrennu" },
        { id: 179, type: 1, name: "Langstökk" },
        { id: 180, type: 1, name: "Langstökk án atrennu" },
        { id: 239, type: 1, name: "Stangarstökk" },
        { id: 252, type: 1, name: "Þrístökk" },
        { id: 253, type: 1, name: "Þrístökk án atrennu" },
      ],
      events_throw: [
        { id: 152, type: 2, name: "Kringlukast (2,0 kg) [KA]" },
        { id: 159, type: 2, name: "Kringlukast (1,75kg) [P19]" },
        { id: 153, type: 2, name: "Kringlukast (1,5 kg) [P17]" },
        { id: 154, type: 2, name: "Kringlukast (1,0 kg) [KO, P15]" },
        { id: 156, type: 2, name: "Kringlukast (600 gr) [S15]" },
        { id: 162, type: 2, name: "Kúluvarp (7,26 kg) [KA]" },
        { id: 165, type: 2, name: "Kúluvarp (6,0 kg) [P19]" }, // Þessi grein er meðhöndluð sérstaklega í bakenda.
        { id: 172, type: 2, name: "Kúluvarp (5,0 kg) [P17]" }, // Þessi grein er meðhöndluð sérstaklega í bakenda.
        { id: 168, type: 2, name: "Kúluvarp (4,0 kg) [KO, P15]" },
        { id: 167, type: 2, name: "Kúluvarp (3,0 kg) [S15]" },
        { id: 163, type: 2, name: "Kúluvarp (2,0 kg) [S13]" },
        { id: 212, type: 2, name: "Sleggjukast (7,26 kg) [KA]" },
        { id: 214, type: 2, name: "Sleggjukast (6,0 kg) [P19]" },
        { id: 220, type: 2, name: "Sleggjukast (5,0 kg) [P15]" },
        { id: 216, type: 2, name: "Sleggjukast (4,0 kg) [KO]" },
        { id: 217, type: 2, name: "Sleggjukast (3,0 kg) [S17]" },
        { id: 213, type: 2, name: "Sleggjukast (2,0 kg)" },
        { id: 226, type: 2, name: "Spjótkast (800 gr) [KA]" },
        { id: 229, type: 2, name: "Spjótkast (700 gr) [P17]" },
        { id: 227, type: 2, name: "Spjótkast (600 gr) [KO, P15]" },
        { id: 233, type: 2, name: "Spjótkast (500 gr) [S17]" },
        { id: 230, type: 2, name: "Spjótkast (400 gr) [S15]" },
        { id: 188, type: 2, name: "Lóðkast (15,88 kg)"},
        { id: 181, type: 2, name: "Lóðkast (15,0 kg)"},
        { id: 183, type: 2, name: "Lóðkast (11,34 kg)"},
        { id: 186, type: 2, name: "Lóðkast (10,0 kg)"},
        { id: 182, type: 2, name: "Lóðkast (9,08 kg)"},
        //{ id: 193, type: 2, name: "Lóðkast (9,0 kg)"},
        { id: 191, type: 2, name: "Lóðkast (8,0 kg)"},
        { id: 184, type: 2, name: "Lóðkast (7,26 kg)"},
        { id: 185, type: 2, name: "Lóðkast (5,45 kg)"},
      ],
      events_sprint: [
        { id: 82, type: 3, name: "60 metra hlaup" },
        { id: 6, type: 3, name: "100 metra hlaup" },
        { id: 27, type: 3, name: "200 metra hlaup" },
        { id: 33, type: 3, name: "300 metra hlaup" },
        { id: 48, type: 3, name: "400 metra hlaup" },
        { id: 55, type: 3, name: "4x100 metra boðhlaup" },
        { id: 57, type: 3, name: "4x200 metra boðhlaup" },
        { id: 59, type: 3, name: "4x400 metra boðhlaup" },
        { id: 5, type: 3, name: "1000 metra boðhlaup" },
      ],
      events_hurdle: [
        { id: 11, type: 4, name: "100 metra gr. (91,4 cm)" },
        { id: 7, type: 4, name: "100 metra gr. (84 cm) [KO, S19, P15]" },
        { id: 8, type: 4, name: "100 metra gr. (76,2 cm) [S17]" },
        { id: 15, type: 4, name: "110 metra gr. (106,7 cm) [KA]" },
        { id: 16, type: 4, name: "110 metra gr. (99,1 cm) [P19]" },
        { id: 17, type: 4, name: "110 metra gr. (91,4 cm) [P17]" },
        { id: 39, type: 4, name: "300 metra gr. (76,2 cm) [P15, S15]" },
        { id: 49, type: 4, name: "400 metra gr. (91,4 cm) [KA, P19]" },
        { id: 50, type: 4, name: "400 metra gr. (84 cm) [P17]" },
        { id: 52, type: 4, name: "400 metra gr. (76,2 cm) [KO, S19, S17]" },
        { id: 99, type: 4, name: "80 metra grind (76,2 cm) [S15]" },
        { id: 83, type: 4, name: "60 metra grind (106,7cm) [KA]" },
        { id: 91, type: 4, name: "60 metra grind (99,1 cm) [P19]" },
        { id: 85, type: 4, name: "60 metra grind (91,4cm) [P17]" },
        { id: 86, type: 4, name: "60 metra grind (84,0 cm) [KO, S19, P15]" },
        { id: 89, type: 4, name: "60 metra grind (76,2 cm) [S17]" },
      ],
      events_middle: [
        { id: 81, type: 5, name: "600 metra hlaup" },
        { id: 97, type: 5, name: "800 metra hlaup" },
        { id: 4,  type: 5, name: "1000 metra hlaup"},
        { id: 19, type: 5, name: "1500 metra hlaup" },
        { id: 1 , type: 5, name: "1 míla"},
        { id: 30, type: 5, name: "3000 metra hlaup" },
        { id: 32, type: 5, name: "3000 metra hindrun" },
      ],
      events_long: [
        { id: 62, type: 6, name: "5000 metra hlaup" },
        { id: 79, type: 6, name: "5 km götuhlaup" },
        { id: 3, type: 6, name: "10.000 metra hlaup" },
        { id: 13, type: 6, name: "10 km götuhlaup" },
        { id: 12, type: 6, name: "10 km götuhlaup (flögutímar)" },
        { id: 141, type: 6, name: "Hálft maraþon" },
        { id: 142, type: 6, name: "Hálft maraþon (flögutímar)" },
        { id: 194, type: 6, name: "Maraþon" },
        { id: 195, type: 6, name: "Maraþon (flögutímar)" },
      ],
      events_athlon: [
        { id: 1001, type: 7, name: "Fimmtarþraut [KO]" },
        { id: 1002, type: 7, name: "Fimmtarþr. unglingastig" },
        { id: 1003, type: 7, name: "Fimmtarþraut (76 cm gr.)" },
        { id: 1004, type: 7, name: "Fimmtarþraut pilta 15 ára" },
        { id: 1011, type: 7, name: "Sjöþraut [KO, KA]" },
        { id: 1012, type: 7, name: "Sjöþraut (6 kg kúla)" },
        { id: 1013, type: 7, name: "Sjöþraut (5 kg kúla)" },
        { id: 1014, type: 7, name: "Sjöþraut meyjaáhöld" },
        { id: 1021, type: 7, name: "Tugþraut [KA]" },
        { id: 1022, type: 7, name: "Tugþraut 16-17 ára" },
        { id: 1023, type: 7, name: "Tugþraut U20 (Norðurlönd)" },
      ],
      ageGroups: [
        { id: 0, name: "Allir aldursflokkar", ageStart: 0, ageEnd: 999 },
        { id: 1, name: "20-22 ára", ageStart: 20, ageEnd: 22 },
        { id: 2, name: "18-19 ára", ageStart: 18, ageEnd: 19 },
        { id: 3, name: "16-17 ára", ageStart: 16, ageEnd: 17 },
        { id: 4, name: "15 ára", ageStart: 15, ageEnd: 15 },
        { id: 5, name: "14 ára", ageStart: 14, ageEnd: 14 },
        { id: 6, name: "13 ára", ageStart: 13, ageEnd: 13 },
        { id: 7, name: "12 ára", ageStart: 12, ageEnd: 12 },
        { id: 8, name: "30-34 ára", ageStart: 30, ageEnd: 34 },
        { id: 9, name: "35-39 ára", ageStart: 35, ageEnd: 39 },
        { id: 10, name: "40-44 ára", ageStart: 40, ageEnd: 44 },
        { id: 11, name: "45-49 ára", ageStart: 45, ageEnd: 49 },
        { id: 12, name: "50-54 ára", ageStart: 50, ageEnd: 54 },
        { id: 13, name: "55-59 ára", ageStart: 55, ageEnd: 59 },
        { id: 14, name: "60-64 ára", ageStart: 60, ageEnd: 64 },
        { id: 15, name: "65-69 ára", ageStart: 65, ageEnd: 69 },
        { id: 16, name: "70-74 ára", ageStart: 70, ageEnd: 74 },
        { id: 17, name: "75-79 ára", ageStart: 75, ageEnd: 79 },
        { id: 18, name: "80-84 ára", ageStart: 80, ageEnd: 84 },
        { id: 19, name: "85-89 ára", ageStart: 85, ageEnd: 89 },
        { id: 20, name: "90-94 ára", ageStart: 90, ageEnd: 94 },
        { id: 21, name: "95+ ára", ageStart: 95, ageEnd: 999 },
      ],
    };
  },
  //beforeDestroy() {
  //  document.title = 'Afrekaskrá FRÍ'
  //},
  mounted() {
    //let extScript = document.createElement('script')
    //extScript.setAttribute('src', 'static/extScript.js')
    //document.head.appendChild(extScript)

    var scriptTag = document.createElement("script"); // Can we ""Vue"" this script?
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
    testPar: function () {
      //return 'Hello'
      return this.$route.params.test;
    },
    yearMinusOne: function () {
      return (this.year - 1).toString();
    },
    ageText: function () {
      return this.ageGroups[this.ageGroup].name;
    },
    //yearText: function () {
    //  if (this.year === 0) {
    //    return "Öll ár";
    //  } else {
    //    return this.year.toString();
    //  }
    //},
    fromText: function () {
      return this.fromDate;
    },
    toText: function () {
      return this.toDate;
    },
    sexText: function () {
      if (this.gender === 1) {
        var sexText = "Karlar";
      } else {
        var sexText = "Konur";
      }

      return sexText;
    },
    inoutText: function () {
      if (this.outin == 1) {
        return "Innanhúss";
      } else if (this.outin == 0) {
        return "Utanhúss";
      } else {
        return "Innan- og utanhúss";
      }
    },
    eventText: function () {
      if (this.event_type === 1) {
        var index = this.events_jump.findIndex((p) => p.id == this.event_id);
        return this.events_jump[index].name;
      } else if (this.event_type === 2) {
        var index = this.events_throw.findIndex((p) => p.id == this.event_id);
        return this.events_throw[index].name;
      } else if (this.event_type === 3) {
        var index = this.events_sprint.findIndex((p) => p.id == this.event_id);
        return this.events_sprint[index].name;
      } else if (this.event_type === 4) {
        var index = this.events_hurdle.findIndex((p) => p.id == this.event_id);
        return this.events_hurdle[index].name;
      } else if (this.event_type === 5) {
        var index = this.events_middle.findIndex((p) => p.id == this.event_id);
        return this.events_middle[index].name;
      } else if (this.event_type === 6) {
        var index = this.events_long.findIndex((p) => p.id == this.event_id);
        return this.events_long[index].name;
      } else if (this.event_type === 7) {
        var index = this.events_athlon.findIndex((p) => p.id == this.event_id);
        return this.events_athlon[index].name;
      }
    },
    titleText: function () {
      var my_str =
        "Afrekaskrá FRÍ - " +
        this.eventText +
        " " +
        this.sexText +
        " " +
        this.inoutText;
      " í " + this.ageText;

      return my_str;
    },
    hasWind: function () {
      if (this.outin === 0 || this.outin === 2) {
        // We are outdoor. Does the current selected event have wind?
        if (this.event["HasWind"] === 1) {
          return true;
        } else {
          return false;
        }
      } else {
        return false; // We are indoor, no wind
      }
    },
  },
  created() {
    //var year_start = 1909;
    //var year_end = this.year;
    //this.year_list = [];

    this.fromDate = this.year + "-01-01";
    this.toDate = this.year + "-12-31";
    this.toMaxDate = this.year + "-12-31";
    
    //while (year_end + 1 > year_start) {
    //  this.year_list.push(year_end--);
    //}

    var parameters = this.$route.query;
    //if ("y" in parameters) {
    //  this.year = Number(this.$route.query.y);
    //}
    if ("f" in parameters) {
      this.fromDate = this.$route.query.f;
    }
    if ("t" in parameters) {
      this.toDate = this.$route.query.t;
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
    get_data: function (event) {
      // Check if fromDate is before toDate and set message if so
      var split_from = this.fromDate.split("-");
      var split_to = this.toDate.split("-");
      if (split_from[0] > split_to[0]) {
        this.message =
          "Frá-dagsetning getur ekki verið á eftir til-dagsetningu 😟";
          this.data = [];
        return;
      } else if (split_from[0] === split_to[0]) {
        if (split_from[1] > split_to[1]) {
          this.message =
            "Frá-dagsetning getur ekki verið á eftir til-dagsetningu 😟";
            this.data = [];
          return;
        } else if (split_from[1] === split_to[1]) {
          if (split_from[2] > split_to[2]) {
            this.message =
              "Frá-dagsetning getur ekki verið á eftir til-dagsetningu 😟";
              this.data = [];
            return;
          }
        }
      }

      this.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.data = [];

      let url =
        this.api_url_prefix +
        "/api/top_list/" +
        this.event_id +
        "/" +
        this.outin +
        "/" +
        this.gender +
        "/" +
        this.fromDate +
        "/" +
        this.toDate +
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
                this.sexText +
                " " +
                this.inoutText +
                " í " +
                this.ageText +
                " frá " +
                this.fromText +
                " til " +
                this.toText +
                " 😟";
            } else {
              this.message = "";
              //if (this.year !== 0) {
              //  this.data = this.cut_year(this.data);
              //}
              // Check if fromDate and toDate have the same year
              var split_from = this.fromDate.split("-");
              var split_to = this.toDate.split("-");
              if (split_from[0] === split_to[0]) {
                this.data = this.cut_year(this.data); // Cut year from date
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
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          document.title = "Afrekaskrá FRÍ";
        })
        .finally(() => {
          this.loading = false;
          document.title = this.titleText;
        });
    },
    cut_year: function (my_data) {
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
    add_inndoor_sign: function (my_data) {
      var dataLen = my_data.length;

      for (var i = 0; i < dataLen; i++) {
        if (my_data[i]["outdoor_indoor"] === 1) {
          my_data[i]["results"] = my_data[i]["results"] + " (i)";
        }
      }

      return my_data;
    },
    convert_to_timeformat: function (unit, my_data) {
      // Breyta tíma úr sek í mm:ss,dd eða hh:mm:ss,dd eftir því hvaða grein er valin.
      //0, # No units!
      //'metrar': 1, # Meters
      //'sek.': 2, # ss,dd
      //'mín.': 3, # mm:ss,dd
      //'klst.': 4, # hh:mm:ss,dd
      //'stig': 5, # Points
      //'Ungl.stig': 6 # Points junior
      // if (unit === 3 || unit === 4) {
      //   var dataLen = my_data.length;
      //   for (var i = 0; i < dataLen; i++) {
      //     var f = Number(my_data[i]["results"]);
      //     if (unit === 4) {
      //       // This unit has hours
      //       var h = Math.floor(f / 3600);
      //       f = f - h * 3600;
      //     } else {
      //       var h = 0;
      //     }
      //     var m = Math.floor(f / 60);
      //     var s = f - m * 60;
      //     var s_str;
      //     var m_str;
      //     var h_str;

      //     if (s < 10) {
      //       s_str = "0" + s.toFixed(2);
      //     } else {
      //       s_str = s.toFixed(2);
      //     }

      //     if (m < 10) {
      //       m_str = "0" + m.toFixed(0);
      //     } else {
      //       m_str = m.toFixed(0);
      //     }

      //     if (h < 10) {
      //       h_str = "0" + h.toFixed(0);
      //     } else {
      //       h_str = h.toFixed(0);
      //     }

      //     if (unit === 3) {
      //       my_data[i]["results"] = m_str + ":" + s_str;
      //     } else {
      //       my_data[i]["results"] = h_str + ":" + m_str + ":" + s_str;
      //     }
      //   }
      // }

      return my_data;
    },
    test: function (event) {
      alert(event.target.id);
      console.log("Hi");
    },
    setFromDate: function (value, type) {
      this.fromDate = value;
      this.$router.push({
        query: { ...this.$route.query, f: this.fromDate, t: this.toDate },
      });
      this.get_data(null);
    },
    setToDate: function (value, type) {
      this.toDate = value;
      this.$router.push({
        query: { ...this.$route.query, f: this.fromDate, t: this.toDate },
      });
      this.get_data(null);
    },
    disabledBefore1900AndAfterThisYear: function (date) {
      const year = date.getFullYear();
      const thisYear = new Date().getFullYear();
      return year < 1900 || year > thisYear;
    },
    //Outdoor = 0, Indoor = 1
    //Women = 2, Men = 1 -->
    outinsex_change: function (event, outin, gender) {
      this.outin = outin;
      this.gender = gender;

      this.$router.push({
        query: { ...this.$route.query, g: gender, i: outin },
      });
      this.get_data(event);
    },
    toogle_sex: function (event, gender) {
      this.gender = gender;

      this.$router.push({ query: { ...this.$route.query, g: gender } });
      this.get_data(event);
    },
    toogle_innout(event, outin) {
      this.outin = outin;

      this.$router.push({ query: { ...this.$route.query, i: outin } });
      this.get_data(event);
    },
    toggle_legalresults: function (event) {
      this.isLegalActive = !this.isLegalActive;
      if (this.isLegalActive === true) {
        this.legal = 1;
      } else {
        this.legal = 0;
      }

      this.$router.push({ query: { ...this.$route.query, l: this.legal } });
      this.get_data(event);
    },
    toggle_isl: function (event, isl) {
      this.isISLActive = !this.isISLActive;
      if (this.isISLActive === true) {
        this.isl = 0;
      } else {
        this.isl = 1;
      }

      this.$router.push({ query: { ...this.$route.query, isl: this.isl } });
      this.get_data(event);
    },
    toggle_bestbyath: function (event) {
      this.isBestByAthActive = !this.isBestByAthActive;
      if (this.isBestByAthActive === true) {
        this.bestbyath = 1;
      } else {
        this.bestbyath = 0;
      }

      this.$router.push({ query: { ...this.$route.query, b: this.bestbyath } });
      this.get_data(event);
    },
    //year_change: function (event) {
    //  this.year = Number(event.target.id);
    //  //this.yearText = event.target.textContent

    //  this.$router.push({ query: { ...this.$route.query, y: this.year } });
    //  this.get_data(event);
    //},
    age_change: function (event) {
      this.ageGroup = Number(event.target.id);

      this.ageStart = this.ageGroups[this.ageGroup].ageStart;
      this.ageEnd = this.ageGroups[this.ageGroup].ageEnd;

      this.$router.push({ query: { ...this.$route.query, a: this.ageGroup } });
      this.get_data(event);
    },
    event_change: function (event) {
      this.event_id = Number(event.target.id);
      this.event_type = Number(event.target.dataset.eventType);

      this.$router.push({
        query: { ...this.$route.query, t: this.event_type, e: this.event_id },
      });
      this.get_data(event);
    },
  },
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

/* center spinner */
.v-spinner {
  text-align: center;
}

.img-club {
  height: 25px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>