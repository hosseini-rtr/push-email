import os
from setuptools import setup, find_packages

setup(
    name='django-newsletter-notify',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Django app for sending newsletter notifications.',
    long_description=open('README.md').read(), # Assumes README.md will be in the same directory
    long_description_content_type='text/markdown',
    url='https://www.example.com/newsletter_notify/', # Replace with actual URL if available
    license='BSD License', # Example license
    packages=['newsletter_notify'], # This will look for a 'newsletter_notify' directory (package)
                                   # in the same directory as setup.py
    install_requires=['Django>=3.2'], # Check project requirements.txt for specific Django version
    include_package_data=True, # This tells setuptools to look at MANIFEST.in
    classifiers=[
        'Development Status :: 3 - Alpha', # Or '4 - Beta', '5 - Production/Stable'
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0', # Add other supported Django versions
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Communications :: Email',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8', # Specify compatible Python versions
)
