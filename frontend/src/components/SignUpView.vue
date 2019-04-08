<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6>
        <v-toolbar class="pt-5 primary darken-1">
          <v-toolbar-title class="white--text"
            ><h4>Welcome to the family, son!</h4></v-toolbar-title
          >
        </v-toolbar>
        <v-card>
          <v-card-text class="pt-4">
            <div>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  label="First name"
                  v-model="firstName"
                  :rules="firstNameRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Last name"
                  v-model="lastName"
                  :rules="lastNameRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Username"
                  v-model="username"
                  :rules="usernameRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Password"
                  v-model="password"
                  min="8"
                  :append-icon="e1 ? 'visibility' : 'visibility_off'"
                  :append-icon-cb="() => (e1 = !e1)"
                  :type="e1 ? 'password' : 'text'"
                  :rules="passwordRules"
                  counter
                  required
                ></v-text-field>

                <v-layout justify-space-between>
                  <v-btn
                    @click="signup"
                    :class="{
                      'primary white--text': valid,
                      disabled: !valid
                    }"
                    >Sign Up</v-btn
                  >
                </v-layout>
              </v-form>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      valid: false,
      e1: false,
      firstName: "Saucy",
      firstNameRules: [v => !!v || "First name is required"],
      lastName: "Jack",
      lastNameRules: [v => !!v || "Last name is required"],
      password: "sekiro",
      passwordRules: [v => !!v || "Password is required"],
      username: "Ashen One",
      usernameRules: [
        v => !!v || "Username is required"
        // v =>
        //   /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
        //   "E-mail must be valid"
      ]
    };
  },
  methods: {
    signup() {
      let user = { username: this.username, password: this.password };
      console.log(`connecting user ${user.username}`);
      this.$auth
        .login(user)
        .then(res => {
          console.log(res);
          alert(res);
          // Execute application logic after successful login
        })
        .catch(err => {
          console.log(err.response);
          alert(err.response.data.msg);
        });
    }
  }
};
</script>

<style scoped></style>
