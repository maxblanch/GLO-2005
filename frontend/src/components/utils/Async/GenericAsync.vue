<template>
  <AsyncContent :dataName="dataName" :requestState="requestState">
    <slot :data="data"></slot>
  </AsyncContent>
</template>

<script>
import RequestState from "./requestState";
import AsyncContent from "./AsyncContent";
import isEmpty from "../../../utils/isEmpty";

export default {
  name: "GenericAsync",
  props: ["dataSource", "dataName", "allowEmpty"],
  data() {
    return {
      requestState: RequestState.LOADING,
      data: null
    };
  },
  methods: {
    setData(data) {
      if (!this.allowEmpty && isEmpty(data)) {
        this.setError(data);
        return;
      }
      this.data = data;
      this.requestState = RequestState.LOADED;
    },
    setError(_err) {
      this.requestState = RequestState.ERROR;
    }
  },
  mounted() {
    this.dataSource.then(this.setData).catch(this.setError);
  },
  components: {
    AsyncContent
  }
};
</script>

<style scoped></style>
