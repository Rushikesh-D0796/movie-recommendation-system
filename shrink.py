import pickle
import numpy as np
import os

file_name = 'similarity_matrix.pkl'

original_size = os.path.getsize(file_name) / (1024 * 1024)
print(f"Original file size: {original_size:.2f} MB")

print("Loading the massive matrix into memory... (please wait)")
with open(file_name, 'rb') as file:
    matrix = pickle.load(file)

print("Compressing data...")
compressed_matrix = matrix.astype(np.float16)

print("Saving the compressed file...")
with open(file_name, 'wb') as file:
    pickle.dump(compressed_matrix, file)

new_size = os.path.getsize(file_name) / (1024 * 1024)
print(f"✅ Success! New file size: {new_size:.2f} MB")