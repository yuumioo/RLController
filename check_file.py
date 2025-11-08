import pickle
import os

town = "Town02"

checkpoint_dir = f"RLC/Autonomous-Driving-in-Carla-using-Deep-Reinforcement-Learning/checkpoints/PPO/Town02/"

# Get a list of all pickle files in the directory
all_files = os.listdir(checkpoint_dir)
pickle_files = [f for f in all_files if f.endswith('.pickle')]

print(f"Checking {len(pickle_files)} pickle files in {checkpoint_dir}...")

for f in pickle_files:
    file_path = os.path.join(checkpoint_dir, f)
    print(f"checking {file_path}")
    try:
        with open(file_path, 'rb') as handle:
            data = pickle.load(handle)
            print(data)
            
            # Check if the episode key exists and matches
            if 'episode' in data and data['episode'] == 740:
                print(f"\nFOUND MATCH!")
                print(f"File: {f}")
                print(f"Data: {data}")
                break
    except Exception as e:
        print(f"Error reading {f}: {e}")