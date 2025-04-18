import bgImg from "../../assets/Discount/banner-image-bg.jpg";

const CarouselSlide = ({ title, subtitle, image }) => {
  return (
    <section
      className="w-full h-[400px] md:h-[500px] lg:h-[600px] bg-cover bg-center flex justify-center items-center px-4 md:px-8"
      style={{ backgroundImage: `url(${bgImg})` }}
    >
      <div className="max-w-6xl w-full flex flex-col md:flex-row items-center justify-between px-4 md:px-8">
        {/* Left Content  */}
        <div className="w-full md:w-1/2 text-center md:text-left mb-8 md:mb-0">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900">
            {title}
          </h1>
          <p className="text-gray-600 my-4">{subtitle}</p>
          <button className="btn btn-secondary px-6 py-3 rounded-full shadow-md">
            Shop Product
          </button>
        </div>

        {/* Right Image  */}
        <div className="w-full md:w-1/2 flex justify-center mb-5">
          <img
            className="max-w-full md:max-w-md drop-shadow-lg"
            src={image}
            alt=""
          />
        </div>
      </div>
    </section>
  );
};

export default CarouselSlide;
