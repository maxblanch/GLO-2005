<template>
  <GenericAsync :dataName="dataName" :dataSource="dataSource">
    <template slot-scope="{ data }">
      <CWSpaceCardView :cwspaces="data" />
    </template>
  </GenericAsync>
</template>

<script>
import CWSpaceCardView from "@/components/CWSpaceCardView";
import cwspaceAPI from "@/api/cwspaces";
import GenericAsync from "@/components/utils/Async/GenericAsync";

export default {
  name: "City",
  components: { GenericAsync, CWSpaceCardView },
  data() {
    return {
      dataSource: cwspaceAPI.getByCity(this.$route.params.city),
      dataName: "coworking spaces in city"
    };
  }
};
</script>

<style scoped></style>
