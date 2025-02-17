codechecker_kernel
===========

``codechecker_kernel`` is a simple kernel to run CodeChecker inside a Jupyter notebook.
It is base on echo_kernel provided in the documentation.
Make sure you've installed CodeChecker first and that it's in your path when you launch Jupyter.

Installation
------------
To install ``codechecker_kernel``::

    git clone https://github.com/esstorm/codechecker_kernel.git
    cd codechecker_kernel
    pip install .
    python -m codechecker_kernel.install

Using the CodeChecker kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for a CodeChecker notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel codechecker`` to
their command line arguments.
