import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const Men = ({ categorythree }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/categories/2") // Adjust the endpoint to match your API
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
  }, [categorythree]);

  return (
    <div>
      <h1>{categorythree} Products</h1>
      <div>
        {products.map(product => (
          <div key={product.id}>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>${product.price}</p>
            <p><img src={product.image_url} alt={product.name} /></p>
            {/* Example Link usage */}
            {/* <Link to={/product/${product.id}}>View Details</Link> */}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Men;