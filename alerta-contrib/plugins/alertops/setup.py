from setuptools import find_packages, setup

version = '1.0.0.1'

setup(
    name='alerta-alertops',
    version=version,
    description='Alerta plugin for AlertOps',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='AlertOps',
    author='Kam Srikanth',
    author_email='kamleshs@alertops.com',
    packages=find_packages(),
    py_modules=['alerta_alertops'],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'alertops = alerta_alertops:TriggerEvent'
        ]
    }
)
