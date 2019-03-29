<template>
  <nav>
    <v-responsive>
      <v-toolbar>
        <v-toolbar-side-icon
          @click.stop="drawer = !drawer"
          class="hidden-sm-and-up"
        ></v-toolbar-side-icon>
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-xs-only">
          <v-btn flat>
            <v-icon left>question_answer</v-icon>
            <span>About</span>
          </v-btn>
          <v-btn flat>
            <v-icon left>assignment_ind</v-icon>
            <span>Sign Up</span>
          </v-btn>
          <v-btn flat>
            <v-icon left>input</v-icon>
            <span>Log In</span>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
    </v-responsive>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <v-list-tile v-for="item in items" :key="item.title" @click="">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      items: [
        { title: "Home", icon: "dashboard" },
        { title: "Search", icon: "search" },
        { title: "All Cities", icon: "location_city" },
        { title: "Sign Up", icon: "assignment_ind" },
        { title: "Log In", icon: "input" }
      ]
    };
  },
  name: "ToolBarVue",
  props: {
    title: String
  }
};
</script>

<style scoped></style>
