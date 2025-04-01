# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-ipcheck
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
from wangsu.ipcheck.models import *

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
| Querycdnservicerealip | 该接口用于获取CDN服务的真实IP列表，特别适用于源站设置了白名单限制的场景。用户可以通过调用此接口获得我司提供的CDN节点用于回源的IP白名单，以便正确配置并确保数据请求能够通过CDN顺利到达源站。 | GET | /api/si/report/whiteip-list |
| Queryspecificipbelong | 该接口用于查询给定IP地址是否属于我司CDN IP。用户需提供IP地址列表。返回结果包含每个IP地址是否归属于我司CDN IP。 | POST | /api/si/tools/ipCheck |
| Ipinfoservice | 该接口用于查询特定IP地址的归属信息。用户可以通过提供一个或多个IP地址来查询它们是否为公司CDN节点，以及其归属的国家、省份、城市和运营商信息。返回结果包括是否为公司CDN节点的标识，如不是公司CDN的节点，该接口将返回未知。此接口适用于当用户查询IP是否我司IP。 | POST | /api/tools/ip-info |
| Checkiscuswhiteip | 本接口主要是提供给客户查询指定ip，是否为客户提供服务节点的ip。<br>查询指定的ip是否是实际在用的服务节点资源池ip，如果是返回ip;yes,否返回ip:no | GET | /task/api/customers/whitelist-check |