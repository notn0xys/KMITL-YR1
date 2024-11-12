import pickle

# Specify the path to your pickle file
pickle_file_path = 'car_data_th.pkl'

# Open the file in 'rb' mode (read-binary)
with open(pickle_file_path, 'rb') as file:
    # Load the data from the pickle file
    car_data = pickle.load(file)

# Print the loaded data
print(car_data)