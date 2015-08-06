import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-phonenumbers',
    version='0.1.3',
    packages=['django_phonenumbers'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Phone number field for Django admin',
    long_description=README,
    url='https://github.com/iraklikhitarishvili/html5croppingtools',
    author='irakli khitarishvili',
    author_email='iraklikhitarishvili@yahoo.com',
    install_requires=['pillow'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)