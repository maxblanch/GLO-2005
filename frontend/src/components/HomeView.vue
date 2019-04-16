<template>
  <div class="HomeView">
    <v-layout wrap style="height: 370px">
      <v-container>
        <v-layout justify-center>
          <div>
            <h1 class="white--text">
              Find your <span>Perfect</span> Coworking Space
            </h1>
            <SearchBar></SearchBar>
          </div>
        </v-layout>
      </v-container>
    </v-layout>
  </div>
</template>

<script>
import SearchBar from "./SearchBar";
export default {
  name: "HomeView",
  components: { SearchBar }
};
</script>

<style scoped>
span {
  color: #42b983;
}
</style>
