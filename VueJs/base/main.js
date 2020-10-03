var app = new Vue({
    el: "#app",
    data: {
        title: "Hallow World",
        ipsun: `Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.`
    }
})

var app2 = new Vue({
    el: "#app-2",
    data: {
        message: 'Você carregou essa página as ' + new Date().toLocaleString()
    }
})

var app3 = new Vue({
    el:"#app-3",
    data: {
        seen: true
    },
    methods: { 
        see: function () {
                if(this.seen == true) this.seen = false
                else this.seen = true
            }
    },
})

var app4 = new Vue({
    el: "#app-4",
    data: {
        todos: [
            { text: 'Learn JavaScript' },
            { text: 'Learn Vue' },
            { text: 'Build something awesome' }
        ]
    }
})

var app6 = new Vue({
    el: "#app-6",
    data: {
        message: "Teste"
    }
})