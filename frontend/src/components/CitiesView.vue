<template>
  <v-layout>
    <v-container>
      <v-layout justify-center>
        <div>
          <h1 v-for="cwspace in cwspaces">
            <router-link :to="cwspace.cityRoute">
              {{ cwspace.city }}
            </router-link>
          </h1>
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  name: "CitiesView",
  props: ["cwspaces"]
};
</script>

<style scoped></style>
