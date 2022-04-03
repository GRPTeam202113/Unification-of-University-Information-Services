/*
 * @Descripttion: This is the main method for linking with
 * backend with post/get, using axios
 * @Author: Yongjing Qi
 * @Date: 2022-03-06 22:35:21
 * @LastEditTime: 2022-04-03 14:15:33
 */

import axios from 'axios'
var request = {
    // var returnValue
    post(para) {
        // var returnValue = null
        // console.log('hhh' + para.facultyname)
        var returnVal = new Promise((resolve, reject) => {
            axios.post('/api/faculty/course/module', para).then(data => { resolve(data) })
        })
        return returnVal
    },
    postError(errorMessage) {
        var returnVal = new Promise((resolve, reject) => {
            axios.post('/api/ErrorReport', errorMessage).then(data => { resolve(data) })
        })
        return returnVal
    },
    postCourseName(para) {
        var returnVal = new Promise((resolve, reject) => {
            axios.post('/api/faculty/course', para).then(data => { resolve(data) })
        })
        return returnVal
    }
}
export {
    request
}
