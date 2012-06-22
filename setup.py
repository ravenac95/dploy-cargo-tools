from setuptools import setup, find_packages

VERSION = '0.0.1-dev'

LONG_DESCRIPTION = open('README.rst').read()

setup(name='dploy-cargo-tools',
    version=VERSION,
    description="dploy's tools for use in cargo",
    long_description=LONG_DESCRIPTION,
    keywords='',
    author='Reuven V. Gonzales',
    author_email='reuven@tobetter.us',
    url="https://github.com/ravenac95/dploy-cargo-tools",
    license='MIT',
    platforms='*nix',
    packages=find_packages(exclude=['ez_setup', 'examples', 'prototyping', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyzmq',
        'supervisor',
    ],
    entry_points={
        'console_scripts': [
            'dploy-cargo-builder = dploycargotools.main:main',
            'dploy-interactive = dploycargotools.main:main',
            'dploy-crash-notify = dploycargotools.main:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Build Tools',
    ],
)
