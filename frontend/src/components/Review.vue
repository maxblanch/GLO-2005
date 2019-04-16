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

          <h2 class="white--text">big boi replied to this review</h2>
          <p class="white--text">
            {{ reply.comment }}
          </p>

          <!--          <WriteReply></WriteReply>-->
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
import CoworkerAPI from "../api/coworker";
import ManagerAPI from "../api/manager";
import cwspaceAPI from "../api/cwspaces";
import WriteReply from "@/components/WriteReply";
export default {
  name: "Review",
  components: { WriteReply },
  props: ["review"],
  data() {
    return { author: {}, reply: {}, replyAuthor: {} };
  },
  mounted() {
    CoworkerAPI.get(this.review.coworkerId).then(this.setReviewAuthor);
    cwspaceAPI
      .getReply(this.review.reviewId)
      .then(this.setReply)
      .catch(({ response }) => console.log(response.data.message));
    ManagerAPI.get(this.reply.managerId).then(({ data }) => console.log(data));
  },
  methods: {
    setReviewAuthor(author) {
      this.author = author;
    },
    setReply(reply) {
      this.reply = reply;
    }
  }
};
</script>

<style scoped></style>
