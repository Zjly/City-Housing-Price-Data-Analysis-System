import Vue from 'vue'
import App from './App.vue'
import router from './router'
// ui框架
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
// 数据请求
import axios from 'axios';
import vueAxios from 'vue-axios';
Vue.use(vueAxios, axios)

Vue.config.productionTip = false

new Vue({
  
  router,
  render: h => h(App)
}).$mount('#app')