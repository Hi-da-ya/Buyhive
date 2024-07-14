
import './App.css';
import Navbar from './components/Navbar/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import Cart from './Pages/Cart';
import Product from './Pages/Product';
import Footer from './components/Footer/Footer';
import Kids from './Pages/Kids';
import Men from './Pages/Men';
import Women from './Pages/Women';
import ShopContextProvider from './Context/ShopContext'; // Ensure to import ShopContextProvider
import Login from './components/Login/Login';
import Signup from './components/Login/Signup'

import LoginSignup from './components/Login/LoginSignup';
import ContactUs from './Pages/Contactus';
import AboutUs from './Pages/Aboutus';
import PrivacyPolicy from './Pages/Privacypolicy';
import TermsAndConditions from './Pages/Term';

function App() {
  const categoryone = 'Women';
  const categorytwo = 'Men';
  const categorythree = 'Kids';
  
  return (
    <ShopContextProvider> {/* Wrap entire application with ShopContextProvider */}
      <div>
        <BrowserRouter>
          <Navbar />
          <Routes>
            {/* Home route */}
            <Route path='/' element={<Home />} />

            {/* Category routes */}
            <Route path='/kids' element={<Kids category={categorythree} />} />
            <Route path='/women' element={<Women category={categoryone} />} />
            <Route path='/men' element={<Men category={categorytwo} />} />

            {/* Product details route */}
            <Route path='/product/:productId' element={<Product />} />

            {/* Cart route */}
            <Route path='/cart' element={<Cart />} />

            {/* Authentication routes */}
            {/* <Route path='/signup' element={<Signup />} /> */}
            <Route path='/login' element={<Login />} /> 
            <Route path='/signup' element={<Signup />} /> 

            <Route path='/contact' element={<ContactUs />} /> 
            <Route path='/about' element={<AboutUs />} />  
            <Route path='/privacy-policy' element={<PrivacyPolicy />} />
            <Route path='/terms-conditions' element={<TermsAndConditions />} /> 
          </Routes>
          <Footer />
        </BrowserRouter>
      </div>
    </ShopContextProvider>
  );
}

export default App;
