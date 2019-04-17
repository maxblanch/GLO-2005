<template>
  <div>
    <h1 class="white--text elevation-10" v-if="reviews.Error">
      {{ reviews.errorMessage }}
    </h1>
    <div v-else v-for="review in reviews">
      <Review
        :review="review"
        @replyposted="handleNewReplyPosted"
        :manager="manager"
      ></Review>
    </div>
    <v-spacer></v-spacer>
  </div>
</template>

<script>
import Review from "@/components/Review";
export default {
  name: "Reviews",
  components: { Review },
  props: ["reviews", "manager"],
  methods: {
    handleNewReplyPosted(eventData) {
      this.$emit("replyposted", eventData);
    }
  }
};
</script>

<style scoped></style>
