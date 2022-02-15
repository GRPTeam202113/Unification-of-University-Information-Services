<template>
    <div class ="fose">
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <h1>This is FoSE page !</h1>
        <router-link to="/">Back to Main</router-link>
        <p>{{Msg}}</p>
    </div>
</template>
<script>
    export default {
        name: 'fose',
        data () {
            return {
                Msg: 'Welcome to FoSE !'
            }
        }
    }
</script>
