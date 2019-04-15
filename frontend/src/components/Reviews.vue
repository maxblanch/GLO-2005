<template>
  <div>
    <h1 class="white--text elevation-10" v-if="reviews.Error">
      {{ reviews.errorMessage }}
    </h1>
    <div v-else v-for="review in reviews">
      <Review :review="review"></Review>
    </div>
    <v-spacer></v-spacer>
  </div>
</template>

<script>
import Review from "@/components/Review";
export default {
  name: "Reviews",
  components: { Review },
  props: ["reviews"]
};
</script>

<style scoped></style>
