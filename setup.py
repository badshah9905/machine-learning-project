import setuptools 

__version__="0.1"

REPO_NAME="machine-learning-project"
AUTHOR_USER_NAME="badshah9905"
SRC_REPO="mlproject"
AUTHOR_EMAIL="badshahm669@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small ml project",
    url=f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issued"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)