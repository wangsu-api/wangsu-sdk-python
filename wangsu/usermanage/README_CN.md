# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-usermanage
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
from wangsu.usermanage.models import *

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
| Addsubaccount | 新增子账号 | POST | /sub-account |
| Querysubaccountinfo | 根据子用户登录名查询账号信息 | GET | /sub-account/* |
| Getsubaccountlist | 通过主账号获取其下的子用户列表 | POST | /sub-account/list |
| Updatesubaccount | 修改指定子用户的账号基本信息 | PUT | /sub-account |
| Deletesubaccount | 删除指定的子用户 | DELETE | /sub-account/* |
| Querypolicyattachedmainaccountorsubaccount | 该接口用于查询指定用户已关联的权限策略列表。用户通过输入其登录名可以获得与之关联的策略信息，该信息包括策略的ID、名称、描述内容、类型（系统策略或自定义策略）等，支持多语言国际化描述。接口返回的结果包含状态码和相关信息，以帮助用户了解策略的具体属性和分类。这在管理用户权限和制定或修改权限策略时非常有用，帮助系统管理员更高效地进行权限配置和调整。 | GET | /user/policy-attached/* |
| Batchaddorrevokepolicytosubaccount | 该接口用于为指定的子用户批量添加或撤销权限策略，通过输入子用户的登录名以及权限策略的标识列表，可以选择执行添加或撤销操作。添加权限时，系统会为子账号增加相应策略，以扩展其权限范围；而在撤销权限时，则会移除指定的策略，减少子账号的访问权限。返回值包括请求状态码和操作信息提示，用户可以通过这些信息确认批量操作的成功与否。此接口适用于需要集中管理子账号权限的场景，简化权限的批量调整过程。 | POST | /user/policies |
| Checkloginnamelegal | 校验登录名是否合法接口 | POST | /login-name/check |
| Addaccountident | 新增账号的aksk，一个账号下最多可有5对aksk。主账号可以新增主账号及其子账号的aksk列表，子账号可以新增同父子账号的aksk。 | POST | /account-ident |
| Deleteaccountident | 删除账号的aksk。主账号可以删除主账号及其子账号的aksk列表，子账号可以删除同父子账号的aksk。 | DELETE | /account-ident/* |
| Updateaccountident | 更新账号的aksk启用/禁用状态。主账号也可更新子账号的aksk。 | PUT | /account-ident |
| Listaccountident | 查看账号的aksk列表。即主账号可以查看主账号及其子账号的aksk列表，子账号可以查看同父子账号的aksk。<br> | POST | /account-ident/list |
| Queryagentassociatedmainaccountservice | 该接口用于查询多层级代理商账号与其关联主账号的关系。通过该接口，用户可以了解每个代理商账号的主账号详细信息，包括主账号的显示名、登录名，以及其对应的父主账号登录名。用户在调用此接口时会接收到关于请求状态的代码和信息，确保查询执行情况透明。此接口适用于需要管理和查询复杂层级代理账号关系的场景，有助于增强对账号管理的整体理解和控制。 | POST | /user/multilevel-agent/main-accounts |