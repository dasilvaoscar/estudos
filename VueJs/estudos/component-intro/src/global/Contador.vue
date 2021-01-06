<template>
  <div id="app">
    <h1>Contador</h1>
    <span>{{ contador }}</span>
    <button @click="add()">+</button>
    <button @click="remove()"> - </button>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      contador: 0
    }
  },

  methods: {
    add: function () {
      this.contador++
    },

    remove: function () {
      this.contador--
    }
  }
}
</script>

<style>

</style>