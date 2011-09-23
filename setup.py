from setuptools import setup, find_packages
version = "0.1"
setup(
    name = "MoFlo",
    version = version,
    packages = find_packages(),
    install_requires = [
        'pytest',
    ],
    include_package_data = True,
    package_data = {},
    zip_safe = False,
)
