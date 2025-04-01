# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-edgekv
```


## 要求

- Python 3.6 或更高版本
- 依赖项：
  - requests >= 2.10.0
  - alibabacloud_tea >= 0.3.3
  - alibabacloud_tea_openapi >= 0.3.6
  - alibabacloud_tea_console >= 0.0.1
  - alibabacloud_tea_util >= 0.3.8

## 快速开始

### 示例

SDK 使用 AKSK 认证。您需要配置您的访问密钥和密钥：

```python
import json
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.edgekv.models import *

# 参考本文档最后的API列表，修改一下对应的{ActionName}、Method、Uri
request = {ActionName}Request()

aksk_config = AkSkConfig()
aksk_config.access_key = "YOUR_ACCESS_KEY"
aksk_config.secret_key = "YOUR_SECRET_KEY"
aksk_config.uri = "/your/api/path"
aksk_config.method = "GET"  # HTTP method: GET, POST, PUT, DELETE, etc.

# Convert request to JSON and make the API call
response = AkSkAuth.invoke(aksk_config, json.dumps(request.to_map()))
print(response)

```


## API列表
有关详细的 API 文档和可用方法，请参阅[官方 Wangsu API 文档](https://www.wangsu.com/document/api-doc/Overview?productType=all)。

| ActionName | description | client_methods | uri |
| --- | --- | --- | --- |
| Deletekeyvalue | 从指定空间删除 key value | DELETE | /edgekv/kv |
| Setkeyvalue | 从NameSpace（存储空间）里写入Key及其对应的Value数据。 | PUT | /edgekv/kv |
| Getkeyvalue | 从指定空间查询key value | POST | /edgekv/kv |
| Createshorturl | 短网址生成接口<br><br><br>短链方案基于EdgeKV实现。需要先开通EdgeKV 并创建全局模式的空间。 | POST | /short-urls/create |
| Getshorturl | 短网址查询接口 | POST | /short-urls/query |
| Delshorturl | 短网址删除接口 | POST | /short-urls/del |
| Ecakvinfo | 查询边缘KV存储信息，包括：存储量、读请求数、写请求数、删请求数 | POST | /myview/Ecakvinfo |
| Sharkletvisit | 边缘应用请求数，包括基础应用请求数、中型应用请求数、特殊应用请求数 | POST | /myview/sharkletVisit |