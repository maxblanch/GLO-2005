// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuetify from "vuetify";

import "vuetify/dist/vuetify.min.css"; // Ensure you are using css-loader
import App from "./App";
import router from "./router";
import axios from "axios";
import store from "./store";
// import "./../node_modules/bulma/css/bulma.css";

Vue.prototype.$http = axios;
const token = localStorage.getItem("token");
if (token) Vue.prototype.$http.defaults.headers.common["Authorization"] = token;

Vue.config.productionTip = false;

Vue.use(Vuetify, {
  theme: {
    primary: "#42b983",
    secondary: "#b0bec5",
    accent: "#8c9eff",
    error: "#b71c1c"
  }
});

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});
