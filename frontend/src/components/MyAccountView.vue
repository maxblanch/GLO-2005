<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Account type</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ accountType }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">First name</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.firstName }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Last name</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.lastName }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">email</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.email }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Gender</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.gender }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Username</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.username }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Address</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.address }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Postal area</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.postalArea }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">City</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.city }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">State</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.state }}</h1>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs4>
        <h1 class="white--text">Country</h1>
      </v-flex>
      <v-flex xs4>
        <h1 class="white--text">{{ currentUser.country }}</h1>
      </v-flex>
    </v-layout>

    <v-btn class="error">Close Account</v-btn>
  </v-container>
</template>

<script>
export default {
  name: "MyAccountView",
  props: ["currentUser"],
  computed: {
    accountType: function() {
      return this.$store.getters.accountType;
    }
  }
};
</script>

<style scoped></style>
