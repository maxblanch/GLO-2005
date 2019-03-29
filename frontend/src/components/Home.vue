<template>
  <div class="Home">
    <v-layout wrap style="height: 370px">
      <v-container>
        <v-layout justify-center>
          <div>
            <h1>
              Find your <span style="color: #42b983">Perfect</span> Coworking
              Space
            </h1>
            <SearchBar></SearchBar>
          </div>
        </v-layout>
      </v-container>
    </v-layout>
  </div>
</template>

<script>
import ToolBarVue from "./ToolBarVue";
import SearchBar from "./SearchBarVue";
export default {
  name: "HomeVue",
  components: { SearchBar, ToolBarVue }
};
</script>

<style scoped></style>
