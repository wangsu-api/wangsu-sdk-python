# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-secretmanagement
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
from wangsu.secretmanagement.models import *

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
| CreateASecret | 创建“保密信息”来存放敏感内容，避免敏感内容直接暴露在加速项目的边缘逻辑中。在边缘逻辑中使用$SECRET(secretName)语法来引用保密信息。 | POST | /cdn/secrets |
| GetAListOfSecrets | 获取保密信息列表。可使用查询参数筛选保密信息。 | GET | /cdn/secrets |
| GetASecret | 获取保密信息的详情，包括其在演练环境及生产环境中被使用的情况。 | GET | /cdn/secrets/* |
| UpdateASecret | 使用该接口更新保密信息。如果您修改了保密信息的名称，则以原有名称引用保密信息的加速项目版本将无法通过验证。此类加速项目版本必须移除对该保密信息的引用或者采用更新后的名称重新引用，才能通过验证。如果修改了保密信息存放的内容，则使用到该保密信息的加速项目在重新部署前必须进行重新验证。在保密信息更新后，在已部署加速项目中已引用的保密信息不会自动被更新。 | PATCH | /cdn/secrets/* |
| DeleteASecret | 删除保密信息。如果保密信息已在加速项目中使用，在删除保密信息之前，必须先从加速项目中解除引用，并重新验证和部署加速项目。 | DELETE | /cdn/secrets/* |