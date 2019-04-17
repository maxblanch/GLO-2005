<template>
  <nav>
    <v-responsive>
      <v-toolbar>
        <v-toolbar-side-icon
          @click.stop="drawer = !drawer"
          class="hidden-sm-and-up"
        ></v-toolbar-side-icon>
        <v-toolbar-title>
          <router-link to="/" class="v-toolbar__title">{{ title }}</router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-xs-only">
          <v-btn v-if="isLoggedIn" flat :to="myAccount">
            <v-icon left>account_circle</v-icon>
            <span>My Account</span>
          </v-btn>

          <v-btn flat to="/about">
            <v-icon left>question_answer</v-icon>
            <span>About</span>
          </v-btn>

          <v-btn flat v-if="isLoggedIn" @click="logout">
            <v-icon left>power_off</v-icon>
            <span>Log Out</span>
          </v-btn>

          <v-btn v-if="!isLoggedIn" flat to="/signup">
            <v-icon left>assignment_ind</v-icon>
            <span>Sign Up</span>
          </v-btn>
          <v-btn v-if="!isLoggedIn" flat to="/login">
            <v-icon left>input</v-icon>
            <span>Log In</span>
          </v-btn>
          <v-btn to="/addSpace">
            <v-icon left>add</v-icon>
            <span>Add your space</span>
          </v-btn>
          <!--          <v-btn v-if="isLoggedIn" to="/addSpace">-->
          <!--            <v-icon left>add</v-icon>-->
          <!--            <span>Add your space</span>-->
          <!--          </v-btn>-->
          <!--          <v-btn v-else to="/login">-->
          <!--            <v-icon left>add</v-icon>-->
          <!--            <span>Add your space</span>-->
          <!--          </v-btn>-->
        </v-toolbar-items>
      </v-toolbar>
    </v-responsive>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-toolbar flat class="transparent" v-if="isLoggedIn">
        <v-list class="pa-0">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img src="https://randomuser.me/api/portraits/men/85.jpg" />
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title
                >{{ accountType }} {{ currentUser }}</v-list-tile-title
              >
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-toolbar>
      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <v-list-tile v-if="isManager" to="/mySpaces">
          <v-list-tile-action>
            <v-icon>search</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>My Workspaces</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-if="isLoggedIn" :to="myAccount">
          <v-list-tile-action>
            <v-icon>account_circle</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>My Account</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile
          v-for="item in items"
          :key="item.title"
          :to="{ path: item.route }"
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-if="!isLoggedIn" to="/login">
          <v-list-tile-action>
            <v-icon>input</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>Log in</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-if="isLoggedIn" @click="logout">
          <v-list-tile-action>
            <v-icon>power_off</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>Log out</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    currentUser: function() {
      return this.$store.getters.currentUser;
    },
    accountType: function() {
      return this.$store.getters.accountType;
    },
    isManager: function() {
      return this.accountType === "manager";
    },
    myAccount: function() {
      return `/${this.currentUser}`;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => this.$router.push("/login"));
    }
  },
  data() {
    return {
      drawer: false,
      items: [
        { title: "Home", icon: "dashboard", route: "/" },
        {
          title: "Add your space",
          icon: "add",
          route: "/addSpace"
        },
        // { title: "Search", icon: "search", route: "/search" },
        {
          title: "All Cities",
          icon: "location_city",
          route: "/cities"
        },
        {
          title: "Sign Up",
          icon: "assignment_ind",
          route: "/signup"
        }
      ]
    };
  },
  name: "ToolBar",
  props: ["title"]
};
</script>

<style scoped>
.v-toolbar__title {
  text-decoration: none;
}
</style>
