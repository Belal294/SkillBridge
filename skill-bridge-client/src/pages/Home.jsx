// src/pages/Home.jsx
import Features from '../components/Features';
import HeroCarousel from '../components/carousel/HeroCarousel';
import Services from '../../src/Serice-Product/Product';


const Home = () => {
  return (
    <div>
      <HeroCarousel/>
      <Features/>
      <Services/>
        
    </div>
  );
};

export default Home;
