<template>
  <div class="crop-container">
    <img alt="Invezted logo" src="./assets/Invezted-logo-G.jpg" height="1000">
  </div>
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'


export default {
  name: 'App',
  components: {
    HelloWorld,

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 5px;
  background-color: #0D2A38;
}

.crop-container {
    width: 1900px;
    height: 280px;
    overflow: hidden;
}
.crop-container img {
    margin-top: -300px;
    margin-left: -860px;
}


</style>
