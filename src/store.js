// store.js
import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userRole: '' // 用户角色
  },
  mutations: {
    setUserRole(state, role) {
      state.userRole = role;
      /* localStorage.setItem('userRole', role); */
    }
  },
  plugins: [
    createPersistedState({
      key: 'your-app-storage-key' // 设置一个存储键名
    })
  ]
});
