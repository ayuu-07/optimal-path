import Viewer3D from './Viewer3D';

const ResultDisplay = ({ result, formData }) => {
  const formattedCost = new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(result.estimated_cost_inr);

  return (
    <div className="w-full h-full flex flex-col">
      <div className="text-center mb-4">
        <p className="text-lg text-gray-600">Estimated Construction Cost</p>
        <p className="text-4xl font-bold text-green-600">{formattedCost}</p>
        <div className="mt-2 text-sm text-gray-500">
          <p>Area: {formData.total_area_sqft} sq ft • Floors: {formData.num_floors}</p>
          <p>{formData.city} • {formData.finish_quality} Quality</p>
        </div>
      </div>
      <div className="flex-grow bg-gray-200 rounded min-h-[300px]">
         <Viewer3D formData={formData} />
      </div>
    </div>
  );
};

export default ResultDisplay;
