# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-appmanage
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
from wangsu.appmanage.models import *

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
| Manageephoneapp | 指定边缘云手机实例进行应用操作，包括应用安装、卸载、启动停止及清除数据。 | POST | /ephone/apps/action |
| Queryapplist | 获取指定边缘云手机实例的应用列表。 | GET | /ephone/apps/list |
| Addtunnelapplications | 该接口用于新增隧道访问应用。用户可以指定应用的名称、内容。在需要将应用授权给用户前，需要先完成应用的创建。 | POST | /api/securelink/idaas/tunnelapp/add |
| Updatetunnelapplications | 该接口用于修改隧道访问应用。用户可以修改应用的名称、内容。在应用信息（IP、域名变更）有变更时，可以使用该接口进行修改，以便用户可以正常访问应用。 | POST | /api/securelink/idaas/tunnelapp/update |
| Updatewebapplications | 该接口用于修改隧道访问应用。用户可以修改应用的名称、内容。在应用信息（IP、域名变更）有变更时，可以使用该接口进行修改，以便用户可以正常访问应用。 | POST | /api/securelink/idaas/webapp/update |
| Addwebapplications | 该接口用于新增Web访问应用。用户可以指定应用的名称、内容。在需要将应用授权给用户前，需要先完成应用的创建。 | POST | /api/securelink/idaas/webapp/add |
| Deletewebapplications | 该接口用于删除Web访问应用。在Web访问应用下架后，可以使用该接口删除应用。删除Web访问应用前，需要确保该应用未被使用（例如，未授权给用户），否则会删除失败。 | POST | /api/securelink/idaas/webapp/delete |
| Deletetunnelapplications | 该接口用于删除隧道访问应用。在隧道访问应用下架后，可以使用该接口删除应用。删除隧道访问应用前，需要确保该应用未被使用（例如，未授权给用户），否则会删除失败。 | POST | /api/securelink/idaas/tunnelapp/delete |
| Queryapplicationdetail | 该接口用于查询隧道访问应用或web访问应用的详细信息。可以使用该接口查询应用的内容、应用管理员、关联的权限组，直接授权的用户/用户组。 | POST | /api/securelink/idaas/application/query |
| Authorizeapplicationforuser | 该接口用于将指定的应用直接授权给用户/用户组，可以为应用追加授权用户或覆盖应用已授权的用户。直接将应用授权给用户，方便企业管理员管理应用权限。 | POST | /api/securelink/idaas/application/grantToUser |
| Authorizeuserapplication | 该接口用于为指定的用户直接授权应用，可以给用户追加授权应用或覆盖用户已授权的应用。直接给用户授权应用，方便企业管理员管理用户应用权限。 | POST | /api/securelink/idaas/application/user-bind |
| Describeauthorizedapplicationsofuser | 该接口用来查询指定用户当前已授权的应用列表。管理员需要确认某个用户已授权的应用时，可以使用该接口查询，确定用户的应用权限范围是否合理。 | POST | /api/securelink/idaas/application/user-resource |
| Createapp | 创建应用，用于接入Android或者iOS的应用，返回应用ID。 | POST | /mah/v1/app/create |
| Adddebugfingerprint | 添加调试指纹，用于应用调试，仅限Android应用。 | POST | /mah/v1/app/add-debug-fingerprint |
| Deleteapp | 删除应用，指定应用ID删除对应应用 | POST | /mah/v1/app/delete |