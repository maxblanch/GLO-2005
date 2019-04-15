<template>
  <v-container v-if="isLoggedIn">
    <h1 class="white--text">Leave a review</h1>
    <v-form justify-center class="elevation-10">
      <v-text-field
        placeholder="Give it a title"
        label="Title"
        box
        v-model="title"
      ></v-text-field>
      <v-textarea
        box
        auto-grow
        placeholder="How did you enjoy this space?"
        label="Review"
        v-model="review"
      ></v-textarea>

      <v-rating hover size="32"></v-rating>

      <v-btn
        :class="{
          primary: valid,
          disabled: !valid
        }"
        >Comment</v-btn
      >
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "WriteReview",
  data() {
    return {
      title: "une titre",
      review: "un commentaire"
    };
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    currentUser: function() {
      return this.$store.getters.currentUser;
    }
  }
};
</script>

<style scoped></style>
