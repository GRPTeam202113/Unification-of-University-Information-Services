<template>
    <div class="course">
        <h1 class="title">{{degree}}</h1>
        <el-divider></el-divider>
        <br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../assets/square.png" alt="">
                <span class="square-container">
                    <div class="normalTitle" style="padding-bottom:1em;">Key information</div>
                    <div class="flex-container">
                    <div class="title-container">
                        <div class="info-title">Degree</div>
                        <div class="info-title">Types of study</div>
                        <div class="info-title">Duration</div>
                        <div class="info-title">Start date</div>
                        <div class="info-title">Faculty</div>
                        <div class="info-title">Study model</div>
                    </div>
                    <div class="content-container">
                        <div class="info-content">{{degree}}</div>
                        <div class="info-content">{{typeOfStudy}}</div>
                        <div class="info-content">{{duration}}</div>
                        <div class="info-content">{{startDate}}</div>
                        <div class="info-content">{{faculty}}</div>
                        <div class="info-content">{{studyModel}}</div>
                    </div>
                    </div>
                    <span class="note-title">Note:</span>
                    <span class="note-content">For the 2+2 study model courses, the student will spend the last two years at our UK campus. For the 4+0 study model courses, the student will spend the entire degree programme in Ningbo, China with study abroad opportunities from year three.</span>
                </span>
            </div>
        </div>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../assets/square.png" alt="">
                <span class="squareTitle">
                    <div class="normalTitle"> Course structure</div>
                </span>
            </div>
            <div class="course-content">{{courseContent}}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'course',
    data() {
        return {
            degree: 'BSc (Hons) Computer Science',
            typeOfStudy: 'Full Year',
            duration: 'Three or four years depending on entry qualifications',
            startDate: 'September 2022',
            faculty: 'Computer Science / Faculty of Science and Engineering',
            studyModel: '2+2, 4+0',
            // newline for courseContent should add <br>*2 in the source
            courseContent: 'This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!This is the course of computer science!'
        }
    }
}
</script>

<style scoped>
.title{
    margin-left: 30px;
    font-size:50px;
    font-weight:bold;
    color: black;
}
.square{
    margin-left: 20px;
    width: 90px;
    height: 90px;
}
.squareTitle{
    position: absolute;
    bottom: 20px;
    left: 50px;
    position: absolute;
    color:rgb(0, 0, 0);
    background-color: #F7F7F8;
    width:90%;
    padding-left:5px;
    padding-top:6px;
    padding-bottom: 6px;
    font-size:25px;
    font-weight: bolder;
}

.square-container{
position: absolute;
    /* bottom: 20px; */
    top: 20px;
    left: 50px;
    position: absolute;
    color:rgb(0, 0, 0);
    background-color: #F7F7F8;
    width:90%;
    padding-left:5px;
    padding-top:6px;
    padding-bottom: 6px;
    font-size:25px;
    font-weight:900;
}

.info-title{
    font-weight: bolder;
    font-size: 18px;
}

.info-content{
    font-weight: bold;
    font-size: 16px;
}

.flex-container{
    display: flex;
}

.title-container{
    line-height: 150%;
}

.content-container{
    line-height: 150%;
    padding-left: 6em;
}

.note-title{
    font-weight:bolder;
    font-size: 8px;
}

.note-content{
    font-weight: 400;
    font-size: 8px;
    line-height: 16px;
}
.course-content{
    margin: 4em;
}
</style>
