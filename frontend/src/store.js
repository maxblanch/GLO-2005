import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    user: localStorage.getItem("username") || ""
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, { token, user }) {
      state.status = "success";
      state.token = token;
      state.user = user;
    },
    auth_error(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: "http://localhost:5000/login",
          data: user,
          method: "POST"
        })
          .then(resp => {
            const token = resp.data.access_token;
            const user = JSON.parse(resp.config.data).username;
            localStorage.setItem("token", token);
            localStorage.setItem("username", user);

            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, user });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            reject(err);
          });
      });
    },
    registerCoworker({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: `http://localhost:5000/coworker/register`,
          data: user,
          method: "POST"
        })
          .then(resp => {
            axios({
              url: "http://localhost:5000/login",
              data: user,
              method: "POST"
            })
              .then(resp => {
                const token = resp.data.access_token;
                const user = JSON.parse(resp.config.data).username;
                localStorage.setItem("token", token);
                localStorage.setItem("username", user);

                axios.defaults.headers.common["Authorization"] = token;
                commit("auth_success", { token, user });
                resolve(resp);
              })
              .catch(err => {
                commit("auth_error");
                localStorage.removeItem("token");
                localStorage.removeItem("username");
                reject(err);
              });
          })
          .catch(err => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit("logout");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    currentUser: state => state.user
  }
});