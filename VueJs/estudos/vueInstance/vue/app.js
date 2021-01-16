const app = new Vue({
    store: store, 

    async created() {
        this.$data.new = await axios.get('https://api.covid19api.com/') /* Dont Work */
    }, 
    
    methods: {
        /* Getters */
        getUsers: function() {
            return this.$store.getters.users
        },
        
        getUserName: function() {
            return this.$store.getters.userName
        },

        getFirstName: function() {
            return this.$store.getters.firstName
        },

        getLastName: function() {
            return this.$store.getters.lastName
        },

        getFullName: function() {
            return `${this.getFirstName()} ${this.getLastName()}`;
        },

        getLogged: function() {
            return this.$store.getters.logged;
        },

        getAnonymous: function() {
            return this.$store.getters.anonymous;
        },

        /* Setters */
        changeLogged: function() {
            this.$store.commit('setLogged', this.getLogged() == true ? false:true);
        }, 

        changeAnonymous: function() {
            this.$store.commit('setAnonymous', this.getAnonymous() == true ? false:true);
        },
        
        /* Rules */
        isAnonymous: function() {
            return this.getAnonymous() == true ? true:false;
        },

        isLogged: function() {
            return this.getLogged() == true ? true:false;
        },

        isAuthorized: function() {
            return this.isAnonymous() || this.isLogged() == true ? true:false
        }
    },

    mounted: function() {
        const payload = {
            name: this.getUserName(),
            firstName: this.getFirstName(),
            lastName: this.getLastName(),
        }
        
        for(let i = 1; i<=15; i++) {
            this.$store.commit('setUsers', payload)
        }
    },
})

Vue.component('comp', {
    template: `<h1 style="text-align:center">Estudando | <code>VueJS</code></h1>`
})

app.$mount('#app')


