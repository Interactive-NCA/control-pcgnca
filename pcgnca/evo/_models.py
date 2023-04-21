"""
Definition of models used for evolution. In addition, this module
provides helper functions for setting up models.
"""

# --------------------- External libraries import
import torch as th
from torch import nn
from torch.nn import Conv2d
import torch.nn.functional as F

import numpy as np


# --------------------- Models definition
class NCA(nn.Module):

    def __init__(self, n_tiles, n_aux_chan=0, bin_chan=False):

        # - Initialise the parent (torch nn module)
        super().__init__()

        # - Define hyperparameters of the NCA model
        self._has_aux = n_aux_chan > 0
        self.n_hid_1 = n_hid_1 = 32
        self.n_aux = n_aux_chan
        self.n_tiles = n_tiles
        self.has_binary = bin_chan

        # - Define architecture of the network
        self.l1 = Conv2d(self.n_tiles + self.has_binary + self.n_aux, n_hid_1, kernel_size=3, stride=1, padding=0, bias=True)
        self.l2 = Conv2d(n_hid_1, n_hid_1, kernel_size=1, stride=1, padding=0, bias=True)
        self.l3 = Conv2d(n_hid_1, self.n_tiles + self.n_aux, kernel_size=1, stride=1, padding=0, bias=True)
        self.layers = [self.l1, self.l2, self.l3]
        self.last_aux = None

        # - Initialise weights according to the best practices (based on actual research)
        self.apply(_init_weights)

    def forward(self, x):

        # Since we do not use gradient based optimisation,
        # disable computation of gradient which reduces memory consumption 
        with th.no_grad():
            
            # - Aux channels setup
            # -- Add auxiliary channels to input
            if self._has_aux:

                # The input does not have any yet, then initialise them by setting all to zero
                # Example: if the grid dimension is 16 x 16 and we have 3 aux channels, then
                # we add to the input [1, 3, 16, 16] array full of zeros, where 1 just denotes batch size
                if self.last_aux is None:
                    self.last_aux = th.zeros(size=(1, self.n_aux, *x.shape[-2:]))
                
                # Concat the input with aux channels
                x_in = th.cat([x, self.last_aux], axis=1)
            
            # -- Zero aux channels
            else:
                x_in = x

            # - Run the actual forward pass
            x = self.l1(x_in)
            x = th.relu(x)
            x = self.l2(x)
            x = th.relu(x)
            x = self.l3(x)
            x = th.sigmoid(x)

            # - Save the values from the aux channels for the next pass ..
            # ..and extract the actual output
            if self._has_aux > 0 or self.has_binary:

                # -- Getting the aux channels (the last M channels)
                self.last_aux = x[:,-self.n_aux:,:,:]
                self.last_aux = F.pad(self.last_aux, (1,1,1,1), mode='constant', value=0)

                # -- Getting the actual output
                x = x[:, :self.n_tiles,:,:]

        return x, self.last_aux

    def reset(self):
        self.last_aux = None


# --------------------- Helper functions
# ------------------------- Private (only use in this module)
def _init_weights(m):
    """
    Initialiase the weights according to the
    best practices. (based on the research)
    """
    if type(m) == th.nn.Linear:
        th.nn.init.xavier_uniform_(m.weight)
        m.bias.data.fill_(0.01)

    if type(m) == th.nn.Conv2d:
        th.nn.init.orthogonal_(m.weight)

# ------------------------- Public
def get_init_weights(nn):
    """
    Use to get flat vector of weights from PyTorch model
    """
    init_params = []

    # Iterate over all layers of the model
    for lyr in nn.layers:
        init_params.append(lyr.weight.view(-1))
        if lyr.bias is not None:
            init_params.append(lyr.bias.view(-1))
    
    # Extract the weights
    init_params = th.cat(init_params)

    return init_params

def set_weights(nn, weights):

    """
    Use to set weights of the given PyTorch model.
    """

    with th.no_grad():
        n_el = 0

        for layer in nn.layers:
            l_weights = weights[n_el : n_el + layer.weight.numel()]
            n_el += layer.weight.numel()
            l_weights = l_weights.reshape(layer.weight.shape)
            layer.weight = th.nn.Parameter(th.Tensor(np.array(l_weights)))
            layer.weight.requires_grad = False
            if layer.bias is not None:
                n_bias = layer.bias.numel()
                b_weights = weights[n_el : n_el + n_bias]
                n_el += n_bias
                b_weights = b_weights.reshape(layer.bias.shape)
                layer.bias = th.nn.Parameter(th.Tensor(np.array(b_weights)))
                layer.bias.requires_grad = False

    return nn
