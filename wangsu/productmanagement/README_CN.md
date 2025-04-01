# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-productmanagement
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
from wangsu.productmanagement.models import *

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
| GetSystemConfiguration | 该接口返回CDN Pro系统配置信息，包括系统支持的边缘逻辑指令，高级功能，以及HTTP, HTTPS非标准端口等。有些功能，指令及端口并非默认开放。如果需要使用未开放的功能，指令及端口，请联系我们的技术支持团队开通。 | GET | /cdn/systemConfigs |
| GetIpAddressesOfTheCdn | 获取CDN Pro对外提供服务所使用的IP地址列表。如果源站采用了白名单机制进行访问控制，需要将这些IP地址加入白名单，从而允许CDN Pro服务器的回源请求。由于这些IP地址是动态变化的，建议定期查询（如每天查询一次）该接口获取最新的IP地址列表，并相应地更新白名单。需要注意的是，该IP列表仅包含CDN Pro父节点的IP地址，并未包括边缘节点的IP。因此，该回源IP加白的场景，仅适用于当回源方式配置了“不直连”（即源站配置中directConnection取值为"noDirect"），且边缘逻辑中未开启“origin_fast_route”快速回源功能的情况。 | GET | /cdn/publicIpList |
| GetAListOfOriginShields | 该接口用于查询shield列表。shield是CDN Pro边缘节点与您的源站之间的中间缓存层。使用shield可提高缓存命中率，减少回源流量。shield是高级功能，如果您需要使用该功能，请联系我们的技术支持。 | GET | /cdn/shields |
| GetAShieldByItsId | 该接口用于查询shield详细信息。shield是CDN Pro边缘节点与您的源站之间的中间缓存层。shield是高级功能，如果您需要使用该功能，请联系我们的技术支持。 | GET | /cdn/shields/* |
| CheckIfIpAddressesBelongToTheCdnProPlatform | 如果您需要知道某些IP地址是否来自CDN Pro，可调用该接口进行批量查询。 | POST | /ngadmin/ipDetails |
| GetOriginFastRouteIpList | 该接口返回CDN Pro快速回源服务器的IP列表。如果您开启了快速回源功能，可通过该接口查询快速回源IP。 | GET | /cdn/originFastRouteIpList |
| GetStagingServersList | 该接口用于查询CDN Pro演练环境的服务器列表。在您将加速项目部署到生产环境前，可先部署到演练环境进行验证。您可通过该接口获取演练环境的服务器信息，并指定某台服务器进行配置验证。 | GET | /cdn/stagingServers |