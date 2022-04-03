/*
 * @Descripttion: the way of using axios to implement cross domain
 * and link front-end & back-end
 * @Author: Yongjing Qi
 * @Date: 2022-03-02 00:32:36
 * @LastEditTime: 2022-03-15 10:51:42
 */
import axios from "axios";

axios.defaults.baseURL = "/api";
axios.defaults.headers.post["Content-Type"] = "application/json;charset=UTF-8";
axios.defaults.headers["X-Requested-With"] = "XMLHttpRequest";
axios.defaults.headers["Cache-Control"] = "no-cache";
axios.defaults.headers["pragma"] = "no-cache";
 
let source = axios.CancelToken.source();
