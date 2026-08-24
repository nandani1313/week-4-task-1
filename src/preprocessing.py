import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Feature selection
    features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    
    # Feature scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    return df, scaled_features
