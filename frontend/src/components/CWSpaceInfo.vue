<template>
  <v-layout>
    <v-container>
      <v-layout justify-center>
        <div>
          <img :src="cwspace.imageUrl" alt="iorem" />
          <h1 class="white--text">
            {{ manager.username }}'s {{ cwspace.name }}
          </h1>
          <p class="white--text">
            {{ cwspace.address }}, {{ cwspace.city }}, {{ cwspace.state }},
            {{ cwspace.country }}
          </p>
          <h3 class="white--text">{{ cwspace.description }}</h3>

          <v-data-table
            :headers="headers"
            :items="options"
            class="elevation-1"
            hide-actions
          >
            <template v-slot:items="props">
              <td>{{ props.item.num }}</td>
              <td>{{ props.item.duration }}</td>
              <td>{{ props.item.price }}</td>
              <!--              <td>-->
              <!--                <v-btn class="primary white&#45;&#45;text">Reserve</v-btn>-->
              <!--              </td>-->
            </template>
          </v-data-table>
        </div>
      </v-layout>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  name: "CWSpaceInfo",
  props: ["cwspace", "manager"],
  data() {
    return {
      headers: [
        { text: "# PEOPLE", value: "num" },
        { text: "DURATION", value: "duration" },
        { text: "PRICE", value: "price" }
        // { text: "AVAILABILITY" }
      ],
      options: [
        {
          num: 1,
          duration: "1 Day",
          price: `${this.cwspace.currency} ${this.cwspace.dayPrice}`
        },
        {
          num: 1,
          duration: "1 Week",
          price: `${this.cwspace.currency} ${this.cwspace.weekPrice}`
        },
        {
          num: 1,
          duration: "1 Month",
          price: `${this.cwspace.currency} ${this.cwspace.monthPrice}`
        }
      ]
    };
  }
};
</script>

<style scoped></style>
