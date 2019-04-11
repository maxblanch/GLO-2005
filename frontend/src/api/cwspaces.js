import axios from "axios";
import { apiRoot } from "@/api/constants";
import cwspaces from "../models/cwspaces";

const cwspacesRoot = `${apiRoot}/cwspaces`;

const getCwSpaces = () =>
  axios.get(cwspacesRoot).then(({ data }) => cwspaces.from(data));

export default {
  getCwSpaces
};
