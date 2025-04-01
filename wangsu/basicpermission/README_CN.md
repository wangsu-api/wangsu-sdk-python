# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-basicpermission
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
from wangsu.basicpermission.models import *

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
| Addterminalauth | 新增基础权限 | POST | /api/securelink/idaas/terminalauth |
| Updateterminalauth | 编辑基础权限. | PUT | /api/securelink/idaas/terminalauth |
| Deleteterminalauth | 根据ID删除基础权限 | DELETE | /api/securelink/idaas/terminalauth |
| Addterminalauthuserorgroup | 新增基础权限关联的用户/用户组 | POST | /api/securelink/idaas/terminalauth/user-group |
| Queryterminalauthlist | 获取基础权限列表 | GET | /api/securelink/idaas/terminalauth |
| Queryterminalauthinfo | 查询基础权限信息 | GET | /api/securelink/idaas/terminalauth/query |
| Removeterminalauthresource | 移除基础权限关联的应用 | DELETE | /api/securelink/idaas/terminalauth/related-resources |
| Removeterminalauthuserorgroup | 移除基础权限关联的用户/用户组 | DELETE | /api/securelink/idaas/terminalauth/user-group |
| Queryterminalauthresourcelist | 获取基础权限可关联的应用列表 | GET | /api/securelink/idaas/terminalauth/resources |
| Updateterminalauthrelatedresources | 修改基础权限关联的应用 | PUT | /api/securelink/idaas/terminalauth/related-resources |
| Queryterminalusergroupbyauthconfig | 根据身份源名称获取用户组列表. | GET | /api/securelink/idaas/usergroup/list-by-authconfig |
| Associaterightsgroupstouserorusergroup | 该接口用来直接为指定用户/用户组关联权限组。如果有多个用户/用户需要分配的多个一样的应用权限时，管理员可以先把多个应用关联到同一个权限组后，再使用该接口分配给用户/用户组。 | POST | /api/securelink/idaas/terminalauth/user-bind |