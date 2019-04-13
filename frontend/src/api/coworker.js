import axios from "axios";
import { apiRoot } from "@/api/constants";
import coworker from "../models/coworker";

const coworkerRoot = `${apiRoot}/coworker`;

const get = id =>
  axios.get(`${coworkerRoot}/${id}`).then(({ data }) => coworker.from(data));

export default {
  get
};
