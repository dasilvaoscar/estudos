var app = new Vue({
    el: '#app',
    data: {
        message: 'Aprendendo VueJs'
    }
})

var app2 = new Vue({
    el: '#app02',
    data: {
      message: 'Você carregou esta página em ' + new Date().toLocaleString()
    }
  })