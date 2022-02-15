<template>
    <!-- element UI -->
    <el-container>
        <el-header height = '80px' >
            <div class = "navBarWrap">
                <div class = "nav-left">
                    <el-link :underline="false" href="https://www.nottingham.edu.cn/en/index.aspx"><img src="../assets/unnc.png" width="70" height="70"></el-link>
                </div>
                <div class = "nav-left">
                    <img src="../assets/headerBackGround.png" width="500" height="70">
                    <div class = "logoWord">
                        <router-link to="/"><h2>Unification of University Information</h2></router-link>
                    </div>
                </div>
                <div class = "nav-right">
                    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                        <el-menu-item index="1">Home</el-menu-item>
                        <el-menu-item index="2">Search</el-menu-item>
                        <el-submenu index="3">
                            <template slot="title">More</template>
                            <el-menu-item index="2-1">选项1</el-menu-item>
                            <el-menu-item index="2-2">选项2</el-menu-item>
                            <el-menu-item index="2-3">选项3</el-menu-item>
                            <el-submenu index="2-4">
                            <template slot="title">选项4</template>
                            <el-menu-item index="2-4-1">选项1</el-menu-item>
                            <el-menu-item index="2-4-2">选项2</el-menu-item>
                            <el-menu-item index="2-4-3">选项3</el-menu-item>
                            </el-submenu>
                        </el-submenu>
                    </el-menu>
                </div>
                <div class="user-icon">
                    <el-avatar :size="45" icon="el-icon-user-solid"></el-avatar>
                    <!--如果已经登陆 则使用: <el-avatar> user </el-avatar> -->
                </div>
            </div>
        </el-header>
    </el-container>
</template>

<script>
    export default {
        name: 'pageheader',
        data() {
            return {
                isFixed: false,
                offsetTop: 0,
                activeIndex: '1',
                activeIndex2: '1'
            }
        },
        mounted() {
            window.addEventListener('scroll', this.initHeight)
            this.$nextTick(() => {
                this.offsetTop = document.querySelector('#boxFixed').offsetTop
            })
        },
        methods: {
            initHeight() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
                this.isFixed = scrollTop > 90
            },
            handleSelect(key, keyPath) {
                console.log(key, keyPath)
            }
        },
        destroyed() {
            window.removeEventListener('scroll', this.initHeight, false)
        }
    }
</script>

<style scoped>
.navBarWrap {
    position:absolute; /** fixed --> 始终保持在页面最上方 */
    text-align: center;
    right:0;
    left:0;
    top:0;
    width: 100%;
    background-color: white;
  }
.navBarWrap div{
    display:inline-block;
    /*vertical-align: bottom;*/
}
.bg-purple {
    background: #c19689;
  }
.nav-left {
    float: left;
    margin:0;
    padding:0;
}
.nav-right{
    float: right;
}
.user-icon {
    float: right;
    margin-top:16px;
    margin-right:30px;
}
.language {
    font-size: 13px;
    right:10px;
    margin:-10px;
    padding:-10px;
}
.earth{
    height:40px;
    width:40px;
}
.logoWord {
    position:absolute;
    top:4px;
    left: 100px;
}
a {
  text-decoration: none;
}
.router-link-active {
  text-decoration: none;
}
</style>
