from setuptools import setup, find_packages

setup(
    name='openrouter_exception_handler',
    packages=find_packages(where='src'),  # ✅ Ahora encuentra el paquete correctamente
    package_dir={'': 'src/openrouter_exception_handler'},  # ✅ Mapea el paquete a la carpeta `src`
    install_requires=['requests'],
)
