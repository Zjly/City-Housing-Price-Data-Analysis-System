// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// ???????????? axios
import axios from './http'
// ?? moment.js ????? UTC ???????
import moment from 'moment'
// Import Bootstrap css and js files
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
// ??? css ??
import './assets/core.css'
import './assets/custom.css'
// ??
import './assets/icon-line/css/simple-line-icons.css'
import './assets/icon-material/material-icons.css'
// register the vue-toasted plugin on vue
import VueToasted  from 'vue-toasted'

Vue.use(VueToasted, {
  // ???? primary/outline/bubble
  theme: 'bubble',
  // ?????????
  position: 'top-center',
  // ??????????
  duration: 3000,
  // ????????
  iconPack : 'material', // set your iconPack, defaults to material. material|fontawesome|custom-class
  // ????????
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  },
});

Vue.config.productionTip = false

// ? $axios ??? prototype ???????????? this.$axios ??
Vue.prototype.$axios = axios
// ? $moment ??? prototype ???????????? this.$moment ??
Vue.prototype.$moment = moment

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})