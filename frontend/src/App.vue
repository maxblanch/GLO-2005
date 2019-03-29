<template>
  <div id="app">
    <ToolBarVue title="un titre"></ToolBarVue>
    <HomeVue></HomeVue>

    <!--    <img alt="Vue logo" src="./assets/logo.png" />-->
    <!--    <HelloWorld msg="Welcome to Your Vue.js App" />-->
    <router-view></router-view>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import ToolBarVue from "./components/ToolBarVue";
import HomeVue from "./components/Home";

export default {
  name: "app",
  components: {
    HomeVue,
    ToolBarVue,
    HelloWorld
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  //margin-top: 60px;
}
</style>
