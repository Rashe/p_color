import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='p_color',
    version='0.1.3',
    author="Rashe",
    description="Color your print()",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rashe/p_color"
)
