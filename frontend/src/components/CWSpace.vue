<template>
  <div>
    <AsyncContent :request-state="requestState" dataName="cwspace info">
      <CWSpaceView :cwspace="cwspace" />
    </AsyncContent>
  </div>
</template>

<script>
import RequestState from "@/components/utils/Async/requestState";
import cwspaceAPI from "@/api/cwspaces";
import AsyncContent from "@/components/utils/Async/AsyncContent";
import CWSpaceView from "@/components/CWSpaceView";

export default {
  name: "CWSpace",
  components: { CWSpaceView, AsyncContent },
  data() {
    return {
      id: this.$route.params.id,
      cwspace: {},
      requestState: RequestState.LOADING
    };
  },
  mounted() {
    cwspaceAPI
      .get(this.id)
      .then(this.setCWSpace)
      .catch(this.setError);
  },
  methods: {
    setCWSpace(cwspace) {
      this.cwspace = cwspace;
      this.requestState = RequestState.LOADED;
    },
    setError(_err) {
      this.requestState = RequestState.ERROR;
    }
  }
};
</script>

<style scoped></style>
