// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

// import required modules
import { Autoplay, Pagination, Navigation } from "swiper/modules";
import CarouselSlide from "./CarouselSlide";
import book from "../../assets/carosel/carosel1.jpg";
import fashion from "../../assets/carosel/carosel2.jpg";
import technology from "../../assets/carosel/carousel3.jpg";

const HeroCarousel = () => {
  const slides = [
    {
      title: "Find Talent and Work in One Platform",
      subtitle: "Discount available. Grab it now!",
      image: book,
    },
    {
      title: "Skill-Based Freelancing Marketplace for Everyone",
      subtitle: "A specialists label creating luxury essentials!",
      image: fashion,
    },
    {
      title: "Connect Skilled Freelancers with Real Projects",
      subtitle: "Explore a range of devices for seamless living.",
      image: technology,
    },
  ];

  return (
    <>
      <Swiper
        autoplay={{
          delay: 3000,
          disableOnInteraction: false,
        }}
        pagination={{
          clickable: true,
        }}
        navigation={false}
        modules={[Autoplay, Pagination, Navigation]}
        className="mySwiper"
      >
        {slides.map((slide, index) => (
          <SwiperSlide key={index}>
            <CarouselSlide
              title={slide.title}
              subtitle={slide.subtitle}
              image={slide.image}
            />

          </SwiperSlide>
        ))}
      </Swiper>
    </>
  );
};

export default HeroCarousel;