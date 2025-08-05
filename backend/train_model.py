# Create a simple trained model for demonstration
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Create sample training data
np.random.seed(42)
n_samples = 1000

# Generate synthetic data
data = {
    'total_area_sqft': np.random.randint(500, 5000, n_samples),
    'num_floors': np.random.randint(1, 5, n_samples),
    'num_bedrooms': np.random.randint(1, 6, n_samples),
    'num_bathrooms': np.random.randint(1, 5, n_samples),
    'city': np.random.choice(['Bhubaneswar', 'Delhi', 'Mumbai', 'Bengaluru'], n_samples),
    'building_type': np.random.choice(['Residential', 'Commercial'], n_samples),
    'finish_quality': np.random.choice(['Basic', 'Standard', 'Premium'], n_samples)
}

# Create DataFrame
df = pd.DataFrame(data)

# Create realistic cost based on the features
base_cost_per_sqft = 2000
city_multipliers = {'Bhubaneswar': 1.0, 'Delhi': 2.0, 'Mumbai': 2.5, 'Bengaluru': 1.8}
quality_multipliers = {'Basic': 0.8, 'Standard': 1.0, 'Premium': 1.5}

costs = []
for _, row in df.iterrows():
    city_mult = city_multipliers[row['city']]
    quality_mult = quality_multipliers[row['finish_quality']]
    cost = (row['total_area_sqft'] * base_cost_per_sqft * 
            city_mult * quality_mult * row['num_floors'])
    # Add some noise
    cost += np.random.normal(0, cost * 0.1)
    costs.append(max(cost, 100000))  # Minimum cost

df['total_cost_inr'] = costs

# Prepare features for training
X = df.drop('total_cost_inr', axis=1)
y = df['total_cost_inr']

# Encode categorical variables
le_city = LabelEncoder()
le_building_type = LabelEncoder()
le_finish_quality = LabelEncoder()

X_encoded = X.copy()
X_encoded['city'] = le_city.fit_transform(X['city'])
X_encoded['building_type'] = le_building_type.fit_transform(X['building_type'])
X_encoded['finish_quality'] = le_finish_quality.fit_transform(X['finish_quality'])

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save the model and encoders
model_data = {
    'model': model,
    'le_city': le_city,
    'le_building_type': le_building_type,
    'le_finish_quality': le_finish_quality,
    'feature_names': X_encoded.columns.tolist()
}

joblib.dump(model_data, 'cost_model.joblib')
print("Model trained and saved successfully!")
print(f"Model score: {model.score(X_encoded, y):.3f}")
