import ManagerAPI from "./manager";
import CoworkerAPI from "./coworker";

const getManager = id => ManagerAPI.get(id);

const getCoworker = id => CoworkerAPI.get(id);

// const get = (id, type) => {
//   switch (type) {
//     case "manager":
//       return getManager(id)
//         .then(res => console.log(res))
//         .catch(({ response }) => console.log(response.data.message));
//
//     case "coworker":
//       return getCoworker(id)
//         .then(res => console.log(res))
//         .catch(({ response }) => console.log(response.data.message));
//   }
// };

export default {
  getManager,
  getCoworker
  // get
};
