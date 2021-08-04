<template>
  <div id="app">
    <h1>{{ state.count }}</h1>
    <h1>{{ $store.state.count }}</h1>
    <h1>{{ count }}</h1>
    <button @click="incrementNumber()">Add</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import { INCREMENT } from '@/store/mutation.types.js'

export default {
  name: 'App',
  methods: {
    ...mapMutations({ incrementNumber: INCREMENT })
  },
  computed: mapState({
    count: 'count'
  }),
  data() {
    return {
      state: this.$store.state
    }
  },
}
</script>