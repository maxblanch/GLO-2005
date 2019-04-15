<template>
  <v-layout>
    <v-container>
      <v-layout justify-center class="elevation-10">
        <div>
          <h1 class="white--text">"{{ review.title }}"</h1>
          <h2 class="white--text">{{ review.rating }} / 5</h2>
          <p class="white--text">
            {{ review.comment }}
          </p>
          <p class="white--text">
            Review left by{{ author.username }} on {{ review.date }}
          </p>
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
import CoworkerAPI from "../api/coworker";
export default {
  name: "Review",
  props: ["review"],
  data() {
    return { author: {} };
  },
  mounted() {
    CoworkerAPI.get(this.review.coworkerId).then(this.setAuthor);
  },
  methods: {
    setAuthor(author) {
      this.author = author;
    }
  }
};
</script>

<style scoped></style>
