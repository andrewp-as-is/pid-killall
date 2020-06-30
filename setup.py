import setuptools

setuptools.setup(
    name='pid-killall',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pid-killall']
)
