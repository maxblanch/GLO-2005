<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6>
        <v-toolbar class="pt-5">
          <v-toolbar-title class="white--text"
            ><h4>Welcome Back</h4></v-toolbar-title
          >
        </v-toolbar>
        <v-card>
          <v-card-text class="pt-4">
            <div>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  label="Enter your e-mail address"
                  v-model="email"
                  :rules="emailRules"
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
                    @click="login()"
                    :class="{
                      'blue darken-4 white--text': valid,
                      disabled: !valid
                    }"
                    >Login</v-btn
                  >
                  <a href="">Forgot Password</a>
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
      password: "",
      passwordRules: [v => !!v || "Password is required"],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ]
    };
  },
  methods: {
    login: () => {
      this.$auth.login({ email, password }).then(() => {
        // Execute application logic after successful login
      });
    }
    // register: () => {
    //   this.drawer = !this.drawer;
    //   alert("asdsad");
    //   this.$auth.register({ name, email, password }).then(() => {
    //     // Execute application logic after successful registration
    //   });
    // },
    // authenticate: provider => {
    //   this.$auth.authenticate(provider).then(() => {
    //     // Execute application logic after successful social authentication
    //   });
    // }
  }
};
</script>

<style scoped></style>
