# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-authentication
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
from wangsu.authentication.models import *

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
| Createuser | 创建一个本地用户 | POST | /api/securelink/idaas/user |
| Deletegroup | 删除一个本地用户组信息，删除组及组内的用户与子组。 | DELETE | /api/securelink/idaas/usergroup |
| Creategroup | 创建一个本地用户组 | POST | /api/securelink/idaas/usergroup |
| Modifygroup | 修改一个本地用户组信息 | PUT | /api/securelink/idaas/usergroup |
| Listgroups | 获取指定用户组下的子组列表 | GET | /api/securelink/idaas/usergroup/list |
| Listusers | 查询指定用户组的用户列表 | GET | /api/securelink/idaas/user/list |
| Deleteuser | 删除一个本地用户信息 | DELETE | /api/securelink/idaas/user |
| Modifyuser | 修改一个本地用户的信息 | PUT | /api/securelink/idaas/user |
| Describeuserinfo | 查询一个用户的信息 | GET | /api/securelink/idaas/user |
| Syncauthconfig | 手动同步身份源 | POST | /api/securelink/idaas/authconfig/sync |