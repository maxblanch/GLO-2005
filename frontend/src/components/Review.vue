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
            Review left by: {{ author.username }} on: {{ review.date }}
          </p>

          <h2 class="white--text" v-if="hasReply">
            {{ manager.username }} replied to this review
          </h2>
          <p class="white--text" v-if="hasReply">
            {{ reply.comment }}
          </p>

          <WriteReply v-if="isOwner"></WriteReply>
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
import CoworkerAPI from "../api/coworker";
import cwspaceAPI from "../api/cwspaces";
import WriteReply from "@/components/WriteReply";
export default {
  name: "Review",
  components: { WriteReply },
  props: ["review", "manager"],
  data() {
    return { author: {}, reply: {}, hasReply: true };
  },
  mounted() {
    CoworkerAPI.get(this.review.coworkerId)
      .then(this.setReviewAuthor)
      .catch(({ response }) => console.log(response.data.message));
    cwspaceAPI
      .getReply(this.review.reviewId)
      .then(this.setReply)
      .catch(({ response }) => {
        this.hasReply = false;
        console.log(response.data.message);
      });
  },
  methods: {
    setReviewAuthor(author) {
      this.author = author;
    },
    setReply(reply) {
      this.reply = reply;
    }
  },
  computed: {
    currentUser: function() {
      return this.$store.getters.currentUser;
    },
    isOwner: function() {
      return this.currentUser === this.manager.managerId;
    }
  }
};
</script>

<style scoped></style>
