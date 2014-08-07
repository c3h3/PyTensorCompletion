from setuptools import setup, find_packages

setup(
    name='PyTensorCompletion',
    version='0.0.1dev',
    description='PyTensorCompletion',
    author='Chia-Chi Chang, Yin-Chen Liao, Hao-Chih Lee',
    author_email='c3h3.tw@gmail.com, qmalliao@gmail.com, howchihlee@gmail.com',
    packages=find_packages(),
    package_data={'': ['*.coffee']},
    install_requires=["numpy",
                      "scipy",
                      "pandas",
                      "scikit-learn",
                      "pymongo"],
)
