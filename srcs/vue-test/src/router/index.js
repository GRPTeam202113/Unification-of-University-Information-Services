/*
 * @Descripttion: This is the rooter setting of the web system
 * @Author: Yongjing Qi
 * @Date: 2022-03-01 23:36:00
 * @LastEditTime: 2022-03-15 10:46:40
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import cele from '@/components/Faculty/CELEPage'
import fose from '@/components/Faculty/FoSEPage'
import fob from '@/components/Faculty/FoBPage'
import fhss from '@/components/Faculty/FHSSPage'
import module from '@/components/Modules/Module'
import course from '@/components/Course'
import search from '@/components/Search'
import errorReport from '@/components/ErrorReport/ErrorReport'
import resultSuccess from '@/components/ErrorReport/ResultSuccess'
import resultFail from '@/components/ErrorReport/ResultFail'
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
    name: 'cele',
    component: cele
  },
  {
    path: '/FoSE',
    name: 'fose',
    component: fose
  },
  {
    path: '/FoB',
    name: 'fob',
    component: fob
  },
  {
    path: '/FHSS',
    name: 'fhss',
    component: fhss
  },
  {
    path: '/Module/:ModuleCode',
    // name: 'ModuleCode',
    // props: true,
    name: 'module',
    // props: route => ({query: route.query.ModuleCode}),
    component: module
  },
  {
    path: '/Course/:Faculty/:CourseName',
    name: 'course',
    component: course
  },
  {
    path: '/Search',
    name: 'search',
    component: search
  },
  {
    path: '/ErrorReport',
    name: 'errorReport',
    component: errorReport
  },
  {
    path: '/ErrorReport/ResultSuccess',
    name: 'resultSuccess',
    component: resultSuccess
  },
  {
    path: '/ErrorReport/ResultFail',
    name: 'resultFail',
    component: resultFail
  }
]
var router = new VueRouter({
  routes
})

export default router
