import { useState } from 'react';
import axios from 'axios';
import InputForm from './components/InputForm';
import ResultDisplay from './components/ResultDisplay';

function App() {
  const [formData, setFormData] = useState(null);
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFormSubmit = async (data) => {
    setIsLoading(true);
    setError('');
    setResult(null);
    setFormData(data);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
      const response = await axios.post(`${apiUrl}/predict`, data);
      setResult(response.data);
    } catch (err) {
      setError('Failed to get prediction. Please ensure the backend is running.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 font-sans p-4 sm:p-8">
      <div className="max-w-6xl mx-auto">
        <header className="text-center mb-8">
          <h1 className="text-4xl sm:text-5xl font-bold text-gray-800">Arch-AI 🏗️</h1>
          <p className="text-lg text-gray-600 mt-2">Instant Construction Cost Estimation & Visualization</p>
        </header>

        <main className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <InputForm onSubmit={handleFormSubmit} isLoading={isLoading} />
          </div>

          <div className="bg-white p-6 rounded-lg shadow-md flex items-center justify-center min-h-[400px]">
            {isLoading && <p className="text-xl">Generating your estimate...</p>}
            {error && <p className="text-xl text-red-500">{error}</p>}
            {result && formData && <ResultDisplay result={result} formData={formData} />}
            {!isLoading && !result && !error && (
              <p className="text-xl text-gray-500">Your results will appear here.</p>
            )}
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
