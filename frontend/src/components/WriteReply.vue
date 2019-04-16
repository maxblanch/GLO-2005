<template>
  <v-layout justify-center>
    <v-form v-if="isManager" v-model="valid" ref="form">
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
export default {
  name: "WriteReply",
  data() {
    return {
      valid: false,
      reply: "no buli",
      replyRules: [v => !!v || "Reply is required"]
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
    isManager: function() {
      return this.accountType === "manager";
    }
  },
  methods: {
    postReply() {
      alert(this.reply);
    }
  }
};
</script>

<style scoped></style>
