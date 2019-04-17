<template>
  <v-container v-if="isCoworker">
    <h1 class="white--text">Leave a review</h1>
    <v-form justify-center class="elevation-10" v-model="valid" ref="form">
      <v-text-field
        placeholder="Give it a title"
        label="Title"
        box
        v-model="title"
        :rules="titleRules"
        required
      ></v-text-field>
      <v-textarea
        box
        auto-grow
        placeholder="How did you enjoy this space?"
        label="Comment"
        v-model="comment"
        :rules="commentRules"
        required
      ></v-textarea>

      <v-rating
        hover
        size="32"
        v-model="rating"
        :rules="ratingRules"
      ></v-rating>

      <v-btn
        @click="postReview"
        :class="{
          primary: valid,
          disabled: !valid
        }"
        >Comment</v-btn
      >
    </v-form>
  </v-container>
  <v-container v-else>
    <h1 class="white--text">Leave a review</h1>
    <h3 class="white--text">
      You must be signed in as a coworker to leave a review
    </h3>
  </v-container>
</template>

<script>
import cwspaceAPI from "@/api/cwspaces";

export default {
  name: "WriteReview",
  props: ["cwsId"],
  data() {
    return {
      valid: false,
      title: "une titre",
      titleRules: [v => !!v || "Title is required"],
      comment: "un commentaire",
      commentRules: [v => !!v || "Comment is required"],
      rating: 3,
      ratingRules: [v => !!v || "Rating is required"]
    };
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    currentUser: function() {
      return this.$store.getters.currentUser;
    },
    accountType: function() {
      return this.$store.getters.accountType;
    },
    isCoworker() {
      return this.accountType === "coworker";
    }
  },
  methods: {
    postReview() {
      const review = {
        title: this.title,
        comment: this.comment,
        rating: this.rating,
        cws_id: this.cwsId
      };
      cwspaceAPI
        .postReview(review)
        .then(({ data }) => this.onReviewPosted(data))
        .catch(({ response }) => alert(response.data.message));
    },

    onReviewPosted(eventData) {
      this.$emit("reviewposted", eventData);
    }
  }
};
</script>

<style scoped></style>
