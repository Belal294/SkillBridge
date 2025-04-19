import { useEffect, useState } from "react";
import apiClient from "../../services/api-client";
import CategoryItems from "./CategoryItem";

const Category = () => {
  const [categories, setCategories] = useState([]);
  
  useEffect(() => {
    apiClient.get("/categories").then((res) => {
      console.log("API response:", res.data);
  
      const fetchedCategories = res.data?.results || [];
      setCategories(fetchedCategories);
    }).catch((err) => {
      console.error("Error fetching categories:", err);
    });
  }, []);
  
  
  return (
    <section className="py-12 px-4 max-w-7xl mx-auto">
      {/* Heading */}
      <div className="flex justify-between items-center mb-8">
        <h2 className="text-3xl font-bold">Browse Categories</h2>
        <a
          href="#"
          className="btn btn-secondary px-6 py-3 rounded-full text-lg"
        >
          View All
        </a>
      </div>

      {/* Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {categories.length > 0 ? (
          categories.map((category, index) => (
            <CategoryItems key={category.id} index={index} category={category} />
          ))
        ) : (
          <p className="col-span-full text-center text-gray-500">
            No categories found.
          </p>
        )}

      </div>
    </section>
  );
};

export default Category;
