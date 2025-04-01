# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-certificationmanage
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
from wangsu.certificationmanage.models import *

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
| Querycertificatelist | ​查看SSL证书的列表及信息，包括证书ID、证书名称、是否共享、使用当前证书的域名信息等。 | GET | /api/ssl/certificate |
| Getcertificatecontent | 下载证书内容，包括：证书crt文件内容，证书key文件内容，证书ca文件内容。加密方式和上传方式一致。 | GET | /api/ssl/content/*/download |
| Addcertificateservicev2 | 新增证书接口，包括证书名称、证书公钥（crt和ca内容合并）、证书密钥、csrid、备注<br> | POST | /api/certificate |
| Deletecertificate | 删除SSL证书，如果查询证书还有关联域名在使用，则无法删除，需要使用【修改域名配置】接口解除域名与证书的关联。 | DELETE | /api/certificate/* |
| Querycertificateinfo | 根据证书ID查看证书详情。<br> | GET | /api/certificate/* |
| Editcertificatev2 | 修改客户证书，可重新上传证书。 | PUT | /api/certificate/* |
| Querycertificatecontent | 查看证书文件内容 | GET | /api/certificate/*/content |
| Querycertificaterelateddomains | 查看证书关联的加速域名 | GET | /api/certificate/*/domain |
| Revokecertificateserviceforwplus | 吊销证书接口 | POST | /api/certificate/revoke |
| Addgmcertificateforwplus | 新增国密接口 | POST | /api/certificate/gm/add |
| Querydomainmulticertconfig | 查询域名证书配置 | GET | /api/config/certificate/v2/* |
| Reissuecertificateforwplus | 该接口用于重颁发证书。可以通过提供证书ID、证书描述、证书算法、验证方式、是否自动验证、是否自动部署、通用名称、主体备用名称重颁发证书，调用成功时接口会返回销售订单id。 | POST | /api/certificate/reissue |
| Downloadconfirmlettertemplateforwplus | 该接口用于下载亚数诚信提供的《信息确认函》模板，用户可以通过《信息确认函》模板来输入用户的组织信息并盖章以使CA厂商核实信息是否真实。 | POST | /api/certificate/download/confirm/letter/template |
| Uploadconfirmletterforwplus | 该接口用于上传《信息确认函》，用户可以通过此接口上传组织信息，便于证书CA厂商确认组织信息是否合法。 | POST | /api/certificate/upload/confirm/letter |