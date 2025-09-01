from setuptools import setup, find_packages

setup(
    name="anubis_product_core",
    version="0.0.2",
    packages=find_packages(),
    author="Jose Manuel Herrera Saenz",
    author_email="incubadoradepollos@gmail.com",
    description="Productos abstractos para utilizar con adaptadores de ecommerce",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/mi-paquete",
    install_requires=[
        "hexarch_core @ git+https://github.com/AnubisSystems/AnubisCore.git"
        # Lista de dependencias, ej:
        # "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Legal Industry",
        "Topic :: Education",
    ]
    python_requires=">=3.13.0",
)
