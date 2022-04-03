<!--
 * @Descripttion: the the after successfully submitting error report
 * @Author: Yongjing Qi
 * @Date: 2022-03-12 14:58:50
 * @LastEditTime: 2022-03-15 10:51:33
-->
<template>
    <div>
        <br>
        <br><br><br><br>
        <el-result icon="success" title="Success" class = "title" subTitle="Please perform operations as prompted">
        <template slot="extra">
            <span><el-button type="primary" plain size="medium" @click="clickBackHome"><span class="search">Back To Home</span></el-button></span>
            <span><el-button type="primary" plain size="medium" @click="clickContinueReport"><span class="search">Continue to Report</span></el-button></span>
        </template>
        </el-result>
        <br><br><br><br>
        <br><br><br><br><br><br><br><br>
    </div>
</template>

<script>
// import {request} from '../../router/request'
  export default {
    data() {
      return {
      }
    },
    methods: {
      clickBackHome() {
        this.$router.push({ name: 'HelloWorld' })
      },
      clickContinueReport() {
        this.$router.push({ name: 'errorReport' })
      }
    }
  }
</script>
<style scoped>
.Title {
    margin-top: 0;
    margin-left: 30px;
    font-size: 50px;
    font-weight: bold;
    color: rgb(0, 0, 0);
  }
.grid-content {
    border-radius: 4px;
    min-height: 36px;
}
.bg-purple-white {
    background: #ffffff;
}
.searchTitle {
    font-weight: bolder;
    font-size: 20px;
}
.submitButton {
    margin-top: 20%;
    margin-top: 0%;
    width:100%;
}
.title {
    font-weight: bolder;
    font-size: 20px;
    color:#116996
}
.submit {
    font-weight: normal;
    font-size: 50px;
}
.introduction {
        margin-left: 60%;
        margin-right: 10%;
        float: right;
}
</style>
