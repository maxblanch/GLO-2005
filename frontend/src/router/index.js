import Vue from "vue";
import Router from "vue-router";
import HomeView from "@/components/HomeView";
import Cities from "@/components/Cities";
import LogInView from "@/components/LogInView";
import SignUpView from "@/components/SignUpView";
import CWSpacePage from "@/components/CWSpacePage";
import CWSpaceCard from "@/components/CWSpaceCard";

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
      name: "Cities",
      component: Cities
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
    },
    {
      path: "/cwspace/:id",
      name: "CWSpacePage",
      component: CWSpacePage
    },
    {
      path: "/cwspaces/",
      name: "CWSpaceCard",
      component: CWSpaceCard
    }
  ]
});
