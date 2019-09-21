from ipykernel.kernelapp import IPKernelApp
from . import CCKernel

IPKernelApp.launch_instance(kernel_class=CCKernel)
