<template>
    <div class ="fhss">
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <h1>This is FHSS page !</h1>
        <router-link to="/">Back to Main</router-link>
        <p>{{Msg}}</p>
    </div>
</template>

<script>
    export default {
        name: 'fhss',
        data () {
            return {
                Msg: 'Welcome to FHSS !'
            }
        }
    }
</script>
