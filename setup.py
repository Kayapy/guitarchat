from setuptools import setup, find_packages

setup(
    name='guitarchat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'streamlit',
        'python-dotenv',
        'github',
        # outras dependências, se houver
    ],
)
