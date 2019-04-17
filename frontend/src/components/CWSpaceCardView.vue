<template>
  <div style="margin: auto">
    <v-card>
      <v-container fluid grid-list-lg style="max-width: 80%; ">
        <v-layout row wrap>
          <v-flex xs12 v-for="cwspace in cwspaces" v-if="cwspace">
            <v-card class="white--text elevation-10 grey darken-3 cwspace-card">
              <v-layout @click="goToSpace(cwspace.cwsId)">
                <v-flex xs5>
                  <v-img
                    :src="cwspace.imageUrl"
                    height="125px"
                    contain
                    :alt="cwspace.name"
                  ></v-img>
                </v-flex>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">{{ cwspace.name }}</div>
                      <div class="subheading">{{ cwspace.rating }} ⭐️</div>
                      <div>
                        <v-icon left>location_on</v-icon>
                        <span>
                          {{ cwspace.address }}, {{ cwspace.city }},
                          {{ cwspace.state }},{{ cwspace.country }}</span
                        >
                      </div>
                      <div>{{ cwspace.description }}</div>
                    </div>
                  </v-card-title>
                </v-flex>
              </v-layout>
              <v-divider light></v-divider>
              <!--              <v-card-actions class="pa-3">-->
              <!--                Rate this space-->
              <!--                <v-spacer></v-spacer>-->

              <!--                <v-icon>star_border</v-icon>-->
              <!--                <v-icon>star_border</v-icon>-->
              <!--                <v-icon>star_border</v-icon>-->
              <!--                <v-icon>star_border</v-icon>-->
              <!--                <v-icon>star_border</v-icon>-->
              <!--              </v-card-actions>-->
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "CWSpaceCardView",
  props: ["cwspaces"],
  methods: {
    goToSpace(id) {
      this.$router.push(`/cwspace/${id}`);
    }
  }
};
</script>

<style scoped>
.cwspace-card {
  cursor: pointer;
}
</style>
