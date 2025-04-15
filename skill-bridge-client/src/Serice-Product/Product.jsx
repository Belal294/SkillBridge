import { useEffect, useState } from "react";
import ServiceItem from "./ProductItem";
import { Navigation } from "swiper/modules";
import { SwiperSlide, Swiper } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import ErroAlert from "../components/ErrorAlert";
import apiClient from "../services/api-client";

const Product = () => {
  const [services, setServices] = useState([]);
  const [isLoading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const isValidArray = (arr) => Array.isArray(arr) && arr.length > 0;

  useEffect(() => {
    setLoading(true);
    apiClient
      .get("/services/")
      .then((res) => {
        console.log("📦 API Full Response:", res.data);

        //  Handle both paginated and non-paginated responses
        if (Array.isArray(res.data)) {
          setServices(res.data);
        } else if (Array.isArray(res.data.results)) {
          setServices(res.data.results);
        } else {
          setServices([]);
        }
      })
      .catch((err) => {
        console.error("❌ Error fetching services:", err);
        setError(err.message);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <section className="mx-auto py-16 bg-gray-50">
      <div className="flex justify-between items-center px-4 md:px-8 mb-4">
        <h2 className="text-3xl md:text-4xl font-bold">Trending Products</h2>
        <a href="#" className="btn btn-secondary px-6 py-6 rounded-full text-lg">
          View All
        </a>
      </div>

      {isLoading && (
        <div className="flex justify-center items-center py-10">
          <span className="loading loading-spinner loading-xl text-secondary"></span>
        </div>
      )}

      {error && <ErroAlert error={error} />}

      {!isLoading && !error && isValidArray(services) && (
        <Swiper
          modules={[Navigation]}
          spaceBetween={10}
          slidesPerView={1}
          breakpoints={{
            640: { slidesPerView: 2 },
            1024: { slidesPerView: 3 },
          }}
          navigation
          className="mt-4 px-4 container"
        >
          {services.map((service) => (
            <SwiperSlide key={service.id}>
              <ServiceItem service={service} />
            </SwiperSlide>
          ))}
        </Swiper>
      )}

      {!isLoading && !error && !isValidArray(services) && (
        <p className="text-center text-gray-500 mt-6">No Products Available</p>
      )}
    </section>
  );
};

export default Product;
