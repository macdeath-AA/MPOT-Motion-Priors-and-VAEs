import pickle
import torch
import numpy as np

filename = "examples/results_data_dict_2.pickle"
output = "examples/trajs_final_free_2.pkl"

with open(filename, 'rb') as f:
    trajs = pickle.load(f)

trajsFinal = trajs['trajs_final_free']

with open(output, 'wb') as f:
    pickle.dump(trajsFinal, f)

# torch.save(trajsFinal, output)

print("Trajectories saved to", output)