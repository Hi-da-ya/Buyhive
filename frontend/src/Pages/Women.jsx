import React, { useEffect, useState } from 'react';
import ProductModal from './ProductModal'; // Assuming your ProductModal component is in the same directory

const Women = ({ categoryone }) => {
  const [products, setProducts] = useState([]);
  const [selectedProductId, setSelectedProductId] = useState(null); // State for the selected product ID
  const [isModalOpen, setIsModalOpen] = useState(false); // State to manage modal open/close

  useEffect(() => {
    fetch("http://127.0.0.1:5555/categories/1") // Adjust the endpoint to match your API
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch');
        }
        return response.json();
      })
      .then(data => {
        if (data.length > 0 && data[0].products) {
          setProducts(data[0].products); // Set products from the first category (assuming the response array contains categories)
        } else {
          console.error('No products found in response:', data);
        }
      })
      .catch(error => console.error('Error fetching products:', error));
  }, [categoryone]);

  const openModal = (productId) => {
    setSelectedProductId(productId); 
    setIsModalOpen(true); 
  };

  const closeModal = () => {
    setIsModalOpen(false); 
    setSelectedProductId(null); 
  };

  return (
    <div className="bg-white">
      <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
        <h2 className="text-2xl font-bold tracking-tight text-gray-900">{categoryone} Women's collection</h2>

        <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          {products.map((product) => (
            <div key={product.id} className="group relative">
              <div className="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
                <img
                  alt={product.imageAlt}
                  src={product.image_url}
                  className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                />
              </div>
              <div className="mt-4 flex justify-between">
                <div>
                  <h3 className="text-sm text-gray-700">
                    {product.name}
                  </h3>
                </div>
                <p className="text-sm font-medium text-gray-900">ksh{product.price}</p>
              </div>
              <button onClick={() => openModal(product.id)} className="mt-2 text-sm font-medium text-indigo-600 hover:text-indigo-500">
                View
              </button>
            </div>
          ))}
        </div>
      </div>

      <ProductModal
        productId={selectedProductId} // Pass the selected product ID to the modal
        isOpen={isModalOpen} // Pass the modal open state
        onClose={closeModal} // Pass the close modal function
      />
    </div>
  );
}

export default Women;