from setuptools import setup

setup(
    name='cozmo-repl',
    version='0.1.0',
    description='IPython REPL for Cozmo',
    license="Apache2",
    author='Adrien Becchis',
    author_email='adriean.khisbe@live.fr',
    packages=['cozmo_repl'],
    scripts=["cozmo-repl"],
    install_requires = ['cozmo', 'IPython', 'style']
)
