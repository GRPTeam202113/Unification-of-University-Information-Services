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
