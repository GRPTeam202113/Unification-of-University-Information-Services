<!--
 * @Descripttion: This page combinies the header, footer and the main body decided by the rooter
 * @Author: Yongjing Qi
 * @Date: 2022-02-23 15:38:27
 * @LastEditTime: 2022-03-15 10:51:56
-->

<template>
  <div id="app">
    <pageheader></pageheader>
    <router-view/>
    <pagefooter></pagefooter>
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer.vue'
export default {
  name: 'App',
  components: {
    'pageheader': Header,
    'pagefooter': Footer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
