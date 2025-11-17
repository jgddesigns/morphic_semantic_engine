from setuptools import setup, find_packages

setup(
    name="morphic-semantic-engine",
    version="0.1.0",
    description="Deterministic semantic generator from tiny numeric seeds.",
    author="Jason G. Dunn",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
