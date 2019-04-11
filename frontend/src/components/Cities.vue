<template>
  <CitiesView />
</template>

<script>
import CitiesView from "@/components/CitiesView";
import cwspaceAPI from "@/api/cwspaces";

export default {
  name: "Cities",
  components: { CitiesView },
  data() {
    return {
      cwspaces: cwspaceAPI.getCwSpaces()
    };
  }
};
</script>

<style scoped></style>
