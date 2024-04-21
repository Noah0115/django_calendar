import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Welcome from '../components/Welcome.vue'
import Even from '../components/Even.vue'
import Users from '../components/Users.vue'

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {
      path: '/', redirect: '/login'
    },
    {
      path: '/login', component: Login
    },
    {
      path: '/home',
      component: Home,
      redirect: '/welcome',
      children: [
        { path: '/welcome', component: Welcome},
        { path: '/user', component: Users },
        { path: '/even', component: Even },
      ]
    }
  ]
})
export default router
