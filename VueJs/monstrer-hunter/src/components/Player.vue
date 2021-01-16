<template>
  <div class="life">
    <h2>Geraldão</h2>
    <b-progress :value="getPlayerLife()" variant="success" striped :animated="animate"></b-progress>
    <div class="geralt">
      <img src="../assets/geralt.png">
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
    getPlayerLife: function() {
      return this.$store.getters.playerLife
    }
  },
})

export default class Player extends Vue {}
</script>
<style>
  .geralt {
    text-align: center
  }

  .geralt img {
    margin: 5% auto auto auto;
    width: 40%;
    height: 100%;
  }
</style>