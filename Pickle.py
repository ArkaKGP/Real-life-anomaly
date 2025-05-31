# import pickle
# import os

# file_path = 'C:/Users/USER/Downloads/FTP/PaDiM-Anomaly-Detection-Localization-master/mvtec_result/temp_wide_resnet50_2/train_bottle.pkl'

# if os.path.exists(file_path):
#     with open(file_path, 'rb') as f:
#         try:
#             data = pickle.load(f)
#             mean = data[0]
#             covariance = data[1]
#             print("✅ Loaded successfully")
#             print("Mean shape:", mean.shape)
#             print("Covariance shape:", covariance.shape)
#         except Exception as e:
#             print("❌ Failed to load:", e)
# else:
#     print("❌ File not found!")


import pickle

file_path = 'C:/Users/USER/Downloads/FTP/PaDiM-Anomaly-Detection-Localization-master/mvtec_result/temp_wide_resnet50_2/train_bottle.pkl'

with open(file_path, 'rb') as f:
    data = pickle.load(f)

# Check what type data is and its keys if applicable
if isinstance(data, dict):
    print("Keys in data:", data.keys())
    print(type(data['mean']))
    print(data['mean'].shape)
    print(type(data['covariance']))
    print(data['covariance'].shape)
else:
    print("Data is not a dictionary, type:", type(data))
    # If it's a list or tuple, you can try:
    try:
        print(type(data[0]))
        print(data[0].shape)
        print(type(data[1]))
        print(data[1].shape)
    except Exception as e:
        print("Failed to print shapes:", e)
