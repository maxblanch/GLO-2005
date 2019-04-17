import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    username: localStorage.getItem("username") || "",
    type: localStorage.getItem("accountType") || "",
    id: localStorage.getItem("id") || ""
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, { token, username, type, id }) {
      state.status = "success";
      state.token = token;
      state.username = username;
      state.type = type;
      state.id = id;
    },
    auth_error(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.username = "";
      state.type = "";
      state.id = -1;
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
            const username = JSON.parse(resp.config.data).username;
            const type = resp.data.type;
            const id = resp.data.id;
            localStorage.setItem("token", token);
            localStorage.setItem("username", username);
            localStorage.setItem("accountType", type);
            localStorage.setItem("id", id);

            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, username, type, id });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            localStorage.removeItem("accountType");
            localStorage.removeItem("id");

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
                const username = JSON.parse(resp.config.data).username;
                const type = resp.data.type;
                const id = resp.data.id;
                localStorage.setItem("token", token);
                localStorage.setItem("username", username);
                localStorage.setItem("accountType", type);
                localStorage.setItem("id", id);

                axios.defaults.headers.common["Authorization"] = token;
                commit("auth_success", { token, username, type, id });
                resolve(resp);
              })
              .catch(err => {
                commit("auth_error");
                localStorage.removeItem("token");
                localStorage.removeItem("username");
                localStorage.removeItem("accountType");
                localStorage.removeItem("id");
                reject(err);
              });
          })
          .catch(err => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            localStorage.removeItem("accountType");
            localStorage.removeItem("id");
            reject(err);
          });
      });
    },
    registerManager({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: `http://localhost:5000/manager/register`,
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
                const username = JSON.parse(resp.config.data).username;
                const type = resp.data.type;
                const id = resp.data.id;
                localStorage.setItem("token", token);
                localStorage.setItem("username", username);
                localStorage.setItem("accountType", type);
                localStorage.setItem("id", id);

                axios.defaults.headers.common["Authorization"] = token;
                commit("auth_success", { token, username, type, id });
                resolve(resp);
              })
              .catch(err => {
                commit("auth_error");
                localStorage.removeItem("token");
                localStorage.removeItem("username");
                localStorage.removeItem("accountType");
                localStorage.removeItem("id");
                reject(err);
              });
          })
          .catch(err => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            localStorage.removeItem("accountType");
            localStorage.removeItem("id");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit("logout");
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        localStorage.removeItem("accountType");
        localStorage.removeItem("id");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    currentUser: state => state.username,
    accountType: state => state.type,
    userId: state => state.id

    // isLoggedIn: () => localStorage.getItem("token"),
    // currentUser: () => localStorage.getItem("username"),
    // accountType: () => localStorage.getItem("accountType"),
    // userId: () => localStorage.getItem("id")
  }
});
