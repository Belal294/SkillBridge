// src/pages/Home.jsx
import Features from '../components/Features';
import HeroCarousel from '../components/carousel/HeroCarousel';
import Services from '../../src/Serice-Product/Product';
import DiscountSection from '../Discount/DiscountSection';
import Category from '../components/categories/Category';

const Home = () => {
  return (
    <div>
      <HeroCarousel/>
      <Features/>
      <Category/>
      <Services/>
      <DiscountSection/>
        
    </div>
  );
};

export default Home;
