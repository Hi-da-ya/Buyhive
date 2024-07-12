import React from 'react';
import './Footer.css';
import footer_logo from '../Assets Folder/logo_big.png';
import instagram_icon from '../Assets Folder/instagram_icon.png';
import whatsapp_icon from '../Assets Folder/whatsapp_icon.png';

const Footer = () => {
  return (
    <div className='footer'>
      <div className='footer-logo'>
        <img src={footer_logo} alt='' />
        <p>BUYHIVE</p>
      </div>
      <ul className='footer-links'>
        <li>About Us</li>
        <li>Contact Us</li>
        <li>Privacy Policy</li>
        <li>Terms & Conditions</li>
      </ul>
      <div className='footer-social-icons'>
        <div className='footer-icons-container'>
          <img src={instagram_icon} alt='Instagram' />
        </div>
        <div className='footer-icons-container'>
          <img src={whatsapp_icon} alt='WhatsApp' />
        </div>
      </div>
      <div className='footer-copyright'>
        <hr />
        <p>Copyright @ 2024 - All Rights Reserved</p>
      </div>
    </div>
  );
};

export default Footer;
