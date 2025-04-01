# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-webhooks
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
from wangsu.webhooks.models import *

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
| GetAListOfWebhooks | 获取已创建的webhook接口列表。当你创建部署任务，刷新任务，预取任务，或者配置验证任务时，都可以使用webhook接口来接收任务完成通知。 | GET | /cdn/webhooks |
| GetAWebhook | 该接口返回webhook接口的详细信息，包括webhook接口基本信息以及接口调用情况。 | GET | /cdn/webhooks/* |
| DeleteAWebhook | 删除webhook接口。删除后，如果有异步任务引用了该webhook接口，且任务仍在执行中，则任务执行完毕后不会触发webhook接口调用。 | DELETE | /cdn/webhooks/* |
| UpdateAWebhook | 更新webhook接口。只有请求体中携带的字段才会被更新。 | PATCH | /cdn/webhooks/* |
| CreateAWebhook | 创建webhook接口。当某个异步任务完成时，可用webhook接口来接收任务完成通知。当你创建部署任务，刷新任务，预取任务，或者配置验证任务时，都可以使用webhook接口来接收任务完成通知。 | POST | /cdn/webhooks |