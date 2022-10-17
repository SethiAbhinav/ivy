# global
import torch

# local
import ivy
import ivy.functional.frontends.torch as torch_frontend


class Tensor:
    def __init__(self, data):
        if ivy.is_native_array(data):
            data = ivy.Array(data)
        self.data = data

    def __repr__(self):
        return (
            "ivy.functional.frontends.torch.Tensor("
            + str(ivy.to_list(self.data))
            + ")"
        )

    # Instance Methoods #
    # -------------------#

    def reshape(self, shape):
        return torch_frontend.reshape(self.data, shape)

    def add(self, other, *, alpha=1):
        return torch_frontend.add(self.data, other, alpha=alpha)

    def sin(self, *, out=None):
        return torch_frontend.sin(self.data, out=out)

    def sin_(self):
        self.data = self.sin()
        return self.data

    def sinh(self, *, out=None):
        return torch_frontend.sinh(self.data, out=out)

    def sinh_(self):
        self.data = self.sinh()
        return self.data

    def cos(self, *, out=None):
        return torch_frontend.cos(self.data, out=out)

    def view(self, shape):
        self.data = torch_frontend.reshape(self.data, shape)
        return self.data

    def float(self, memory_format=torch.preserve_format):
        return ivy.astype(self.data, ivy.float32)

    def asinh(self, *, out=None):
        return torch_frontend.asinh(self.data, out=out)

    def asinh_(self):
        self.data = self.asinh()
        return self.data

    def tan(self, *, out=None):
        return torch_frontend.tan(self.data, out=out)

    # Special Methoods #
    # -------------------#

    def __add__(self, other):
        return torch_frontend.add(self, other)

    def __radd__(self, other):
        return torch_frontend.add(other, self)


# Tensor (alias)
tensor = Tensor
