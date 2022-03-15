<!--
 * @Descripttion: the page for error report
 * @Author: Yongjing Qi
 * @Date: 2022-03-12 13:58:09
 * @LastEditTime: 2022-03-15 10:51:37
-->
<template>
    <div>
        <h1 class="Title">Error Report</h1>
        <el-divider></el-divider>
        <br>
        <div class="introduction">{{ generalIntroForErrorReport }}</div>
        <br><br><br><br><br>
        <div>
            <el-card :body-style="{ padding: '20px'}" el-card shadow="always">
            <br><br>
            <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 6}"
            placeholder="Please describe the error you have spotted"
            v-model="textarea">
            </el-input>
            <br><br><br>
            <div class="submitButton" align = "center">
                <span><el-button type="primary" plain style="width: 30%" icon="el-icon-search" @click="onSubmit"><span class="submit">Click To Submit</span></el-button></span>
            </div>
            </el-card>
            <br><br><br><br><br><br><br><br>
        </div>
    </div>
</template>

<script>
import {request} from '../../router/request'
  export default {
    data() {
      return {
        generalIntroForErrorReport: 'Using the form below you can report eny error you discovered in this web to our backend, changes will be conducted soon !',
        textarea: null
      }
    },
    methods: {
        onSubmit() {
            if (this.textarea != null) {
                // console.log('successfull error report')
                // console.log(this.textarea)
                var para = {error_message: this.textarea}
                var returnVal = request.postError(para)
                var returnValue = null
                returnVal.then((result) => {
                    returnValue = result.data
                    console.log(returnValue)
                    // this.processReturnValue(returnValue)
                    if (returnValue === 1) {
                        this.$router.push({ name: 'resultSuccess' })
                    } else if (returnValue === 0) {
                        this.$router.push({ name: 'resultFail' })
                    }
                })
                this.textarea = null
            }
        },
        processReturnValue() {

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
    font-size: 20px;
}
.introduction {
        margin-left: 60%;
        margin-right: 10%;
        float: right;
}
</style>
