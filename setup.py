import setuptools

# 官方打包链接  https://packaging.python.org/tutorials/packaging-projects/


# 读取MD作为说明
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # 包名
    name="hanlingzhi-test",
    # 版本(也可以用日期表示 2020.3.1 这样每次提交不需要在改版本)
    version="0.0.1",
    # 作者
    author="Han LingZhi",
    # 作者邮箱
    author_email="343651570@qq.com",
    # 包的说明(这个要正规,会展示出来, 列表页灰色横幅可见)
    description="验证打包功能的测试包, 请勿下载",
    # 项目描述
    long_description=long_description,
    # 模式的格式
    long_description_content_type="text/markdown",
    # 项目提供主页URL
    url="https://github.com/hanlingzhi/TF-ByScenario",
    # 许可证类型 https://choosealicense.com/ 可以选择证书类型
    license='MIT',
    # 程序包列表 package包会自动搜索
    packages=setuptools.find_packages(),
    # 关键词
    keywords='hanlingzhi package demo',
    # 分类器
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Operating System :: OS Independent",
    ],
    # 包依赖
    install_requires=['pytest'],
    # python版本依赖
    python_requires='>=3.6',
)