from setuptools import setup, find_packages

setup(
    name='ch-st-molstar',
    version='0.0.2',
    author='doubleone44',
    author_email='mees@charmtx.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['streamlit', 'mrcfile', 'numpy'],
    url='https://github.com/Charm-Tx/streamlit-molstar',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved",
        "Topic :: Scientific/Engineering",
    ]
)
