// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuetify from "vuetify";

import "vuetify/dist/vuetify.min.css"; // Ensure you are using css-loader
import App from "./App";
import router from "./router";
import VueAxios from "vue-axios";
import VueAuthenticate from "vue-authenticate";
import axios from "axios";

Vue.config.productionTip = false;

Vue.use(Vuetify, {
  theme: {
    primary: "#42b983",
    secondary: "#b0bec5",
    accent: "#8c9eff",
    error: "#b71c1c"
  }
});
Vue.use(VueAxios, axios);
Vue.use(VueAuthenticate, {
  baseUrl: "http://localhost:5000" // API domain
  // providers: {
  // //Define OAuth providers config
  //   github: {
  //     clientId: "",
  //     redirectUri: "http://localhost:8080/cities" // client app callback
  //   }
  // }
});

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>"
});
