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

          <WriteReply
            v-if="isOwner"
            @replyposted="handleNewReplyPosted"
            :reviewId="review.reviewId"
          ></WriteReply>
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
    },
    handleNewReplyPosted(eventData) {
      this.$emit("replyposted", eventData);
    }
  },
  computed: {
    currentUser: function() {
      return this.$store.getters.currentUser;
    },
    accountType: function() {
      return this.$store.getters.accountType;
    },
    userId: function() {
      return this.$store.getters.userId;
    },
    isManager: function() {
      return this.accountType === "manager";
    },
    isCoworker: function() {
      return this.accountType === "coworker";
    },
    isOwner: function() {
      let test = false;

      if (this.isManager)
        test = this.userId === this.manager.managerId.toString();

      console.log(test);

      return test;
    }
  }
};
</script>

<style scoped></style>
