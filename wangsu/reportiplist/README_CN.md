# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-reportiplist
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
from wangsu.reportiplist.models import *

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
| Reportserveripispprovinceservice | 查询CDN在各ISP各省份的服务IP列表 | POST | /api/report/server-ip/isp-province |
| Reportserveripexistflowservice | 该接口可以通过提供CDN的域名来获取对应的有流量的CDN服务IP列表。此功能适用于需要了解域名实际加速使用服务IP的场景。 | POST | /api/report/server-list/exist-flow |
| Querycdniplist | 该接口用于查询CDN服务中每个指定的域名对应的覆盖节点IP列表。用户可以通过提交相关请求获取其账号下多域名的节点IP信息，主要用于流量调度和优化管理。返回的数据显示了每个域名的详细覆盖节点IP，帮助用户了解和监控CDN服务的节点分布。 | POST | /api/report/server-list |
| Reportserverlistservice | 该接口用于查询特定域名在CDN服务中的IP列表及其归属运营商和区域信息。通过该接口，用户可以获取与域名相关联的CDN服务节点的详细信息。 | GET | /api/report/server-list/ip-isp-area |