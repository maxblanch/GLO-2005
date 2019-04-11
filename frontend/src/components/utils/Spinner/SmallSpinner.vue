<template>
  <CustomSpinner :size="SpinnerSize.SMALL"></CustomSpinner>
</template>

<script>
import CustomSpinner from "./CustomSpinner";
import SpinnerSize from "./spinnerSize";

export default {
  name: "SmallSpinner",
  data() {
    return {
      SpinnerSize
    };
  },
  components: { CustomSpinner }
};
</script>

<style scoped></style>
