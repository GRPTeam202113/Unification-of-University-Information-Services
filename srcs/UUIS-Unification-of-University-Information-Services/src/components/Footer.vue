<!--
 * @Descripttion: This is the footer component for this web system,
 * it will be shown on each web page, it is designed based on
 * the footer of UNNC official website, useful links are listed here
 * @Author: Yongjing Qi
 * @Date: 2022-02-18 15:18:03
 * @LastEditTime: 2022-03-15 10:48:26
-->
<template>
    <el-container>
        <div class="Footer">
            <div class="title">Address</div>
            <div class="mainBodyAddress" style="italic">199 Taikang East Road Ningbo, 315100, China</div>
            <div class = "mainBody">T. +86 (0)574 8818 0000</div>
            <div class = "mainBody">F. +86 (0)574 8818 9372</div>
        </div>
        <div class="Footer">
            <div class="title">Legal</div>
            <div class = "mainBody"><a href="https://www.nottingham.edu.cn/en/usage/copyright.aspx">Copyright</a></div>
            <div class = "mainBody"><a href="https://www.nottingham.edu.cn/en/usage/privacy.aspx">Privacy policy</a></div>
            <div class = "mainBody"><a href="https://www.nottingham.edu.cn/en/usage/website-terms-of-use.aspx">Terms and conditions</a></div>
        </div>
        <div class="Footer">
            <div class="title">Essentials</div>
            <div class = "mainBody"><a href="https://moodle.nottingham.ac.uk/login/index.php">Moodle</a></div>
            <div class = "mainBody"><a href="https://nusearch.nottingham.edu.cn">NUsearch</a></div>
            <div class = "mainBody"><a href="https://bluecastle-cn.nottingham.ac.uk/">Blue Castle</a></div>
            <div class = "mainBody"><a href="http://email.nottingham.edu.cn/">Email</a></div>
            <div class = "mainBody"><a href="https://hub.nottingham.ac.uk/">MyNottinghamHub</a></div>
            <div class = "mainBody"><router-link :to="{name:'errorReport'}">Error Report</router-link></div>
        </div>
        <div class="Footer">
            <div class="title">Social Media</div>
            <div class = "mainBody">
                <div class="wrapper">
                    <div><el-link :underline="false" href="https://www.facebook.com/unnchome"><img src="../assets/SocialMedia/FaceBook.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://twitter.com/UNNCHome"><img src="../assets/SocialMedia/Twitter.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://www.youtube.com/channel/UCFAen0Ip6FEUTTYG2biAXiw"><img src="../assets/SocialMedia/Youtube.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://www.linkedin.com/school/university-of-nottingham-ningbo-china/"><img src="../assets/SocialMedia/Linkedin.png" width="30" height="30"></el-link></div>
                </div>
                <div class="wrapper">
                    <div><el-link :underline="false" href="https://www.linkedin.com/school/university-of-nottingham-ningbo-china/"><img src="../assets/SocialMedia/Instagram.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://weibo.com/unncweibo"><img src="../assets/SocialMedia/Weibo.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://www.nottingham.edu.cn/en/utilities/qrcodes/official-public-wechat-account.aspx"><img src="../assets/SocialMedia/Wechat.png" width="30" height="30"></el-link></div>
                    <div><el-link :underline="false" href="https://vk.com/uonningbochina"><img src="../assets/SocialMedia/vk.png" width="30" height="30"></el-link></div>
                </div>
            </div>
        </div>
    </el-container>
    <!-- element UI -->
</template>

<script>
    export default {
        name: 'pagefooter',
        data() {
            return {
            }
        }
    }
</script>

<style scoped>
.backGround{
    margin: 0;
    padding: 40px;
    width:100%;
    background-color:rgb(0, 0, 0);
}
.backGround div{
    display:inline-block;
}
.Footer{
    padding-left:60px;
    padding-bottom: 50px;
    padding-top: 50px;
    margin:0;
    width:100%;
    background-color: black;
    color:white;
    font-size:0;
}
.title{
    text-align: left;
    line-height:6;
    font-size: 16px;
    font-weight: bold;
}
.mainBody {
    text-align: left;
    line-height:2;
    font-size: 13px;;
}
.mainBodyAddress {
    text-align: left;
    line-height:5;
    font-size: 13px;
    font-style: italic;
}
.nav-left {
    float: left;
    margin:0;
    padding:0;
}
.nav-right{
    float: right;
}
.logoWord {
    position:absolute;
    left: 100px;
}
.wrapper div{
    display:inline-block;
    margin:2px;
}
a {
    text-decoration:none;
    color:white;
}
</style>
