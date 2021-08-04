import { INCREMENT } from './mutation.types.js'

export default {
  namespaced: true,
  state: {
      count: 0
  },
  mutations: {
    [INCREMENT](state) {
      state.count++
    }
  },
  actions: {
  },
}
  