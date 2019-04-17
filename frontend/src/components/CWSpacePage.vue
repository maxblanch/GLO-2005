<template>
  <div>
    <AsyncContent :request-state="requestState" dataName="cwspace info">
      <CWSpaceInfo :cwspace="cwspace" :manager="manager" />
    </AsyncContent>
    <AsyncContent :request-state="requestState" dataName="reviews info">
      <Reviews
        :reviews="reviews"
        :manager="manager"
        @replyposted="handleNewReplyPosted"
      />
    </AsyncContent>
    <AsyncContent :request-state="requestState" dataName="cwspace info">
      <WriteReview
        @reviewposted="handleNewReviewPosted"
        :cwsId="cwspace.cwsId"
      />
    </AsyncContent>
  </div>
</template>

<script>
import RequestState from "@/components/utils/Async/requestState";
import cwspaceAPI from "@/api/cwspaces";
import ManagerAPI from "@/api/manager";
import AsyncContent from "@/components/utils/Async/AsyncContent";
import CWSpaceInfo from "@/components/CWSpaceInfo";
import Reviews from "@/components/Reviews";
import WriteReview from "./WriteReview";

export default {
  name: "CWSpace",
  components: { WriteReview, Reviews, CWSpaceInfo, AsyncContent },
  data() {
    return {
      id: this.$route.params.id,
      cwspace: {},
      reviews: {},
      manager: {},
      requestState: RequestState.LOADING
    };
  },
  mounted() {
    cwspaceAPI
      .get(this.id)
      .then(this.setCWSpace)
      .catch(this.setError);
    cwspaceAPI
      .getReviews(this.id)
      .then(this.setReviews)
      .catch(this.setReviewError);
  },
  methods: {
    setCWSpace(cwspace) {
      this.cwspace = cwspace;
      ManagerAPI.get(cwspace.managerId).then(this.setManager);
      this.requestState = RequestState.LOADED;
    },
    setReviews(reviews) {
      this.reviews = reviews;
      this.requestState = RequestState.LOADED;
    },
    setManager(manager) {
      this.manager = manager;
      this.requestState = RequestState.LOADED;
    },
    setError(_err) {
      this.requestState = RequestState.ERROR;
    },
    setReviewError(_err) {
      console.log(_err.response.data.message);
      this.reviews = { Error: true, errorMessage: _err.response.data.message };
    },
    handleNewReviewPosted(eventData) {
      cwspaceAPI
        .getReviews(eventData.cws_id)
        .then(this.setReviews)
        .catch(this.setReviewError);
    },
    handleNewReplyPosted(eventData) {
      alert(eventData.message);

      cwspaceAPI
        .getReviews(this.id)
        .then(this.setReviews)
        .catch(this.setReviewError);
    }
  }
};
</script>

<style scoped></style>
