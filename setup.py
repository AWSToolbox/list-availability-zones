# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.list-availability-zones',
    version='0.1.1',
    packages=['wolfsoftware.list_availability_zones'],
    entry_points={
        'console_scripts': [
            'list-availability-zones=wolfsoftware.list_availability_zones.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='Generate a table of the availability zones your account is using.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DevelopersToolbox/template-package-cli',
    project_urls={
        ' Source': 'https://github.com/AWSToolbox/list-availability-zones',
        ' Tracker': 'https://github.com/AWSToolbox/list-availability-zones/issues/',
        ' Documentation': 'https://github.com/AWSToolbox/list-availability-zones',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        # 'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Utilities',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
