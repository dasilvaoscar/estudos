<template> 
  <div class="menu-game">
    <b-navbar toggleable="lg" type="dark">
      <b-button @click="attackMonster()" class="btn-game" variant="danger">Attack</b-button>
      <b-button @click="superSpecial()" class="btn-game" variant="info">Super</b-button>
      <b-button @click="healHunter()" class="btn-game" variant="success">Heal</b-button>
      <b-button @click="playerSurrender()" class="btn-game" variant="dark">Surrender</b-button>
    </b-navbar>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
  
  methods: {
    attackMonster: function () {
      this.$store.commit('damageOnMonster', 7)
      this.$store.commit('damageOnPlayer', 15)
      this.$store.commit('setStage', {
        healOnPlayer: 0,
        damageOnMonster: 7,
        damageOnPlayer: 15,
      })
    },

    superSpecial: function () {
      this.$store.commit('damageOnMonster', 20)
      this.$store.commit('damageOnPlayer', 12)
      this.$store.commit('setStage', {
        healOnPlayer: 0,
        damageOnMonster: 20,
        damageOnPlayer: 12
      })
    },

    healHunter: function () {
      this.$store.commit('healOnPlayer', 10)
      this.$store.commit('damageOnPlayer', 5)
      this.$store.commit('setStage', {
        healOnPlayer: 10,
        damageOnMonster: 0,
        damageOnPlayer: 5,
      })
    },

    playerSurrender: function() {
      this.$store.commit('damageOnPlayer', this.$store.getters.playerLife)
    }
  }
})

export default class Menu extends Vue {}
</script>
<style>
  .menu-game {
    width: 100%;
    margin: 5% auto auto auto;
    display: block;
  }

  .btn-game {
    width: 100%;
    padding: 2%;
    margin: .5%;
  }
</style>