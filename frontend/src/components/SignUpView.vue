<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6 style="max-width: 80%">
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
                  label="E-mail"
                  v-model="email"
                  :rules="emailRules"
                  required
                ></v-text-field>
                <v-radio-group row v-model="gender" :rules="genderRules">
                  <v-radio label="Male" value="Male" color="primary"></v-radio>
                  <v-radio
                    label="Female"
                    value="Female"
                    color="primary"
                  ></v-radio>
                </v-radio-group>
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
                <v-text-field
                  label="Address"
                  v-model="address"
                  :rules="addressRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Postal area"
                  v-model="postalArea"
                  :rules="postalAreaRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="City"
                  v-model="city"
                  :rules="cityRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="State/province"
                  v-model="state"
                  :rules="stateRules"
                  required
                ></v-text-field>
                <v-select
                  v-model="country"
                  :items="countries"
                  :rules="countryRules"
                  menu-props="auto"
                  label="Country"
                  hide-details
                ></v-select>

                <v-radio-group
                  row
                  v-model="accountType"
                  :rules="accountTypeRules"
                >
                  <v-radio
                    label="Coworker"
                    value="Coworker"
                    color="primary"
                  ></v-radio>
                  <v-radio
                    label="Manager"
                    value="Manager"
                    color="primary"
                  ></v-radio>
                </v-radio-group>
                <v-layout justify-space-between>
                  <v-btn
                    @click="signup"
                    :class="{
                      'primary white--text': valid,
                      disabled: !valid
                    }"
                    >Sign Up</v-btn
                  >
                  <router-link to="/login"
                    >Already have an account?</router-link
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
import { countries } from "../utils/countries";

export default {
  name: "SignUpView",
  data() {
    return {
      valid: false,
      e1: true,

      firstName: "Saucy",
      firstNameRules: [v => !!v || "First name is required"],
      lastName: "Jack",
      lastNameRules: [v => !!v || "Last name is required"],
      email: "yeehaw@gmail.com",
      emailRules: [
        v => !!v || "E-mail is required",
        v =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ],
      gender: "",
      genderRules: [v => !!v || "Gender is required"],
      username: "Ashen One5",
      usernameRules: [v => !!v || "Username is required"],
      password: "sekiro",
      passwordRules: [v => !!v || "Password is required"],
      address: "3675 Avenue des Caryas",
      addressRules: [v => !!v || "Address is required"],
      postalArea: "G1G 3G2",
      postalAreaRules: [v => !!v || "Postal area is required"],
      city: "Quebec",
      cityRules: [v => !!v || "City is required"],
      state: "Quebec",
      stateRules: [v => !!v || "State is required"],
      country: "Canada",
      countryRules: [v => !!v || "Country is required"],
      accountType: "",
      accountTypeRules: [v => !!v || "Account type is required"],

      countries: countries
    };
  },
  methods: {
    signup() {
      if (!this.valid) return;
      const user = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        gender: this.gender,
        username: this.username,
        password: btoa(this.password),
        address: this.address,
        postal_area: this.postalArea,
        city: this.city,
        state: this.state,
        country: this.country
      };

      this.$store
        .dispatch(`register${this.accountType}`, user)
        .then(res => {
          console.log(res);
          this.$router.push("/");
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
