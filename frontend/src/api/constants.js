export const apiRoot = "http://localhost:5000";

export const Headers = {
  Authorization: `Bearer ${localStorage.getItem("token")}`,
  "Content-Type": "application/json"
};
