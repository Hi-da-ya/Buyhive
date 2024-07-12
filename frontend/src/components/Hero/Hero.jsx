import React from 'react'
import './Hero.css'
import arrow_hand from '../Assets Folder/arrow.png'

const Hero = () => {
  return (
    <div className='hero'>
        <div className='hero-left'>
            <h2>BEST SELLERS</h2>
            <div>
                <div className='hero-hand-icon'>
                    <p>New</p>
                    
                </div>
                <p>Collections</p>
                <p>Something for Everyone</p>
            </div>
            <div className='hero-shop-btn'>
                <div>Shop Now</div>
                <img src={arrow_hand} alt='' />
            </div>
        </div>
        <div className='hero-right'>
            
        </div>

    </div>
  )
}

export default Hero