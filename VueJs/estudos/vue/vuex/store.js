const store = new Vuex.Store({
  state: {
    user: {
        userName: 'oscar.silva',
        firstName: 'Oscar',
        lastName: 'da Silva',
        logged: false,
        anonymous: false,
    },

    users: []
  },

  getters: {
    userName: state => state.user.userName,
    firstName: state => state.user.firstName,
    lastName: state => state.user.lastName,
    logged: state => state.user.logged,
    anonymous: state => state.user.anonymous,
    user: state => state.user,
    users: state => state.users
  },

  mutations: {
    setLogged: function(state, boolean) {
      state.user.logged = boolean;
    },

    setAnonymous: function(state, boolean) {
      state.user.anonymous = boolean;
    },

    setUsers: function(state, user) {
      state.users.push(user);
    },
  },
})

