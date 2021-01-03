<template>
  <div class="life">
    <h2>Fucking Nemesis</h2>
    <b-progress :value="getMonsterLife()" variant="danger" striped :animated="animate"></b-progress>
    <div class="nemesis">
      <img src="../assets/nemesis.png">
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
  data: () => {
    return {
      animate: true
    }
  },

  methods: {
    getMonsterLife: function() {
      return this.$store.getters.monsterLife
    }
  },
})

export default class Monster extends Vue {}
</script>
<style>
  .nemesis {
    text-align: center;
  }

  .nemesis img {
    margin: 5% auto auto auto;
    width: 100%;
  }
</style>