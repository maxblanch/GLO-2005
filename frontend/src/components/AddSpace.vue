<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6 style="max-width: 80%" v-if="isManager">
        <v-toolbar class="pt-5 primary darken-1">
          <v-toolbar-title class="white--text"
            ><h4>New workspace</h4></v-toolbar-title
          >
        </v-toolbar>
        <v-card>
          <v-card-text class="pt-4">
            <div>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  label="Name"
                  v-model="name"
                  :rules="nameRules"
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
                  label="Country"
                  v-model="country"
                  :items="countries"
                  :rules="countryRules"
                  menu-props="auto"
                  hide-details
                ></v-select>
                <v-textarea
                  box
                  auto-grow
                  label="Description"
                  v-model="description"
                  :rules="descriptionRules"
                  required
                ></v-textarea>
                <v-text-field
                  label="Image Url"
                  v-model="imageUrl"
                  :rules="imageUrlRules"
                  required
                ></v-text-field>
                <v-select
                  label="Currency"
                  v-model="currency"
                  :items="currencies"
                  :rules="currencyRules"
                  menu-props="auto"
                  hide-details
                ></v-select>
                <v-text-field
                  label="Price per day (No decimals)"
                  v-model="pricePerDay"
                  :rules="pricePerDayRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Price per week (No decimals)"
                  v-model="pricePerWeek"
                  :rules="pricePerWeekRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Price per month (No decimals)"
                  v-model="pricePerMonth"
                  :rules="pricePerMonthRules"
                  required
                ></v-text-field>

                <v-layout justify-space-between>
                  <v-btn
                    @click="addSpace"
                    :class="{
                      'primary white--text': valid,
                      disabled: !valid
                    }"
                    >Add Space</v-btn
                  >
                </v-layout>
              </v-form>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>

      <v-flex v-else>
        <h1 class="white--text">
          You must be logged in as a manager to add spaces
        </h1>
        <router-link to="/signup"
          >Create a free manager account now!</router-link
        >
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { countries } from "../utils/countries";
import currencyAPI from "../utils/currencies";
import cwspaceAPI from "@/api/cwspaces";

export default {
  name: "AddSpace",
  data() {
    return {
      valid: false,
      name: "",
      nameRules: [v => !!v || "Name is required"],
      address: "",
      addressRules: [v => !!v || "Address is required"],
      postalArea: "",
      postalAreaRules: [v => !!v || "Postal area is required"],
      city: "",
      cityRules: [v => !!v || "City is required"],
      state: "",
      stateRules: [v => !!v || "State is required"],
      country: "",
      countryRules: [v => !!v || "Country is required"],
      description: "",
      descriptionRules: [v => !!v || "Description is required"],
      imageUrl: "https://cdn2.thecatapi.com/images/Qjb0fsrDo.jpg",
      imageUrlRules: [v => !!v || "Image Url is required"],
      currency: "",
      currencyRules: [v => !!v || "Currency is required"],
      pricePerDay: "",
      pricePerDayRules: [v => !!v || "Price per day is required"],
      pricePerWeek: "",
      pricePerWeekRules: [v => !!v || "Price per week is required"],
      pricePerMonth: "",
      pricePerMonthRules: [v => !!v || "Price per month is required"],

      currencies: currencyAPI.get(),
      countries: countries
    };
  },
  methods: {
    addSpace() {
      if (!this.valid) return;
      const cwspace = {
        name: this.name,
        address: this.address,
        postal_area: this.postalArea,
        city: this.city,
        state: this.state,
        country: this.country,
        latitude: parseInt(this.latitude),
        longitude: parseInt(this.longitude),
        description: this.description,
        image_url: this.imageUrl,
        currency: this.currency,
        day_price: parseInt(this.pricePerDay),
        week_price: parseInt(this.pricePerWeek),
        month_price: parseInt(this.pricePerMonth)
      };

      cwspaceAPI
        .addSpace(cwspace)
        .then(({ data }) => {
          console.log(data);
          this.$router.push(`/cwspace/${data.cws_id}`);
        })
        .catch(err => {
          console.log(err.response);
          alert(err.response.data.msg);
        });
    }
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    accountType: function() {
      return this.$store.getters.accountType;
    },
    isManager: function() {
      return this.accountType === "manager";
    }
  }
};
</script>

<style scoped></style>
