# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-nghostnames
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
from wangsu.nghostnames.models import *

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
| GetListOfHostnamesThatHaveBeenDeployed | 获取已部署到演练或生产环境的加速项目对应的加速域名列表。 | GET | /cdn/hostnames |
| GetHistoricalInformationAboutHostnames | 该接口用来查询在某段时间段内成功部署到生产或演练环境中的加速域名列表。 | GET | /cdn/hostnames/historical |
| GetHistoricalInformationAboutOneHostname | 该接口用来查询加速域名在生产和演练环境的历史部署信息。可通过查询参数指定查询起止时间。 | GET | /cdn/hostnames/historical/* |
| GetInformationAboutASpecificHostname | 该接口可用来查询已部署的加速域名的详细信息。 | GET | /cdn/hostnames/* |
| Querynghostnameandedgehostnameforwplus | 该接口用于查询cdnpro加速域名与真实服务域名关系。可以不传参数查询全部信息，也可通过提供cdnpro加速域名或真实服务域名查询指定信息，信息包括cdnpro加速域名和真实服务域名。 | POST | /api/ngcdn/hostname/edgehostname |