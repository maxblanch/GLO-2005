<template>
  <GenericAsync :dataName="dataName" :dataSource="dataSource">
    <template slot-scope="{ data }">
      <CitiesView :cwspaces="data" />
    </template>
  </GenericAsync>
</template>

<script>
import CitiesView from "@/components/CitiesView";
import cwspaceAPI from "@/api/cwspaces";
import GenericAsync from "@/components/utils/Async/GenericAsync";

export default {
  name: "Cities",
  components: { GenericAsync, CitiesView },
  data() {
    return {
      dataSource: cwspaceAPI.getAll(),
      dataName: "coworking spaces data"
    };
  }
};
</script>

<style scoped></style>
