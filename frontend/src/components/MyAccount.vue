<template>
  <div>
    <AsyncContent :request-state="requestState" dataName="user info">
      <MyAccountView :currentUser="currentUser" />
    </AsyncContent>
  </div>
</template>
<script>
import userAPI from "@/api/user";
import MyAccountView from "@/components/MyAccountView";
import AsyncContent from "@/components/utils/Async/AsyncContent";
import RequestState from "@/components/utils/Async/requestState";

export default {
  name: "MyAccount",
  computed: {
    userId: function() {
      return this.$store.getters.userId;
    },
    accountType: function() {
      return this.$store.getters.accountType;
    }
  },
  components: { AsyncContent, MyAccountView },
  data() {
    return {
      currentUser: {},
      requestState: RequestState.LOADING
    };
  },
  mounted() {
    if (this.$store.getters.accountType === "manager")
      userAPI
        .getManager(this.$store.getters.userId)
        .then(this.setCurrentUser)
        .catch(this.setError);
    // .catch(({ response }) => console.log(response.data.message));
    else {
      userAPI
        .getCoworker(this.$store.getters.userId)
        .then(this.setCurrentUser)
        .catch(this.setError);
      // .catch(({ response }) => console.log(response.data.message));
    }
  },
  methods: {
    setCurrentUser(currentUser) {
      this.currentUser = currentUser;
      this.requestState = RequestState.LOADED;
    },
    setError(_err) {
      this.requestState = RequestState.ERROR;
    }
  }

  // data() {
  //   return {
  //     currentUser: {}
  //   };
  // },
  // mounted() {
  //   switch (this.accountType) {
  //     case "manager":
  //       ManagerAPI.get(this.$store.getters.userId)
  //         .then(res => console.log(res))
  //         .catch(({ response }) => console.log(response.data.message));
  //       break;
  //
  //     case "coworker":
  //       CoworkerAPI.get(this.$store.getters.userId)
  //         .then(res => console.log(res))
  //         .catch(({ response }) => console.log(response.data.message));
  //       break;
  //   }
  // }
};
</script>

<style scoped></style>
