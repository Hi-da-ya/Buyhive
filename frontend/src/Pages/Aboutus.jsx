import React from 'react'

function AboutUs() {
  return (
    <div className="container mx-auto p-8 bg-gradient-to-b from-gray-100 to-gray-200">
      <div className="text-center mb-12">
        <h1 className="text-5xl font-bold text-gray-800 mb-4">About Us</h1>
        <p className="text-xl text-gray-600">Welcome to Buy Hive, your go-to online clothing store.</p>
      </div>

      <div className="flex flex-wrap items-center mb-12">
        <div className="w-full md:w-1/2 p-8 bg-white rounded-lg shadow-lg">
          <img src="https://img.freepik.com/free-photo/portrait-person-owning-managing-their-own-business_23-2151456971.jpg?semt=ais_user_ai_gen" alt="Vision" className="h-auto rounded-lg mb-4" />
          <h2 className="text-3xl font-semibold text-gray-800 mb-4">Our Vision</h2>
          <p className="text-gray-700 leading-relaxed">
            At Buy Hive, we aim to revolutionize the fashion industry by providing high-quality, stylish clothing that is accessible to everyone. We believe in sustainability, inclusivity, and innovation.
          </p>
        </div>
        
        <div className="w-full md:w-1/2 p-8 bg-white rounded-lg shadow-lg mt-6 md:mt-0">
          <img src='https://img.freepik.com/free-photo/abstract-store-with-futuristic-concept-architecture_23-2150861876.jpg?semt=ais_user_ai_gen' alt="Mission" className="h-auto rounded-lg mb-4" />
          <h2 className="text-3xl font-semibold text-gray-800 mb-4">Our Mission</h2>
          <p className="text-gray-700 leading-relaxed">
            Our mission is to offer a diverse range of clothing that caters to all styles and preferences while maintaining a commitment to sustainability and ethical practices. We strive to create a seamless and enjoyable shopping experience for our customers.
          </p>
        </div>
      </div>

      <div className="bg-white p-8 rounded-lg shadow-lg">
        <h2 className="text-3xl font-semibold text-gray-800 mb-4">Testimonials</h2>
        <div className="space-y-8">
          <div className="bg-gradient-to-r from-teal-100 to-teal-200 p-6 rounded-lg shadow-md">
            <p className="text-gray-700 leading-relaxed">
              "Buy Hive has completely transformed my wardrobe! The quality and style of their clothing are unmatched."
            </p>
            <p className="text-right text-teal-600 mt-4">- Alex M.</p>
          </div>
          <div className="bg-gradient-to-r from-purple-100 to-purple-200 p-6 rounded-lg shadow-md">
            <p className="text-gray-700 leading-relaxed">
              "I love the variety and the sustainable practices that Buy Hive stands for. I always find something I love."
            </p>
            <p className="text-right text-purple-600 mt-4">- Jamie S.</p>
          </div>
          <div className="bg-gradient-to-r from-pink-100 to-pink-200 p-6 rounded-lg shadow-md">
            <p className="text-gray-700 leading-relaxed">
              "The customer service is fantastic, and the clothing is even better in person. Highly recommend Buy Hive!"
            </p>
            <p className="text-right text-pink-600 mt-4">- Taylor R.</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default AboutUs