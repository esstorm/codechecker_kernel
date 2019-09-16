from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='codechecker_kernel',
    version='0.1',
    packages=['codechecker_kernel'],
    description='Simple kernel for CodeChecker',
    long_description=readme,
    author='Esteban Torres',
    author_email='e.torres.menendez@gmail.com',
    url='https://github.com/esstorm/codechecker_kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
