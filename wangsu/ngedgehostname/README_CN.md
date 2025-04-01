# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-ngedgehostname
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
from wangsu.ngedgehostname.models import *

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
| GetAnEdgeHostname | 该接口返回调度域名的详细信息，包含相关的访客分区规则和调度域名的操作记录。<br><br>调度域名的部署为异步操作。提交创建或修改调度域名的请求后，通常需要几分钟时间配置才能生效。您可以在'调度域名的操作记录'中查看部署状态。 | GET | /cdn/edgeHostnames/* |
| DeleteAnEdgeHostname | 使用该接口删除调度域名。如果您的DNS配置了 CNAME 记录指向该调度域名，那么您必须在删除调度域名之前更改DNS记录。否则，访问相关的加速域名将会报错。 | DELETE | /cdn/edgeHostnames/* |
| UpdateAnEdgeHostnameAll | 使用该接口全量更新调度域名。请确保指定调度域名所有相关的字段，包括那些不需要更改的字段。调度域名的部署为异步操作。提交配置修改的请求后，通常需要几分钟时间配置才能生效。您可以调用'查询调度域名详情'接口，在'操作记录'中查看部署状态。 | PUT | /cdn/edgeHostnames/* |
| UpdateAnEdgeHostnamePart | 使用该接口对调度域名的部分字段进行更新。调度域名的部署为异步操作。提交配置修改的请求后，通常需要几分钟时间配置才能生效。您可以调用'查询调度域名详情'接口，在'操作记录'中查看部署状态。 | PATCH | /cdn/edgeHostnames/* |
| CreateAnEdgeHostname | 使用该接口创建调度域名，自定义规则处理不同访客分区的请求。您必须在DNS创建一条CNAME记录，将您的加速域名指向调度域名，以便CDN Pro按照您定义的规则进行流量调度。<br><br>调度域名的部署为异步操作。提交创建调度域名的请求后，通常需要几分钟时间配置才能生效。请等待部署完成并确认配置生效后，再将您的加速域名指向调度域名。您可以调用'查询调度域名详情'接口，在'操作记录'中查看部署状态。 | POST | /cdn/edgeHostnames |
| GetAListOfEdgeHostnames | 获取调度域名的列表。 | GET | /cdn/edgeHostnames |
| GetAListOfIsps | 获取CDN Pro支持的运营商列表。这些运营商可在创建调度域名时用于定义访客分区规则。 | GET | /cdn/edgeHostnames/isps |
| Getclientregions | 获取CDN Pro支持的访客区域列表。这些访客区域可在创建调度域名时用于定义访客分区规则。 | GET | /cdn/edgeHostnames/clientRegions |