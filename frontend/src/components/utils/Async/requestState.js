const RequestState = Object.freeze({
  LOADING: Symbol("loading"),
  LOADED: Symbol("loaded"),
  ERROR: Symbol("error")
});

export default RequestState;
