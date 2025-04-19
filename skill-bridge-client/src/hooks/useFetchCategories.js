import { useEffect, useState } from "react";
import apiClient from "../services/api-client";

const useFetchCategories = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const res = await apiClient.get("/categories");

        const data = Array.isArray(res.data)
          ? res.data
          : res.data.results || [];

        setCategories(data);
      } catch (error) {
        console.error("Failed to fetch categories:", error);
        setCategories([]); 
      }
    };

    fetchCategories();
  }, []);

  return categories;
};

export default useFetchCategories;
