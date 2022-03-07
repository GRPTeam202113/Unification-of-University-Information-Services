import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import cele from '@/components/Faculty/CELEPage'
import fose from '@/components/Faculty/FoSEPage'
import fob from '@/components/Faculty/FoBPage'
import fhss from '@/components/Faculty/FHSSPage'
import module from '@/components/Module'
import course from '@/components/Course'
import search from '@/components/Search'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Ping from '../components/Ping';

Vue.use(ElementUI)
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/ping',
    component: Ping
  },
  {
    path: '/CELE',
    component: cele
  },
  {
    path: '/FoSE',
    component: fose
  },
  {
    path: '/FoB',
    component: fob
  },
  {
    path: '/FHSS',
    component: fhss
  },
  {
    path: '/Module',
    component: module
  },
  {
    path: '/Course',
    component: course
  },
  {
    path: '/Search',
    component: search
  }
]

var router = new VueRouter({
  routes
})

export default router
