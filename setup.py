from setuptools import setup

setup(
    name="resume-evaluator",
    version="1.0",
    description="Evaluate and rank intern applicants across many different universities.",
    author="Jeremy Ng",
    author_email="jeremy1x.ng@intel.com",
    packages=["resume-evaluator"],
    package_dir={"resume-evaluator": "src"},
    # external packages as dependencies
    install_requires=["resume-evaluator", "nltk", "pymupdf"],
)
