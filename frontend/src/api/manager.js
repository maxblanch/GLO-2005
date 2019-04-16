import axios from "axios";
import { apiRoot } from "@/api/constants";
import manager from "../models/manager";

const managerRoot = `${apiRoot}/manager`;

const get = id =>
  axios.get(`${managerRoot}/${id}`).then(({ data }) => manager.from(data));

export default {
  get
};
