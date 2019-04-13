import axios from "axios";
import { apiRoot } from "@/api/constants";
import cwspaces from "../models/cwspaces";
import cwspace from "../models/cwspace";
import reviews from "../models/reviews";

const cwspacesRoot = `${apiRoot}/cwspaces`;
const cwspaceRoot = `${apiRoot}/cwspace`;
const reviewsRoot = `${apiRoot}/reviews`;
const cityRoot = `${cwspacesRoot}/city`;

const getAll = () =>
  axios.get(cwspacesRoot).then(({ data }) => cwspaces.from(data));

const getByCity = city =>
  axios.get(`${cityRoot}/${city}`).then(({ data }) => cwspaces.from(data));

const get = cwsId =>
  axios.get(`${cwspaceRoot}/${cwsId}`).then(({ data }) => cwspace.from(data));

const getReviews = cwsId =>
  axios.get(`${reviewsRoot}/${cwsId}`).then(({ data }) => reviews.from(data));

const search = query =>
  axios.get(`${cwspacesRoot}/${query}`).then(({ data }) => cwspaces.from(data));

export default {
  getAll,
  getByCity,
  get,
  getReviews,
  search
};
