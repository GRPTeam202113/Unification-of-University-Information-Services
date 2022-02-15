<template>
<div>
  <el-carousel :interval="5000" type="card" height="500px">
  <el-carousel-item v-for="item in images" :key="item">
    <img :src="item.url" alt="无图片"/>
  </el-carousel-item>
  </el-carousel>
  <br><br><br>
  <div class="title">Schools and Departments</div>
  <el-divider></el-divider>
  <br><br>
  <el-row>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card class="box-card" shadow="hover">
        <span><h2>Centre for English Language Education</h2></span>
        <div class="introduction">{{ celeIntro }}</div>
        <br><br>
        <div style="padding: 14px;">
            <div class="bottom clearfix">
              <el-button class="learnMoreButton" icon="el-icon-right"><router-link to="/cele">Learn More</router-link></el-button>
            </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card :body-style="{ padding: '20px'}" el-card shadow="hover">
        <img src="../assets/Faculty/cele.jpg" class="image">
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
  </el-row>
  <br><br><br><br><br><br><br><br>
  <el-row>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card :body-style="{ padding: '20px'}" el-card shadow="hover">
        <img src="../assets/Faculty/fob.jpg" class="image">
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card class="box-card" shadow="hover">
        <span><h2>Faculty of Business</h2></span>
        <div class="introduction">{{ fobIntro }}</div>
        <br><br><br><br><br>
        <div style="padding: 14px;">
            <div class="bottom clearfix">
              <el-button class="learnMoreButton" icon="el-icon-right"><router-link to="/fob">Learn More</router-link></el-button>
            </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <br><br><br><br><br><br><br><br>
  <el-row>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card class="box-card" shadow="hover">
        <span><h2>Faculty of Humanities and Social Sciences</h2></span>
        <div class="introduction">{{ fhssIntro }}</div>
        <br>
        <div style="padding: 14px;">
            <div class="bottom clearfix">
              <el-button class="learnMoreButton" icon="el-icon-right"><router-link to="/fhss">Learn More</router-link></el-button>
            </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card :body-style="{ padding: '20px'}" el-card shadow="hover">
        <img src="../assets/Faculty/fhss.jpg" class="image">
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
  </el-row>
  <br><br><br><br><br><br><br><br>
  <el-row>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card :body-style="{ padding: '20px'}" el-card shadow="hover">
        <img src="../assets/Faculty/fose.jpg" class="image">
      </el-card>
    </el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
    <el-col :span="10">
      <el-card class="box-card" shadow="hover">
        <span><h2>Faculty of Science and Engineering</h2></span>
        <div class="introduction">{{ celeIntro }}</div>
        <br><br>
        <div style="padding: 14px;">
            <div class="bottom clearfix">
              <el-button class="learnMoreButton" icon="el-icon-right"><router-link to="/fose">Learn More</router-link></el-button>
            </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <br><br><br><br><br><br>
</div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to ',
      images: [
          {url: require('../assets/MainBackGround1.jpeg')},
          {url: require('../assets/MainBackGround2.jpg')},
          {url: require('../assets/MainBackGround3.jpg')},
          {url: require('../assets/MainBackGround4.jpg')}],
      celeIntro: 'We are one of the largest and most well-established English language teaching departments in the world.',
      fobIntro: 'We offer business programmes at undergraduate, postgraduate and executive levels.',
      fhssIntro: 'Programmes on Economics, Education and English, International Communications, and International Studies from undergraduate to postgraduate level.'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.time {
    font-size: 13px;
    color: #999;
  }
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .button {
    margin: 5%;
    padding: 0;
    float: right;
  }
  .image {
    width: 100%;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
.celeImage {
  margin-left: 45%;
  margin-right: 15%;
}
.celeTitle {
  margin-left: 5%;
  margin-bottom: 350px;
  font-size: 30px;
  font-weight: bolder;
}
.introduction{
  font-size: 20px;
  color: rgb(131, 131, 131);
}
.grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
.bg-purple-white {
    background: #ffffff;
}
.box-card {
    margin-left: 3%;
  }
.title {
    margin-left: 30px;
    font-size: 70px;
    font-weight: bold;
    color: rgb(0, 0, 0);
  }
.learnMoreButton {
  background-color: #ffffff;
  float: right;
}
h1, h2 {
  font-weight: bolder;
  font-size: 50px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
