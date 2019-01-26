import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-branding",
    version="0.0.1",
    author="Michael Moeller",
    author_email="kontakt@mk-moeller.de",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/MichiMolle/django-branding",
    packages=setuptools.find_packages(),
    install_requires=[
          'django',
      ],
)