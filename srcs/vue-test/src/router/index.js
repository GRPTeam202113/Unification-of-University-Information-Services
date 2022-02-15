import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import cele from '@/components/Faculty/CELEPage'
import fose from '@/components/Faculty/FoSEPage'
import fob from '@/components/Faculty/FoBPage'
import fhss from '@/components/Faculty/FHSSPage'
import course from '@/components/Course'
import module from '@/components/Module'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
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
    path: '/Course',
    component: course
  },
  {
    path:'/Module',
    component: module
  }
]

var router = new VueRouter({
  routes
})

export default router
