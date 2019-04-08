import Vue from "vue";
import Router from "vue-router";
import HomeView from "@/components/HomeView";
import CitiesView from "@/components/CitiesView";
import LogInView from "@/components/LogInView";
import SignUpView from "../components/SignUpView";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView
    },
    {
      path: "/cities",
      name: "CitiesView",
      component: CitiesView
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView
    }
  ]
});
