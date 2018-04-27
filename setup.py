import setuptools

setuptools.setup(
    name="mytool",
    version="0.1",

    author="Mihai Criveti",

    description="Build sample",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),
    scripts=['bin/mytool_cmd'],

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
