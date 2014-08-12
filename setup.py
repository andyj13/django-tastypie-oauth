from setuptools import setup


required = [line for line in open('requirements/base.txt').read().split("\n")]


setup(
    name='django-tastypie-oauth',
    version=__import__('tastypie_oauth').__version__,
    description='Providing OAuth services for Tastypie APIs',
    long_description=open('README.md').read(),
    author='Oregon Center for Applied Science',
    author_email='bpitcher@orcasinc.com',
    url='https://github.com/orcasgit/django-tastypie-oauth',
    install_requires=["setuptools"] + required,
    license='Apache 2.0',
    packages=['tastypie_oauth'],
    package_data={'': ['LICENCE']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
