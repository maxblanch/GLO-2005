<template>
  <v-text-field
    solo
    prepend-inner-icon="location_on"
    name="searchSpace"
    placeholder="Search by City, State, Country or Name... (ex: Canada)"
    type="text"
    v-model="query"
    @keyup="search"
  ></v-text-field
></template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      query: ""
    };
  },
  methods: {
    search(e) {
      if (e.keyCode === 13) this.$router.push(`/search/${this.query}`);
    }
  }
};
</script>

<style scoped></style>
