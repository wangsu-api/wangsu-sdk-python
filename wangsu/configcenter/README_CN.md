# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-configcenter
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
from wangsu.configcenter.models import *

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
| Createconfigmap | 创建configmap | POST | /api/v1/namespaces/*/configmaps |
| Listconfigmap | 获取configmap列表 | GET | /api/v1/namespaces/*/configmaps |
| Getconfigmap | 获取configmap的详细信息 | GET | /api/v1/namespaces/*/configmaps/* |
| Updateconfigmap | 更新configmap | PUT | /api/v1/namespaces/*/configmaps/* |
| Deleteconfigmap | 删除configmap | DELETE | /api/v1/namespaces/*/configmaps/* |
| Listsecret | 获取secret列表 | GET | /api/v1/namespaces/*/secrets |
| Getsecret | 获取secret的详细信息 | GET | /api/v1/namespaces/*/secrets/* |
| Createsecret | 创建secret | POST | /api/v1/namespaces/*/secrets |
| Updatesecret | 更新secret | PUT | /api/v1/namespaces/*/secrets/* |
| Deletesecret | 删除secret | DELETE | /api/v1/namespaces/*/secrets/* |
| Putpatchconfigmap | 部分更新configmap | PUT | /api/v1/namespaces/*/configmaps/*/ws/patch |
| Putpatchsecret | 部分更新secret | PUT | /api/v1/namespaces/*/secrets/*/ws/patch |
| Gettoken | 获取认证token | GET | /openapi/custom/api/v1/token |