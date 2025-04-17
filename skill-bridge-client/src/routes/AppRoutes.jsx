// AppRoutes.jsx
import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import MainLayout from "../layouts/MainLayout";
import ShopPage from "../components/Services/ShopPage";
import Services from "../../src/pages/services"

const AppRoutes = () => {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        {/* <Route path="about" element={<About />}/> */}
        <Route path="/services" element={<Services />}/>
        
      </Route>
    </Routes>
  );
};

export default AppRoutes;
