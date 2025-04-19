// import defaultImage from "../assets/carosel/defalut.jpg";

// const ServiceItem = ({ service }) => {
//   if (!service) {
//     // console.log("service is Undefined")
//     return null; 
//   }

//   const imageUrl =
//     service?.images?.length > 0 ? service.images[0].image : defaultImage;

//   const title = service?.title || "Untitled";
//   const price = service?.price ?? "Price not available"; 
//   const description = service?.description || "No description available."; 

//   return (
//     <div className="card bg-base-100 w-96 shadow-sm">
//       <figure className="px-10 pt-10">
//         <img src={imageUrl} alt="Service" className="rounded-xl" />
//       </figure>
//       <div className="card-body items-center text-center">
//         <h2 className="card-title">{title}</h2> 
//         <h3 className="font-bold text-xl text-red-700">${price}</h3> 
//         <p>{description}</p> 
//         <div className="card-actions mt-1">
//           <button className="btn btn-secondary">Buy Now</button>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default ServiceItem;



import defaultImage from "../../src/assets/carosel/defalut.jpg";

const ProductItem = ({ product }) => {
  return (
    <div className="card bg-base-100 w-96 shadow-sm">
      <figure className="px-10 pt-10">
        <img
          src={
            product.images.length > 0 ? product.images[0].image : defaultImage
          }
          alt="Shoes"
          className="rounded-xl"
        />
      </figure>
      <div className="card-body items-center text-center">
        <h2 className="card-title">{product.title}</h2>
        <h3 className="font-bold text-xl text-red-700">${product.price}</h3>
        <p>{product.description}</p>
        <div className="card-actions mt-1">
          <button className="btn btn-secondary">Buy Now</button>
        </div>
      </div>
    </div>
  );
};

export default ProductItem;