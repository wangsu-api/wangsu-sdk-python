# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-edgehostname
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
from wangsu.edgehostname.models import *

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
| Deleteedgehostname | 删除指定的调度域名。删除指的是卸载DNS部署，同时删除数据。仅未关联任何加速域名的调度域名才允许删除。注意：删除后无法恢复，请谨慎执行删除操作。 | DELETE | /api/edge-hostnames/* |
| Deployakcdnedgehostname | 部署指定的调度域名。部署指的是下发调度域名配置并使其DNS服务生效。部署后，使用此调度域名的加速域名可以正常使用CDN服务。同时，当您的调度域名部署状态为待部署、部署失败时，可使用此接口重新部署调度域名。 | POST | /api/edge-hostnames/*/deploy |
| Disableedgehostname | 禁用指定的调度域名的DNS服务。禁用后，使用此调度域名的加速域名将无法使用CDN服务。您可禁用DNS服务状态为已生效(active)的调度域名，禁用后的DNS服务状态将变更为挂起(inactive)。禁用不删除配置数据，禁用后的调度域名后可重新启用。注意：禁用前请确保您的加速域名CNAME未指向此调度域名，否则将影响您的加速服务。 | POST | /api/edge-hostnames/*/disable |
| Enableedgehostname | 启用指定的调度域名的DNS服务。启用后，使用此调度域名的加速域名可正常使用CDN服务。DNS服务状态为挂起(inactive)的调度域名才允许重新启用，启用后的DNS服务状态将变更为已生效(active)。 | POST | /api/edge-hostnames/*/enable |
| Queryedgehostname | 查询指定的调度域名的配置详情，包括：调度域名名称、调度域名描述、DNS服务状态、DNS部署状态、是否允许中国大陆加速、关联的加速域名列表、分区调度规则等。 | GET | /api/edge-hostnames/* |
| Queryedgehostnames | 查询调度域名列表，返回参数包括：调度域名名称、调度域名描述、DNS服务状态、DNS部署状态、是否允许中国大陆加速、关联的加速域名列表等。 | GET | /api/edge-hostnames |
| Updateedgehostname | 修改指定的调度域名的配置，支持配置分区调度规则。注意，此接口禁修改配置数据，修改完后您需再调用部署调度域名接口触发部署。 | PUT | /api/edge-hostnames/* |