<!--
 * @Descripttion: In this file, the front-end determines and loads components
 * based on dynamic routes (using the parameters passes via the routes to dynamically
 * load .vue for each module)
 * @Author: Yongjing Qi
 * @Date: 2022-03-14 19:06:51
 * @LastEditTime: 2022-03-15 10:48:46
-->
<template>
  <div v-if="flag">
    <async-example />
  </div>
</template>
<script>
import Vue from 'vue';
export default {
  created() {
    this.initComponent();
  },
  data() {
    return {
      flag: false
    };
  },
  methods: {
    initComponent() {
      // console.log('hhh' + this.$route.params.ModuleCode)
      const path = './' + this.$route.params.ModuleCode;
      Vue.component('async-example', function(resolve) {
        require([`${path}`], resolve);
      });
      this.flag = true;
    }
  }
};
</script>
