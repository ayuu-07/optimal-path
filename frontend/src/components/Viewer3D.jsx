import { Canvas } from '@react-three/fiber';
import { OrbitControls, Box, Text } from '@react-three/drei';
import { Suspense } from 'react';

const Building = ({ formData }) => {
  const { total_area_sqft, num_floors } = formData;
  const areaPerFloor = total_area_sqft / num_floors;
  const sideLength = Math.sqrt(areaPerFloor) / 10; // Scale down for better viewing
  const floorHeight = 2; // Height per floor

  // Color based on finish quality
  const getColor = (quality) => {
    switch (quality) {
      case 'Premium': return '#8B5CF6'; // Purple
      case 'Standard': return '#6B7280'; // Gray
      case 'Basic': return '#F59E0B'; // Yellow
      default: return '#6B7280';
    }
  };

  return (
    <group>
      {/* Create a box for each floor */}
      {[...Array(num_floors)].map((_, i) => (
        <Box
          key={i}
          args={[sideLength, floorHeight, sideLength]}
          position={[0, i * floorHeight + floorHeight / 2, 0]}
        >
          <meshStandardMaterial color={getColor(formData.finish_quality)} />
        </Box>
      ))}

      {/* Ground plane */}
      <Box args={[sideLength * 1.5, 0.1, sideLength * 1.5]} position={[0, -0.05, 0]}>
        <meshStandardMaterial color="#22C55E" />
      </Box>
    </group>
  );
};

const Viewer3D = ({ formData }) => {
  const { total_area_sqft, num_floors } = formData;
  const areaPerFloor = total_area_sqft / num_floors;
  const sideLength = Math.sqrt(areaPerFloor) / 10;

  return (
    <div className="w-full h-full">
      <Canvas 
        camera={{ 
          position: [sideLength * 3, sideLength * 3, sideLength * 3], 
          fov: 50 
        }}
      >
        <Suspense fallback={null}>
          <ambientLight intensity={0.6} />
          <directionalLight position={[10, 10, 5]} intensity={1} />
          <pointLight position={[-10, -10, -5]} intensity={0.3} />
          
          <OrbitControls 
            enablePan={true}
            enableZoom={true}
            enableRotate={true}
            autoRotate={true}
            autoRotateSpeed={1}
          />
          
          <Building formData={formData} />
        </Suspense>
      </Canvas>
      
      <div className="absolute bottom-2 left-2 bg-black bg-opacity-50 text-white p-2 rounded text-xs">
        <p>Click and drag to rotate • Scroll to zoom</p>
      </div>
    </div>
  );
};

export default Viewer3D;
