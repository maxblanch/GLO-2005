<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6>
        <v-toolbar class="pt-5 primary darken-1">
          <v-toolbar-title class="white--text"
            ><h4>Welcome Home, Ashen One</h4></v-toolbar-title
          >
        </v-toolbar>
        <v-card>
          <v-card-text class="pt-4">
            <div>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  label="Enter your WeShare username"
                  v-model="username"
                  :rules="usernameRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Enter your password"
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
                    @click="login"
                    :class="{
                      'primary white--text': valid,
                      disabled: !valid
                    }"
                    >Login</v-btn
                  >
                  <router-link to="/signup"
                    >You don't already have an account?</router-link
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
  name: "LogInView",
  data() {
    return {
      valid: false,
      e1: false,
      password: "sekiro",
      passwordRules: [v => !!v || "Password is required"],
      username: "Ashen One",
      usernameRules: [v => !!v || "Username is required"]
    };
  },
  methods: {
    login() {
      let user = { username: this.username, password: btoa(this.password) };
      console.log(`connecting user ${user.username}`);
      this.$auth
        .login(user)
        .then(res => {
          console.log(res);
          this.$router.push("/");
          // Execute application logic after successful login
        })
        .catch(err => {
          console.log(err.response);
          alert(err.response.data.message);
        });
    }
  }
};
</script>

<style scoped></style>
