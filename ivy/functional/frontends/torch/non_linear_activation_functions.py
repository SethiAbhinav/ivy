# global
import ivy


def _compute_threshold(input, threshold, value, inplace):
    if inplace:
        return ivy.where(ivy.greater(input, threshold), input, value, out=input)
    return ivy.where(ivy.greater(input, threshold), input, value)


def sigmoid(input, out=None):
    return ivy.sigmoid(input, out=out)


sigmoid.unsupported_dtypes = ("float16",)


def leaky_relu(input, negative_slope=0.01):
    return ivy.leaky_relu(input, alpha=negative_slope)


leaky_relu.unsupported_dtypes = ("float16",)


def softmax(input, dim=None, dtype=None):
    if dtype:
        input = ivy.astype(ivy.array(input), ivy.as_ivy_dtype(dtype))
    return ivy.softmax(input, axis=dim)


softmax.unsupported_dtypes = ("float16",)


def gelu(input, approximate="none"):
    if approximate == "none":
        approximate = False
    else:
        approximate = True
    return ivy.gelu(input, approximate)


gelu.unsupported_dtypes = ("float16",)


def tanh(input, *, out=None):
    return ivy.tanh(input, out=out)


tanh.unsupported_dtypes = {"torch": ("float16",)}


def logsigmoid(input):
    return -ivy.softplus(-input)


logsigmoid.unsupported_dtypes = ("float16",)


def softmin(input, dim=None, dtype=None):
    if dtype:
        input = ivy.astype(ivy.array(input), ivy.as_ivy_dtype(dtype))
    return ivy.softmax(-input, axis=dim)


softmin.unsupported_dtypes = ("float16",)


def threshold(input, threshold, value, inplace=False):
    return _compute_threshold(input, threshold, value, inplace)


threshold.unsupported_dtypes = ("float16",)


def threshold_(input, threshold, value):
    return _compute_threshold(input, threshold, value, inplace=True)


threshold_.unsupported_dtypes = ("float16",)
