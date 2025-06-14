import gdown
import joblib
import os

# Google Drive file ID from your link
file_id = '1MLUr5RprSx-kgfWRuWGx11iqA8Q4i2DE'
output_path = 'random_forest_model.pkl'

# Download if not already downloaded
if not os.path.exists(output_path):
    url = f'https://drive.google.com/uc?id={file_id}'
    print("Downloading model from Google Drive...")
    gdown.download(url, output_path, quiet=False)
else:
    print("Model already exists locally.")

# Load the model
print("Loading model...")
model = joblib.load(output_path)
print("Model loaded and ready.")
