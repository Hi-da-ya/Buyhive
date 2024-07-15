import React, { useState, useContext } from 'react';
import './Navbar.css';
import logo from '../Assets Folder/logo.png';
import cart_icon from '../Assets Folder/cart_icon.png';
import { Link } from 'react-router-dom';
import { ShopContext } from "../../Context/ShopContext";

const Navbar = () => {
  const [menu, setMenu] = useState('home');
  const { getTotalCartItems } = useContext(ShopContext);

  return (
    <div className='navbar'>
      <div className='nav-logo'>
        <img src={logo} alt='' />
        <p>BUYHIVE</p>
      </div>
      <ul className='nav-menu'>
        <li onClick={() => setMenu('home')}><Link style={{ textDecoration: 'none'}} to='/'>Home</Link> {menu === 'home' && <hr />}</li>
        <li onClick={() => setMenu('kids')}><Link style={{ textDecoration: 'none'}} to='/kids'>Kids</Link> {menu === 'kids' && <hr />}</li>
        <li onClick={() => setMenu('women')}><Link style={{ textDecoration: 'none'}} to='/women'>Women</Link> {menu === 'women' && <hr />}</li>
        <li onClick={() => setMenu('men')}><Link style={{ textDecoration: 'none'}} to='/men'>Men</Link> {menu === 'men' && <hr />}</li>
      </ul>
      <div className='nav-login-cart'>
        <Link to='/signup'><button>SignUp</button></Link>
        <Link to='/login'><button>Login</button></Link>
        <Link to='/cart'><img src={cart_icon} alt='' /></Link>
        <div className='nav-cart-count'>{getTotalCartItems()}</div>
      </div>
    </div>
  );
};

export default Navbar;
