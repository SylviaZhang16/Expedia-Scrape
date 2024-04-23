import React from 'react';
import { useLocation } from 'react-router-dom';

function ResultsPage() {
  const location = useLocation();
  const { results } = location.state || [];
  return (
    <div className="container mx-auto mt-10">
      {results.length > 0 ? (
        results.map((hotel, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg mb-4">
            <h2 className="font-bold text-xl mb-2 px-6 py-4">{hotel.name}</h2>
            <img className="w-full" src={hotel.image_url || 'default-image.jpg'} alt={hotel.name} />
            <div className="px-6 py-4">
              <p className="text-gray-700 text-base">
                Price: {hotel.price || 'Price not available'}
              </p>
            </div>
          </div>
        ))
      ) : (
        <p className="text-center text-gray-600 text-xl">No results found</p>
      )}
    </div>
  );
}

export default ResultsPage;
