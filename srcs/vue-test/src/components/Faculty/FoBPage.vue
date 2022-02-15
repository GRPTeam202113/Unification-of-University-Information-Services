<template>
    <div class ="fob">
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <h1>This is FoB page !</h1>
        <router-link to="/">Back to Main</router-link>
        <p>{{Msg}}</p>
    </div>
</template>

<script>
    export default {
        name: 'fob',
        data () {
            return {
                Msg: 'Welcome to FoB !'
            }
        }
    }
</script>
