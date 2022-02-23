<template>
<div>
    <h1>Please select in the following bars for your target modules</h1>
    <el-select v-model="value"
    class="faculty-select" filterable size="large"
    placeholder="Select the Faculty">
    <el-option
    v-for="item in facultys"
    :key="item.value"
    :label="item.label"
    :value="item.value"
    ></el-option>
    </el-select>

    <el-select v-model="value"
    class="course-select" filterable size="large"
    placeholder="Select the Course">
    <el-option
    v-for="item in courses"
    :key="item.value"
    :label="item.label"
    :value="item.value"
    ></el-option>
    </el-select>

    <el-select v-model="value"
    class="year-select" filterable size="large"
    placeholder="Select the Year">
    <el-option
    v-for="item in years"
    :key="item.value"
    :label="item.label"
    :value="item.value"
    ></el-option>
    </el-select>

    <el-select v-model="value"
    class="module-select" filterable size="large"
    placeholder="Select the Module">
    <el-option
    v-for="item in modules"
    :key="item.value"
    :label="item.label"
    :value="item.value"
    ></el-option>
    </el-select>

    <el-button type="primary">Search</el-button>
    <br><br><br><br><br><br>
 </div>
</template>

<script>
export default {
    name: 'search',
    data() {
        return {
            facultys: [{
                value: 'CELE',
                label: 'CELE'
            },
            {
                value: 'FoSE',
                label: 'FoSE'
            },
            {
                value: 'FoB',
                label: 'FoB'
            },
            {
                value: 'FHSS',
                label: 'FHSS'
            }],
            courses: [{
                value: 'CS',
                label: 'Computer Science'
            },
            {
                value: 'Math',
                Label: 'Mathematics'
            },
            {
                value: 'AE',
                label: 'Aerospace Engineering'
            },
            {
                value: 'AEE',
                label: 'Architectural Environmental Engineering'
            },
            {
                value: 'Arch',
                label: 'Architecture'
            },
            {
                value: 'Chem',
                label: 'Chemistry'
            },
            {
                value: 'CE',
                label: 'Civil Engineering'
            }],
            years: [{
                value: '1',
                label: 'CELE Year'
            },
            {
                value: '2',
                label: 'Year 2'
            },
            {
                value: '3',
                label: 'Year 3'
            },
            {
                value: '4',
                label: 'Year 4'
            }],
            modules: [{
                value: 'ACE',
                label: 'Algorithms and Computing Efficiency'
            },
            {
                value: 'GRP',
                label: 'Group Project'
            },
            {
                value: 'LAC',
                label: 'Languages and Computation'
            }]
        }
    }
}
</script>
