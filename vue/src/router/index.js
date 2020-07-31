import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import House from '../views/House.vue'
import Login from '../views/Login.vue'
import News from '../views/News.vue'
import Register from '../views/Register.vue'
import Forecast from '../views/Forecast.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/house',
    name: 'House',
    component: House
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/forecast',
    name: 'Forecast',
    component: Forecast
  }

]

const router = new VueRouter({
  routes
})

export default router
