from setuptools import find_packages, setup

version = '5.0.3'

setup(
    name='alerta-goalert',
    version=version,
    description='Alerta plugin for GoAlert',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='MIT',
    author='SKob',
    author_email='skobolo@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_goalert'],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'goalert = alerta_goalert:TriggerEvent'
        ]
    }
)
