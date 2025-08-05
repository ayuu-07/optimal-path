import { useState } from 'react';

const InputForm = ({ onSubmit, isLoading }) => {
  const [data, setData] = useState({
    total_area_sqft: 1200,
    num_floors: 2,
    num_bedrooms: 3,
    num_bathrooms: 2,
    city: 'Bhubaneswar',
    building_type: 'Residential',
    finish_quality: 'Standard',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    const isNumeric = ['total_area_sqft', 'num_floors', 'num_bedrooms', 'num_bathrooms'].includes(name);
    setData({ ...data, [name]: isNumeric ? parseInt(value, 10) || 0 : value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(data);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <h2 className="text-2xl font-semibold text-gray-700 mb-4">Project Details</h2>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">Total Area (sq. ft)</label>
        <input 
          type="number" 
          name="total_area_sqft" 
          value={data.total_area_sqft} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border" 
          required 
          min="100"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">Number of Floors</label>
        <input 
          type="number" 
          name="num_floors" 
          value={data.num_floors} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border" 
          required 
          min="1"
          max="10"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">Bedrooms</label>
        <input 
          type="number" 
          name="num_bedrooms" 
          value={data.num_bedrooms} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border" 
          required 
          min="1"
          max="10"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">Bathrooms</label>
        <input 
          type="number" 
          name="num_bathrooms" 
          value={data.num_bathrooms} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border" 
          required 
          min="1"
          max="10"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">City</label>
        <select 
          name="city" 
          value={data.city} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border"
        >
          <option value="Bhubaneswar">Bhubaneswar</option>
          <option value="Delhi">Delhi</option>
          <option value="Mumbai">Mumbai</option>
          <option value="Bengaluru">Bengaluru</option>
        </select>
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700">Finish Quality</label>
        <select 
          name="finish_quality" 
          value={data.finish_quality} 
          onChange={handleChange} 
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 p-2 border"
        >
          <option value="Basic">Basic</option>
          <option value="Standard">Standard</option>
          <option value="Premium">Premium</option>
        </select>
      </div>
      
      <input type="hidden" name="building_type" value="Residential" />

      <button 
        type="submit" 
        disabled={isLoading} 
        className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 transition-colors"
      >
        {isLoading ? 'Calculating...' : 'Generate Estimate'}
      </button>
    </form>
  );
};

export default InputForm;
