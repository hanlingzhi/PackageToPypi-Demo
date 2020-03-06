# 韩灵稚打包测试
Hanlingzhi's Package PyPi Demo
##工程结构说明
<pre>
.
├── LICENSE.txt    	// 证书文件
├── README.md		// MD文件
├── hanlingzhi
│   ├── __init__.py
│   └── math_h.py
├── setup.py			// 打包配置
└── string_h
    ├── __init__.py
    └── reverse.py
</pre>

##测试服务器打包流程

* 升级setuptools和wheel包
<pre>python3 -m pip install --user --upgrade setuptools wheel
</pre>

* 打包到本地文件
<pre>python3 setup.py sdist bdist_wheel
会生成build、dist、hanlingzhi_test.egg-info文件，其中dist文件就是制品
├── dist
│   ├── hanlingzhi-test-0.0.1.tar.gz
│   └── hanlingzhi_test-0.0.1-py3-none-any.whl
</pre>

* 分发到PyPi私服(pypi提供的测试版 test.pypi.org)，首先安装twine
<pre>
pip3 install twine
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: hanlingzhi  // 私服注册的用户名
Enter your password:                 // 私服注册的密码
Uploading hanlingzhi_test-0.0.1-py3-none-any.whl
100%|████| 7.96k/7.96k [00:16<00:00, 486B/s]
Uploading hanlingzhi-test-0.0.1.tar.gz
100%|████| 7.28k/7.28k [00:01<00:00, 4.34kB/s]
</pre>

* 下载依赖
<pre>
最好在虚拟环境下测试  python3 -m venv venv
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps hanlingzhi_test
Looking in indexes: https://test.pypi.org/simple/
Collecting hanlingzhi_test
  Downloading https://test-files.pythonhosted.org/packages/a7/ca/3e5ecda3c564a721642a756e31ec2f6f340067cfa4dddb119e2eb2c98dd0/hanlingzhi_test-0.0.1-py3-none-any.whl
Installing collected packages: hanlingzhi-test
Successfully installed hanlingzhi-test-0.0.1
</pre>

* 测试
<pre>
python3
>>> from hanlingzhi import math_h
>>> math_h.addition(3,4)
7			// 成功
</pre>

* 上传正式服务
<pre>
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
</pre>