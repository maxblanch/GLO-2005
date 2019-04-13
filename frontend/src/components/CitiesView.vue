<template>
  <v-layout>
    <v-container>
      <v-layout justify-center>
        <div>
          <h1
            @click="goToCity(cwspace.city)"
            class="white--text"
            v-for="cwspace in cwspaces"
          >
            {{ cwspace.city }}
          </h1>
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  name: "CitiesView",
  props: ["cwspaces"],
  methods: {
    goToCity(city) {
      this.$router.push(`/cities/${city}`);
    }
  }
};
</script>

<style scoped></style>
