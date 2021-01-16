<template>
  <div id="app">
    {{counter}}

    <button class="btn" @click="soma()">
            ADD <span class="badge badge-primary"></span>
    </button>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'App',
  computed:{
    ...mapGetters({
      counter: 'counter'
    }),
  }, 
  methods: {
    ...mapMutations(['soma'])
  }
  

}
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
</style>
