from setuptools import setup


setup(
    name='cldfbench_bdproto',
    py_modules=['cldfbench_bdproto'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bdproto=cldfbench_bdproto:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
