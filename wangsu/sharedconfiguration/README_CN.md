# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-sharedconfiguration
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
from wangsu.sharedconfiguration.models import *

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
| Listsharedwafruleexceptions | 获取共享配置WAF规则例外。 | POST | /api/v1/waf/share/exception/get-list |
| Createsharedwafruleexception | 新增共享配置的WAF规则例外。 | POST | /api/v1/waf/share/exception/create |
| Updatesharedwafruleexception | 修改共享配置的WAF规则例外。 | POST | /api/v1/waf/share/exception/update |
| Deletesharedwafruleexception | 删除共享配置的WAF规则例外。 | POST | /api/v1/waf/share/exception/delete |
| Createcustomaction | 新增自定义处理动作，最多可配置5个自定义响应动作。 | POST | /api/v1/share-action/add-customize-act |
| Listcustomactions | 获取自定义处理动作列表。 | POST | /api/v1/share-action/get-customize-act-list |
| Updatecustomaction | 修改自定义处理动作。 | POST | /api/v1/share-action/update-customize-act |
| Deletecustomactions | 删除自定义处理动作。注意：无法删除已被引用的自定义处理动作。 | POST | /api/v1/share-action/delete-customize-act-batch |
| Createsharedwhitelistrule | 新增共享配置的白名单规则。 | POST | /api/v1/common/share-whitelist/add |
| Updatesharedwhitelistrule | 修改共享配置的白名单规则。 | POST | /api/v1/common/share-whitelist/update |
| Deletesharedwhitelistrule | 删除共享配置的白名单规则。 | POST | /api/v1/common/share-whitelist/delete |
| Listsharedwhitelistrules | 获取共享配置的白名单规则 | POST | /api/v1/common/share-whitelist/get-list |
| Createsharedratelimitingrule | 新增共享配置的频率限制规则。 | POST | /api/v1/share-rate-limit/add-rule |
| Updatesharedratelimitingrule | 修改共享配置的频率限制规则。 | POST | /api/v1/share-rate-limit/update-rule |
| Deletesharedratelimitingrule | 删除共享配置的频率限制规则。 | POST | /api/v1/share-rate-limit/delete-by-ids |
| Listsharedratelimitingrules | 获取共享配置的频率限制规则。 | POST | /api/v1/share-rate-limit/get-rule-list |
| Createappapiexceptionfeature | 新增共享配置-APP/API例外特征。 | POST | /api/v1/dms/service-feature/add |
| Queryappapiexceptionlist | 查询共享配置-APP/API例外的列表。 | POST | /api/v1/dms/service-feature/get-list |
| Deleteappapiexceptionfeature | 删除共享配置-APP/API例外特征。 | POST | /api/v1/dms/service-feature/delete |
| Queryappapiexceptionfeaturedetail | 查看共享配置-APP/API例外特征详情。 | POST | /api/v1/dms/service-feature/get-detail |
| Queryappapiexceptionfeaturereferencedhostnames | 查看共享配置-APP/API例外特征关联的域名列表。 | POST | /api/v1/dms/service-feature/get-relate-domain-list |
| Updateshareconfigurationsappapiexceptionfeature | 修改App/API例外（共享配置）。 | POST | /api/v1/dms/service-feature/update |
| Listsharedcustomrules | 获取共享配置的自定义规则。 | POST | /api/v1/share-customize-rule/get-list |
| Disassociateshareratelimit | 解除共享配置的频率限制规则与域名的关联。 | POST | /api/v1/common/share-rate-limit/disassociate |
| Associateshareratelimit | 将共享配置的频率限制规则与域名的关联。 | POST | /api/v1/common/share-rate-limit/associate |
| Associatesharecustomizerule | 将共享配置的自定义规则与域名的关联。 | POST | /api/v1/common/share-customize-rule/associate |
| Disassociatesharecustomizerule | 解除共享配置的自定义规则与域名的关联。 | POST | /api/v1/common/share-customize-rule/disassociate |
| Associatesharecustomizebots | 将共享配置的定义Bot与域名的关联。 | POST | /api/v1/common/share-customize-bots/associate |
| Disassociatesharecustomizebots | 解除共享配置的自定义Bot与域名的关联。 | POST | /api/v1/common/share-customize-bots/disassociate |
| Associatesharedwhitelistrule | 将共享配置的白名单规则与域名的关联。 | POST | /api/v1/common/share-whitelist/associate |
| Disassociatesharedwhitelistrule | 解除共享配置的白名单规则与域名的关联。 | POST | /api/v1/common/share-whitelist/disassociate |
| Associatedmsshareservicefeature | 将共享配置的APP/API例外与域名的关联。 | POST | /api/v1/dms/service-feature/relateDomains |
| Disassociatedmsshareservicefeature | 将共享配置的APP/API例外与域名解除关联。 | POST | /api/v1/dms/service-feature/disRelateDomains |