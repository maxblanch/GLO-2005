<template>
  <v-container fluid fill-height>
    <v-layout flex align-center justify-center>
      <v-flex xs12 sm4 elevation-6 style="max-width: 80%">
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
                <v-text-field
                  label="Latitude"
                  v-model="latitude"
                  :rules="latitudeRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Longitude"
                  v-model="longitude"
                  :rules="longitudeRules"
                  required
                ></v-text-field>
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
                  label="Price per day"
                  v-model="pricePerDay"
                  :rules="pricePerDayRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Price per week"
                  v-model="pricePerWeek"
                  :rules="pricePerWeekRules"
                  required
                ></v-text-field>
                <v-text-field
                  label="Price per month"
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
      name: "Saucy",
      nameRules: [v => !!v || "Name is required"],
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
      latitude: "12.3212",
      latitudeRules: [v => !!v || "Latitude is required"],
      longitude: "11.1231",
      longitudeRules: [v => !!v || "Longitude is required"],
      description: "hehe boi",
      descriptionRules: [v => !!v || "Description is required"],
      imageUrl: "https://cdn2.thecatapi.com/images/Qjb0fsrDo.jpg",
      imageUrlRules: [v => !!v || "Image Url is required"],
      currency: "",
      currencyRules: [v => !!v || "Currency is required"],
      pricePerDay: "18",
      pricePerDayRules: [v => !!v || "Price per day is required"],
      pricePerWeek: "205",
      pricePerWeekRules: [v => !!v || "Price per week is required"],
      pricePerMonth: "350",
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

      console.log("creating workspace");
      console.log(cwspace);
      cwspaceAPI
        .addSpace(cwspace)
        .then(res => console.log(res))
        .catch(err => {
          console.log(err.response);
          alert(err.response.data.msg);
        });
    }
  }
};
</script>

<style scoped></style>
