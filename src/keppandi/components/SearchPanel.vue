<template>
  <div>
    <div class="row mb-4">
      <div class="col-md-12 text-center">
        <a
          v-for="letter in alphabet"
          :key="letter"
          class="btn btn-sm"
          :class="{'btn-outline-secondary': startsWith === letter}"
          @click="toggleLetter(letter)"
        >
          {{ letter }}
        </a>
      </div>
    </div>
    <div class="form-row mb-4">
      <div class="col-md-6 col-lg-6 mb-6">
        <input
          :value="search"
          type="text"
          class="form-control text-center"
          placeholder="Leita"
          @input="searchInput"
        >
      </div>
      <!-- <div class="col-md-6 col-lg-3 mb-3">
        <select
          :value="regionId"
          class="form-control"
          @change="changeRegion"
        >
          <option
            selected="selected"
            :value="undefined"
          >
            Íþróttahérað
          </option>
          <option
            v-for="region in regions"
            :key="region.id"
            :value="region.id"
          >
            {{ region.fullName }}
          </option>
        </select>
      </div> -->
      <div class="col-md-4 col-lg-4 mb-4">
        <select
          :value="clubId"
          class="form-control"
          @change="changeClub"
        >
          <option
            selected="selected"
            :value="undefined"
          >
            Félag
          </option>
          <option
            v-for="club in clubs"
            :key="club.id"
            :value="club.thorId"
          >
            {{ club.fullName }}
          </option>
        </select>
      </div>
      <!-- <div class="col-md-4 col-lg-2 mb-3">
        <select
          :value="legacyClub"
          class="form-control"
          @change="changeLegacy"
        >
          <option
            selected="selected"
            :value="undefined"
          >
            Gömul skráning
          </option>
          <option
            v-for="club in legacy"
            :key="club"
            :value="club"
          >
            {{ club }}
          </option>
        </select>
      </div> -->
      <div class="col-md-4 col-lg-1 mb-4">
        <button
          type="button"
          class="btn btn-secondary btn-block"
          @click.prevent="clear"
        >
          Hreinsa
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import debounce from 'lodash.debounce'

export default {
  name: 'AthleteSearchPanel',
  props: {
    clubs: {
      type: Array,
      default: () => []
    },
    settings: {
      type: Object,
      default: () => {}
    }
  },
  data () {
    return {
      startsWith: this.settings.startsWith,
      search: this.settings.search,
      clubId: this.settings.clubId,
      alphabet: ['A', 'Á', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'X', 'Y', 'Ý', 'Z', 'Þ', 'Æ', 'Ö']
    }
  },
  computed: {
    selected () {
      return {
        startsWith: this.startsWith,
        search: this.search,
        clubId: this.clubId,
      }
    },
  },
  methods: {
    clear () {
      this.startsWith = undefined
      this.search = undefined
      this.clubId = undefined
      this.$emit('change', this.selected)
    },
    toggleLetter (letter) {
      if (this.startsWith === letter) {
        this.startsWith = undefined
      } else {
        this.startsWith = letter
        this.search = undefined
      }
      this.$emit('change', this.selected)
    },
    searchInput: debounce(function (e) {
      this.startsWith = undefined
      this.search = e.target && e.target.value

      // To clear box
      if (this.search.length === 0) {
        this.$emit('change', this.selected)
      }

      // Only search on 3
      if (this.search.length >= 3) {
        this.$emit('change', this.selected)
      }
    }, 300),
    changeRegion (e) {
      this.clubId = undefined
      this.$emit('change', this.selected)
    },
    changeClub (e) {
      this.clubId = e.target.value
      this.$emit('change', this.selected)
    }
  }
}
</script>
<style scoped>
a.btn {
  cursor: pointer;
}
a.btn:hover {
  border-color: #6c757d
}

a.btn-outline-secondary:hover {
  color: #fff
}
</style>
