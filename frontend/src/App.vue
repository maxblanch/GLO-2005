<template>
  <v-app id="app" dark>
    <ToolBar title="WeShare" />
    <router-view />
  </v-app>
</template>

<script>
import ToolBar from "@/components/ToolBar";
export default {
  name: "App",
  components: {
    ToolBar
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
  /*margin-top: 60px;*/
}
</style>
