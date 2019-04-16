<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap v-for="item in items">
      <v-flex xs6>
        <h2 class="white--text">{{ item.title }}</h2>
      </v-flex>
      <v-flex xs6>
        <h3 class="white--text">{{ item.value }}</h3>
      </v-flex>
    </v-layout>

    <v-btn class="error">Close Account</v-btn>
  </v-container>
</template>

<script>
export default {
  name: "MyAccountView",
  props: ["currentUser"],
  data() {
    return {
      items: [
        { title: "Account Type", value: this.$store.getters.accountType },
        { title: "First Name", value: this.currentUser.firstName },
        { title: "Last Name", value: this.currentUser.lastName },
        { title: "E-mail", value: this.currentUser.email },
        { title: "Gender", value: this.currentUser.gender },
        { title: "Username", value: this.currentUser.username },
        { title: "Address", value: this.currentUser.address },
        { title: "Postal Area", value: this.currentUser.postalArea },
        { title: "City", value: this.currentUser.city },
        { title: "State", value: this.currentUser.state },
        { title: "Country", value: this.currentUser.country }
      ]
    };
  }
};
</script>

<style scoped></style>
