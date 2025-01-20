from setuptools import setup, find_packages


setup(
    name = "Generative AI Project",
    version = "0.0.0",
    author = "George Sebastian Cucuiet",
    author_email = "code@sudo-ai.com",
    packages = find_packages(),
    install_requires = [
        "numpy",
        "tensorflow",
        "keras",
        "matplotlib",
        "pillow",
        "tqdm",
        "scipy",
        "scikit-learn",
        "pandas",
        "transformers",
        "jupyter",
        "seaborn",
    ],  
)