<template>
  <CustomSpinner :size="SpinnerSize.LARGE"></CustomSpinner>
</template>

<script>
import CustomSpinner from "./CustomSpinner";
import SpinnerSize from "./spinnerSize";

export default {
  name: "LargeSpinner",
  data() {
    return { SpinnerSize };
  },
  components: { CustomSpinner }
};
</script>

<style scoped></style>
