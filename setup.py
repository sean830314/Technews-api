from setuptools import setup

version='0.1'

# with open('README.md', 'r') as f:
#     readme = f.read()


# with open('LICENSE', 'r') as f:
#     license = f.read()

INSTALL_REQUIRES = (
    'protobuf==3.11.3',
    'grpcio==1.27.1',
    'grpcio-tools==1.27.1',
    'googleapis-common-protos==1.51.0',
)

setup(
    name='technews-api',
    version=version,
    description='TechNews API interfaces',
    # long_description=readme,
    long_description_content_type="text/markdown",
    author='Kroos.Chen',
    author_email='support@prophetstor.com',
    urls='https://github.com/containers-ai/api',
    license=license,
    packages=['technews_api.v1alpha1.search',
              'technews_api.v1alpha1.search.category',
              'technews_api.v1alpha1.search.article',
              'technews_api.v1alpha1.search.common'],
    package_dir={
        'technews_api.v1alpha1.search': 'technews_api/v1alpha1/search',
        'technews_api.v1alpha1.search.category': 'technews_api/v1alpha1/search/category',
        'technews_api.v1alpha1.search.article': 'technews_api/v1alpha1/search/article',
        'technews_api.v1alpha1.search.common': 'technews_api/v1alpha1/search/common',
    },
    install_requires=INSTALL_REQUIRES,
    zip_safe=False
)