<p align="center">
<a href="https://www.wangsu.com/"><img src="https://static-wcs.wangsu.com/portalnav/navLogo_1720611253498_152_网宿logo-23_512.png" height="400" ></a>
</p>
<h1 align="center">WangSU  SDK for Python</h1>

# 目录
1. [简介](#简介)
2. [安装](#获取安装)


# 简介

欢迎使用网宿科技开发者工具套件（SDK），此 SDK 是网宿OpenApi平台的配套开发工具。

## 通过 pip 安装(推荐)

通过pip方式安装或更新请在命令行中执行以下命令:
```bash
pip install --upgrade wangsu-sdk-python  # 可选
```
### 安装指定产品 SDK（推荐）
例如：安装指定产品包
```bash
pip install --upgrade wangsu-sdk-python-指定产品分类包名缩写  # 如 usermanage接口分类包：wangsu-sdk-python-usermanage
```
具体接口分类的包名缩写请参考 [products.md](./products.md) 中的包名字段。

### 安装全产品 SDK
```bash
pip install --upgrade wangsu-sdk-python
```
全产品 SDK 包含了所有云产品的调用代码，推荐安装指定产品 SDK。

### 注意事项
- 安装全产品 SDK 和安装指定产品的 SDK 两种方式只能选择其中一种。
- 推荐使用python3 环境
具体产品的包名缩写和使用方法请参考 [products.md](./products.md) 中的包名字段。

## 支持产品列表
参见 [产品列表](products.md)