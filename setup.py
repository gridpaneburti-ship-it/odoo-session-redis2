import setuptools

setuptools.setup(
    name="odoo-session-redis",
    version="17.0.1.0.0",
    description="Store Odoo web sessions in Redis",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Camptocamp, Ali Abdelaal",
    license="AGPL-3",
    packages=["odoo.addons.session_redis"],
    package_dir={"odoo.addons.session_redis": "."},
    install_requires=["redis"],
    python_requires=">=3.10",
)
