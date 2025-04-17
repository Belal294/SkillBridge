import axios from "axios";

export default axios.create({
  baseURL: "https://skill-bridge-phi.vercel.app/api/v1",
});