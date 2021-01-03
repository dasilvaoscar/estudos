<template>
  <div class="container">
    <Menu />
    <div id="game">
      <Player />
      <Monster />
    </div>
    <hr/>
    <Logs />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Menu from './components/Menu.vue'
import Monster from './components/Monster.vue'
import Player from './components/Player.vue'
import Logs from './components/Logs.vue'

@Component({
  components: {
    Menu,
    Monster,
    Player,
    Logs,
  },
})

export default class App extends Vue {}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  #game {
    display: flex
  }

  .life {
    width: 40%;
    margin: 10% auto 5% auto;
  }
</style>
