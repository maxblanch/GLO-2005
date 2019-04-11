<template>
  <div>
    <section class="section" v-if="requestState === RequestState.LOADING">
      <LargeSpinner />
    </section>

    <div v-if="requestState === RequestState.LOADED">
      <slot></slot>
    </div>

    <section class="section" v-if="requestState === RequestState.ERROR">
      <ErrorMessage :message="error" />
    </section>
  </div>
</template>

<script>
import ErrorMessage from "@/components/utils/ErrorMessage";
import RequestState from "./requestState";
import LargeSpinner from "../Spinner/LargeSpinner";

export default {
  name: "AsyncContent",
  props: ["requestState", "dataName"],
  data() {
    return {
      RequestState,
      LargeSpinner,
      error: `Unable to fetch ${this.dataName} at this time.`
    };
  },
  components: {
    LargeSpinner,
    ErrorMessage
  }
};
</script>

<style scoped></style>
