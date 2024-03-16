from setuptools import find_packages, setup

setup(
    name='Medical Chatbot',
    version='0.0.1',
    author='Nitanshu Kumar',
    author_email='nishu1547@gmail.com',
    packages=find_packages(),
    install_requires=['ctransformers',
                      'sentence-transformers==2.2.2',
                      'pinecone-client',
                      'langchain',
                      'flask',
                      'pypdf',
                      'python-dotenv',
                      'huggingface',
                      'openai',
                      'langchain-community']
)
