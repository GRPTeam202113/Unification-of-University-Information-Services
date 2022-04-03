/*
 * @Descripttion: the manually created database for 3 faculty (FOSE FHSS FOB)
 * about the course details under each faculty
 * @Author: Yifei Shao
 * @Date: 2022-03-08 10:34:42
 * @LastEditTime: 2022-03-15 10:48:58
 */

var FOSE = [{
                    value: 'AE',
                    label: 'Aerospace Engineering'
                },
                {
                    value: 'AEE',
                    label: 'Architectural Environment Engineering'
                },
                {
                    value: 'ARCH',
                    label: 'Architecture'
                },
                {
                    value: 'CHEM',
                    label: 'Chemistry'
                },
                {
                    value: 'CE',
                    label: 'Civil Engineering'
                },
                {
                    value: 'CS',
                    label: 'Computer Science'
                },
                {
                    value: 'CSAI',
                    label: 'Computer Science with Artificial Intelligence'
                },
                {
                    value: 'EEE',
                    label: 'Electrical and Electronic Engineering'
                },
                {
                    value: 'ENS',
                    label: 'Environmental Engineering'
                },
                {
                    value: 'MATH',
                    label: 'Mathematics with Applied Mathematics'
                },
                {
                    value: 'ME',
                    label: 'Mechanical Engineering'
                },
                {
                    value: 'PDM',
                    label: 'Product Design and Manufacture'
                },
                {
                    value: 'STA',
                    label: 'Statistics'
                }]

var FOB = [{
                value: 'FAM',
                label: 'Finance, Accounting and Management'
            },
            {
                value: 'IBE',
                label: 'International Business Economics'
            },
            {
                value: 'IBM',
                label: 'International Business Management'
            },
            {
                value: 'IBC',
                label: 'International Business with Communication Studies'
            },
            {
                value: 'IBL',
                label: 'International Business with Language'
        }]

var FHSS = [{
                value: 'ECO',
                label: 'Economics'
            },
            {
                value: 'EGA',
                label: 'English Language and Applied Linguistics'
            },
            {
                value: 'EGL',
                label: 'English Language and Literature'
            },
            {
                value: 'IC',
                label: 'International Communications Studies'
            },
            {
                value: 'ICL',
                label: 'International Communications Studies with Chinese'
            },
            {
                value: 'IET',
                label: 'International Economics and Trade'
            },
            {
                value: 'IS',
                label: 'International Studies'
            },
            {
                value: 'ISL',
                label: 'International Studies with Spanish German French Japanese Chinese'
            }]
module.exports = {
    FOB: FOB,
    FHSS: FHSS,
    FOSE: FOSE
}
