import axios from "axios";
import { apiRoot } from "@/api/constants";
import cwspaces from "../models/cwspaces";
import cwspace from "../models/cwspace";

const cwspacesRoot = `${apiRoot}/cwspaces`;
const cwspaceRoot = `${apiRoot}/cwspace`;

const getAll = () =>
  axios.get(cwspacesRoot).then(({ data }) => cwspaces.from(data));

const get = id =>
  axios.get(`${cwspaceRoot}/${id}`).then(({ data }) => cwspace.from(data));

export default {
  getAll,
  get
};
