import React from 'react';
import { useLocation } from 'react-router-dom';

function ResultsPage() {
  const location = useLocation();
  const { results, isLoading } = location.state || { results: [], isLoading: true };

  if (isLoading) {
    return <div className="text-center mt-20 text-xl text-gray-500">Loading...</div>;
  }

  return (
    <div className="container mx-auto mt-10">
      <h1 className="text-2xl font-bold mb-6 text-center">
        Displaying {results.length} Results
      </h1>
      <div className="flex flex-wrap justify-center gap-4">
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
    </div>
  );
}

export default ResultsPage;
