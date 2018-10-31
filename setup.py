from setuptools import find_packages, setup

setup(
    name="iqe-kafka-plugin",
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=[
        "kafka-python==1.4.3"
    ]
)
