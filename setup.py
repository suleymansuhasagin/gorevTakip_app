from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gorev-takip",
    version="0.1.0",
    author="Adınız Soyadınız",
    author_email="email@adresiniz.com",
    description="Basit bir görev takip uygulaması",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kullanici-adiniz/gorev-takip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gorev-takip=todo_app.user_interface:main",
        ],
    },
)