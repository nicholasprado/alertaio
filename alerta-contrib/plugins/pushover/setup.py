from setuptools import find_packages, setup

version = '5.3.2'

setup(
    name='alerta-pushover',
    version=version,
    description='Alerta plugin for Pushover',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    packages=find_packages(),
    py_modules=['alerta_pushover'],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'pushover = alerta_pushover:PushMessage'
        ]
    }
)
