# Arch-AI: AI-Powered Architectural Estimator

This project is a web application that provides instant construction cost estimates and basic 3D visualizations for residential building projects.

## 🏗️ Features

- **Cost Prediction**: Get instant construction cost estimates based on area, location, and quality
- **3D Visualization**: See a basic 3D model of your building
- **Multi-City Support**: Estimates for Bhubaneswar, Delhi, Mumbai, and Bengaluru
- **Quality Options**: Basic, Standard, and Premium finish quality options
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, CatBoost (ML model)
- **Frontend:** React, Vite, Three.js, Tailwind CSS
- **3D Graphics:** React Three Fiber
- **Deployment:** Docker, Heroku (Backend), Vercel (Frontend)

## 📦 Setup & Running Locally

### Prerequisites

- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`
   API documentation at `http://127.0.0.1:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:5173`

## 🚀 Usage

1. **Start the backend server** (follow backend setup above)
2. **Start the frontend** (follow frontend setup above)
3. **Open your browser** to `http://localhost:5173`
4. **Fill in the project details:**
   - Total area in square feet
   - Number of floors
   - Number of bedrooms and bathrooms
   - Select your city
   - Choose finish quality
5. **Click "Generate Estimate"** to get your cost prediction and 3D visualization

## 📁 Project Structure

```
arch-ai-project/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile          # Docker configuration
│   └── cost_model.joblib   # ML model (created after training)
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── InputForm.jsx
│   │   │   ├── ResultDisplay.jsx
│   │   │   └── Viewer3D.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── index.html
└── README.md
```

## 🧪 API Endpoints

### GET `/`
Health check endpoint

### POST `/predict`
Predict construction cost

**Request Body:**
```json
{
  "total_area_sqft": 1200,
  "num_floors": 2,
  "num_bedrooms": 3,
  "num_bathrooms": 2,
  "city": "Bhubaneswar",
  "building_type": "Residential",
  "finish_quality": "Standard"
}
```

**Response:**
```json
{
  "estimated_cost_inr": 4800000
}
```

## 🎯 Cost Calculation Logic

The current implementation uses a simplified calculation:
- **Base cost**: ₹2,000 per sq ft
- **City multipliers**: 
  - Bhubaneswar: 1.0x
  - Delhi: 2.0x
  - Mumbai: 2.5x
  - Bengaluru: 1.8x
- **Quality multipliers**:
  - Basic: 0.8x
  - Standard: 1.0x
  - Premium: 1.5x

**Formula**: `Area × Base Cost × City Multiplier × Quality Multiplier × Floors`

## 🚀 Deployment

### Backend (Heroku)

1. Create a Heroku app
2. Set up the Heroku CLI
3. Deploy using Docker:
   ```bash
   heroku container:push web
   heroku container:release web
   ```

### Frontend (Vercel)

1. Push code to GitHub
2. Connect GitHub repository to Vercel
3. Set environment variable `VITE_API_URL` to your backend URL
4. Deploy

## 🔮 Future Enhancements

- **Machine Learning Model**: Train on real construction data
- **Detailed Cost Breakdown**: Materials, labor, permits breakdown
- **Advanced 3D Models**: Floor plans and detailed architecture
- **User Accounts**: Save and manage multiple projects
- **Location Integration**: GPS-based location detection
- **Material Calculator**: Detailed material quantity estimation

## 🐛 Known Issues

- 3D model is basic (boxes only)
- Cost estimation is simplified
- Limited to 4 cities currently

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for the construction industry**
