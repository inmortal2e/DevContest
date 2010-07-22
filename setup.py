try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='DevContest',
    version='0.2.4',
    description='Web interface for developers contests. Python, C, Pascal, PHP, Perl, Java',
    author='Juda Kaleta',
    author_email='juda.kaleta@gmail.com',
    url='http://github.com/yetty/DevContest/',
    license='GPL2',
    install_requires=[
        "Pylons==0.9.7",
        "routes==1.11",
        "SQLAlchemy>=0.5",
        "Pygments>=1.3.0",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'devcontest': ['i18n/*/LC_MESSAGES/*.mo']},
    message_extractors={'devcontest': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
            ('public/**', 'ignore', None)]},
    zip_safe=True,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = devcontest.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
