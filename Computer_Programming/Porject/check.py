import pickle
with open('car_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)