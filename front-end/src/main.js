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
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
// ????
import './assets/icon-line/css/simple-line-icons.css'
import './assets/icon-material/material-icons.css'
// bootstrap-markdown ????????
import './assets/bootstrap-markdown/css/bootstrap-markdown.min.css'
import './assets/bootstrap-markdown/css/custom.css'
import './assets/icon-awesome/css/font-awesome.min.css'  // ???????????? font-awesome ????
// markdown ??
import './assets/markdown-styles/github-markdown.css'
// ??? css ??
import './assets/core.css'
import './assets/custom.css'

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

// register the vue-sweetalert2 plugin on vue
import VueSweetalert2 from 'vue-sweetalert2'
Vue.use(VueSweetalert2)


// ?? highlight.js ????? vue-router ? Home ???? Post ???????????????
// ???????????????? v-highlight
import hljs from 'highlight.js'
// ????????default, atelier-dune-light  ???atom-one-dark, atom-one-dark-reasonable, monokai
import 'highlight.js/styles/atom-one-dark-reasonable.css'
Vue.directive('highlight',function (el) {
  let blocks = el.querySelectorAll('pre code');
  blocks.forEach((block)=>{
    hljs.highlightBlock(block)
  })
})


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