# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-ngcertificate
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
from wangsu.ngcertificate.models import *

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
| CreateACertificate | 创建证书及其第一个版本。您可以上传私钥/公钥对来创建证书，或者选择生成自签名证书。 | POST | /cdn/certificates |
| GetListOfCertificates | 获取证书列表。接口返回证书的ID、名称、部署到生产环境的版本、部署到演练环境的版本、最新的版本号、证书的最后更新时间以及证书的过期时间等信息。 证书列表默认按证书的最后更新时间降序排序。 | GET | /cdn/certificates |
| GetACertificate | 获取证书的详细信息，包括证书的版本以及证书使用情况。 | GET | /cdn/certificates/* |
| UpdateACertificate | 您可以使用该接口来更新证书。相关字段与”创建证书”接口中的字段相同。 如果证书已在加速项目中使用且已部署到生产环境或演练环境，我们建议您调用“创建部署任务”接口来部署更新后的证书，否则CDN Pro仍会使用旧版本的证书来响应用户请求。 | PATCH | /cdn/certificates/* |
| DeleteACertificate | 该接口用来删除证书。当证书在生产环境或演练环境中使用时不可删除。 | DELETE | /cdn/certificates/* |
| DownloadTheCsr | 下载证书签名请求 (CSR) 文件 。您可以向证书颁发机构提交CSR，申请证书。申请到证书后，请调用“更新证书”接口更新证书到CDN Pro。 | GET | /cdn/certificates/*/csr |
| GetACertificateVersionsDetails | 获取某个证书版本的详细信息，包括到期日期、加密算法、私钥长度、指纹，以及是否在生产环境和演练环境中部署等信息。 | GET | /cdn/certificates/*/versions/* |