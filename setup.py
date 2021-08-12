from distutils.core import setup
from notificore_restapi import __version__

setup(
    name='notificore-restapi',
    version=__version__,
    packages=['notificore_restapi'],
    url='https://github.com/Notificore/notificore-python',
    license='BSD 2-Clause License',
    author='Ievgen Krupa',
    author_email='Ievgen.Krupa+github@gmail.com',
    description='Notificore REST API Wrapper'
)
