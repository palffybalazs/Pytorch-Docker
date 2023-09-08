# Test gpu with pytorch

import torch

print("Is GPU available: ", torch.cuda.is_available())

print("Number of GPU: ", torch.cuda.device_count())

print("Device number: ", torch.cuda.current_device())

print("Cuda device: ", torch.cuda.device(0))

print("Name of the GPU: ", torch.cuda.get_device_name(0))


