/*
 * @Descripttion: This is the engine page to generate the whole web system
 * @Author: Yongjing Qi
 * @Date: 2022-02-23 15:38:27
 * @LastEditTime: 2022-03-15 10:47:15
 */

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueAxios from 'vue-axios'
import axios from 'axios'
import router from './router'

Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(VueAxios, axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
