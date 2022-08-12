import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    longdesc = fh.read()

    setuptools.setup(
        name="PrismBot",
        packages=setuptools.find_packages(),
        version="1.0.0",
        author="ColdCawfee",
        description="This is a discord bot that will take an initial sentence, and google translate it multiple times.",
        long_description=longdesc,
        url="https://github.com/ColdCawfee/PrismBot",
        project_urls={},
        scripts=[
            "main.py"
        ],
        include_package_data=True,
        install_requires=[
            'hikari==2.0.0.dev110',
            'hikari-lightbulb==2.2.4',
            'googletrans==3.1.0a0',
        ],
        python_requires=">=3.8",
    )