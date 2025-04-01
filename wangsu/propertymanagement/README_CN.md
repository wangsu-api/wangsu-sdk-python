# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-propertymanagement
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
from wangsu.propertymanagement.models import *

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
| GetAPropertyVersion | 获取加速项目版本的详细配置信息。 | GET | /cdn/properties/*/versions/* |
| UpdateAPropertyVersion | 该接口可用来更新加速项目版本。已部署到生产或演练环境的加速项目处于“冻结”状态，无法再次被更新或验证，该状态下的加速项目版本只有版本描述字段可被更新。 | PATCH | /cdn/properties/*/versions/* |
| DeleteAPropertyVersion | 删除一个加速项目版本。 | DELETE | /cdn/properties/*/versions/* |
| GetAProperty | 查询某个加速项目的信息，包括已创建的版本数以及哪些版本已部署等。 | GET | /cdn/properties/* |
| UpdateAProperty | 该接口用于更新加速项目的名称和描述。该操作不会创建加速项目新版本，也不会更新现有的加速项目版本。<br>如果要更改加速项目的配置，请调用“更新加速项目版本”接口。 | PATCH | /cdn/properties/* |
| DeleteAProperty | 根据ID删除加速项目。 | DELETE | /cdn/properties/* |
| GetListOfPropertyVersions | 获取加速项目版本列表。返回每个版本的摘要信息，包括其状态及关联的加速域名等。 | GET | /cdn/properties/*/versions |
| CreateAPropertyVersion | 创建一个新的加速项目版本。 | POST | /cdn/properties/*/versions |
| CreateAProperty | 创建加速项目，在加速项目中定义需要部署到CDN Pro服务器的一个或多个加速域名的配置。 | POST | /cdn/properties |
| GetListOfProperties | 该接口返回加速项目列表，包括每个加速项目的ID、最新版本号、注释、演练环境版本号、生产环境版本号，以及每个版本的最后更新时间等信息。可使用查询参数筛选加速项目。 | GET | /cdn/properties |