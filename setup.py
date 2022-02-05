import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name='easy-bloom-filter',
    packages=setuptools.find_packages(),
    version='0.1.0',
    license='MIT',
    description="""python implementation of bloom filter""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='yehoyada.sht',
    author_email='yehoyada.sht@gmail.com',
    maintainer='yehoyada.sht',
    maintainer_email='yehoyada.sht@gmail.com',
    url='https://github.com/hvuhsg/py-bloom-filter',
    keywords=['bloom', 'filter'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)