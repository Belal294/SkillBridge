import axios from "axios";

export default axios.create({
  baseURL: "https://skill-bridge-tau.vercel.app/api/v1",
});