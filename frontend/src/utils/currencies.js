import axios from "axios";

function get() {
  let array = [];
  axios
    .get("https://openexchangerates.org/api/currencies.json")
    .then(({ data }) => {
      let keys = Object.keys(data);
      keys.forEach(key => array.push(`${key} - ${data[key]}`));
    });
  return array;
}

export default {
  get
};
