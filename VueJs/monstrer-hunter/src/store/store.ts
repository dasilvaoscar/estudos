import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    monsterLife: 100,
    playerLife: 100,
    stage: [{
      healOnPlayer: 0,
      damageOnMonster: 0,
      damageOnPlayer: 0,
    }],
  },

  mutations: {
    setStage: function (state, stage) {
      state.stage.push(stage)
    },

    damageOnMonster: function (state, damage) {
      state.monsterLife -= damage
    },

    healOnPlayer: function (state: { playerLife: number }, heal: number) {
      state.playerLife += heal
    },

    damageOnPlayer: function (state: { playerLife: number }, damage: number) {
      state.playerLife -= damage
    },
  },

  getters: {
    monsterLife: state => state.monsterLife,
    playerLife: state => state.playerLife,
    stage: state => state.stage,
  }
})
