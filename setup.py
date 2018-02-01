from setuptools import find_packages, setup

setup(
    name='django-healthy-pixel',
    version='0.0.0-alpha',
    description='',
    url='https://github.com/hobbes7878/django-healthy-pixel',
    author='Jon McClure',
    author_email='jon.r.mcclure@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='',

    packages=find_packages(exclude=['docs', 'tests', 'example']),

    install_requires=[],

    extras_require={
        'test': ['pytest'],
    },
)
