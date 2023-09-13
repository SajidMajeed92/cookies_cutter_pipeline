#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Sajid Majeed",
    author_email='sajidmajeed.ist@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="y",
    entry_points={
        'console_scripts': [
            'pipe_line_with_cookie_cutter=pipe_line_with_cookie_cutter.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pipe_line_with_cookie_cutter',
    name='pipe_line_with_cookie_cutter',
    packages=find_packages(include=['pipe_line_with_cookie_cutter', 'pipe_line_with_cookie_cutter.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SajidMajeed92/pipe_line_with_cookie_cutter',
    version='0.0.1',
    zip_safe=False,
)
