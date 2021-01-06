import Vue from 'vue'
import App from './App.vue'
import Counter from './global/Contador'

Vue.config.productionTip = false
Vue.component('app-counter', Counter) /* Registando componente de forma GLOBAL */

new Vue({
  render: h => h(App),
}).$mount('#app')
