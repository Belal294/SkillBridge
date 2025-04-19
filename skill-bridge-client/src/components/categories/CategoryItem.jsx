import { FaAngleRight } from "react-icons/fa6";

const CategoryItems = ({ index, category }) => {
  const gradients = [
    "from-pink-100 to-blue-100",
    "from-blue-100 to-purple-100",
    "from-purple-100 to-pink-100",
    "from-pink-100 to-blue-100",
  ];

  const gradient = gradients[index % gradients.length];
  const firstLetter = category?.name?.charAt(0)?.toUpperCase() || "C";
  const itemCount = category?.service_count ?? 0;
  const name = category?.name || "Untitled";
  // const description =
  //   category?.description || "No description available for this category.";

  return (
    <div
      className={`rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow duration-300 cursor-pointer bg-gradient-to-br ${gradient}`}
    >
      <div className="p-6 flex flex-col h-full">
        {/* Icon & Count */}
        <div className="flex justify-between items-start mb-4">
          <div className="h-10 w-10 rounded-full bg-pink-500 text-white flex items-center justify-center font-bold text-xl">
            {firstLetter}
          </div>
          <span className="text-sm text-gray-600 bg-white/70 px-2 py-1 rounded-full">
            {itemCount} {itemCount === 1 ? "Item" : "Items"}
          </span>
        </div>

        {/* Name */}
        <h3 className="text-xl font-bold mb-2">{name}</h3>

        {/* Description */}
        <p className="text-gray-600 text-sm mb-4 flex-grow">
          {/* {description} */}
        </p>

        {/* Button */}
        <button className="text-pink-500 font-bold hover:text-pink-600 transition-colors flex items-center gap-1 mt-auto">
          Explore
          <FaAngleRight />
        </button>
      </div>
    </div>
  );
};

export default CategoryItems;
