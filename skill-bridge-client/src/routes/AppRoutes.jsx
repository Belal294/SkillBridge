// // AppRoutes.jsx
// import { Routes, Route } from "react-router-dom";
// import Home from "../pages/Home";
// import MainLayout from "../layouts/MainLayout";
// import Product from "../../src/pages/services";
// import Login from "../pages/Login";
// import Register from "../pages/Register";
// import Dashboard from "../pages/Dashboard";
// import PrivateRoute from "../components/PrivateRoute";
// import ActivateAccount from "../components/Registration/ActivateAccount";

// const AppRoutes = () => {
//   return (
//     <Routes>
//       <Route element={<MainLayout />}>
//         <Route path="/" element={<Home />} />
//         {/* <Route path="about" element={<About />}/> */}
//         <Route path="/services" element={<Product />}/>
//         <Route path="login" element={<Login />} />
//         <Route path="register" element={<Register />} />
//         <Route path="activate/:uid/:token" element={<ActivateAccount />} />
//         <Route
//           path="dashboard"
//           element={
//             <PrivateRoute>
//               <Dashboard />
//             </PrivateRoute>
//           }
//         />
        
//       </Route>
//     </Routes>
//   );
// };

// export default AppRoutes;


import { Route, Routes } from "react-router";
import About from "../pages/About";
import MainLayout from "../layouts/MainLayout";
import Home from "../pages/Home";
import Shop from "../pages/services";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Dashboard from "../pages/Dashboard";
import PrivateRoute from "../components/PrivateRoute";
import ActivateAccount from "../components/Registration/ActivateAccount";

const AppRoutes = () => {
  return (
    <Routes>
      {/* <Route index element={<Home />}></Route>
      <Route path="about" element={<About />} /> */}

      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="about" element={<About />} />
        <Route path="shop" element={<Shop />} />
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="activate/:uid/:token" element={<ActivateAccount />} />
        <Route
          path="dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
      </Route>
    </Routes>
  );
};

export default AppRoutes;