# Ubuntu Tensorflow object detection API 环境搭建与测试

## [anaconda][1] 环境搭建
### 下载
```
wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh
```

### 环境变量
```
vim ~/.bashrc
    export PATH=/root/anaconda3/bin:$PATH
source ~/.bashrc
```

## 安装依赖
### tensorflow
```
# For CPU
pip install tensorflow
# For GPU
pip install tensorflow-gpu
```

### libraries 
```
apt-get install protobuf-compiler python-pil python-lxml python-tk
pip install Cython
pip install jupyter
pip install matplotlib
```

## Tensorflow object detection API 
### 下载
```
git clone https://github.com/tensorflow/models
```

### 环境变量
```
vim ~/.bashrc
    export PATH=/root/models/research:$PATH
    export PATH=/root/models/research/slim:$PATH
source ~/.bashrc
```
Add Libraries to PYTHONPATH
```
# From tensorflow/models/research/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```
### Protobuf 编译
```
# From tensorflow/models/  
protoc object_detection/protos/*.proto --python_out=.  
```
## 测试
```
python object_detection/builders/model_builder_test.py  
```

#### 参考文献
[https://blog.csdn.net/dy_guox/article/details/79081499#commentsedit][2]
[https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md#protobuf-compilation][3]


[1]: https://www.anaconda.com/
[2]: https://blog.csdn.net/dy_guox/article/details/79081499#commentsedit
[3]: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md#protobuf-compilation