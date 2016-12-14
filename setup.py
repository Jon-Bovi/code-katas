"""Setup mailroom madness module."""


from setuptools import setup

setup(
    name="code-katas",
    description="code kata implementations from codewars",
    version=0.5,
    author="Ford Fowler",
    author_email="fordjfowler@gmail.com",
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["fizzbuzz",
                "open_or_senior",
                "bit_counting",
                "dubstep_decoder",
                "rna",
                "dbl_linear"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
