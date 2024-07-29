setup(
    name='openimis-be-payment-request',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU AGPL v3',
    description='The openIMIS Backend payment request module.',
    url='https://amg.km/',
    author='Maxime Ngoe,
    author_email='maxime.ngoe@y-note.cm',
    install_requires=[
        'django',
        'djangorestframework',
        'openimis-be-core',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)
#test de la nouvelle branche future appelé "Future_branch"
