import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';  

function SearchPage() {
  const navigate = useNavigate();  
  const [destination, setDestination] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!destination || !startDate || !endDate) {
      setError('Please fill in all fields');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ destination, start_date: startDate, end_date: endDate }),
      });
      const data = await response.json();
      if (response.ok) {
        navigate('/results', { state: { results: data } });
      } else {
        throw new Error('Something went wrong with the search');
      }
    } catch (error) {
      console.error(error);
      alert('Failed to fetch results');
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10">
      <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="destination">
            Destination:
          </label>
          <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="destination" type="text" value={destination} onChange={(e) => setDestination(e.target.value)} />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="start-date">
            Start Date:
          </label>
          <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="start-date" type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="end-date">
            End Date:
          </label>
          <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="end-date" type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </div>
        {error && <p className="text-red-500">{error}</p>}
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
          Search
        </button>
      </form>
    </div>
  );
}

export default SearchPage;
