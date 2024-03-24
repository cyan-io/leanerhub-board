from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = f.readlines()


setup(
    name="learner-board",
    version="1.0.1",
    author="Cyan@https://github.com/cyan-io",
    author_email="cyan-io@outlook.com",
    url="https://github.com/cyan-io/learner-board",
    download_url="https://github.com/cyan-io/learner-board/releases",
    license="MPL 2.0",
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "learnerboard = src.board:main",
            "lboard = src.board:main",
        ]
    },
    install_requires=install_requires,
    platforms="any",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)
