export default {
  state: {
    counter: 0
  },
  getters: {
    counter: state => state.counter
  },
  mutations: {
    soma: function(state) {
      state.counter++
    }
  }
}