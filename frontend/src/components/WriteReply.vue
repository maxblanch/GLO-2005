<template>
  <v-layout justify-center>
    <v-form v-model="valid" ref="form">
      <v-textarea
        box
        auto-grow
        placeholder="Reply to this comment"
        label="Reply"
        v-model="reply"
        :rules="replyRules"
        required
      ></v-textarea>

      <v-btn
        @click="postReply"
        :class="{
          primary: valid,
          darken1: valid,
          disabled: !valid
        }"
        >Reply</v-btn
      >
    </v-form>
  </v-layout>
</template>

<script>
import cwspaceAPI from "@/api/cwspaces";

export default {
  name: "WriteReply",
  props: ["reviewId"],
  data() {
    return {
      valid: false,
      reply: "",
      replyRules: [v => !!v || "Reply is required"]
    };
  },
  methods: {
    postReply() {
      const reply = { review_id: this.reviewId, comment: this.reply };
      cwspaceAPI
        .postReply(reply)
        .then(({ data }) => this.onReplyPosted(data))
        .catch(({ response }) => alert(response.data.message));
    },
    onReplyPosted(eventData) {
      this.$emit("replyposted", eventData);
    }
  }
};
</script>

<style scoped></style>
