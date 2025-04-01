# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-security
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
from wangsu.security.models import *

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
| Vmpcreatesshkey | 实例在创建时可以指定使用密钥对，在此之前需要先创建密钥对。 | POST | /vmp/osKeypairs |
| Vmpquerysshkey | 查询该用户的所有密钥对。 | GET | /vmp/osKeypairs |
| Vmpremovesshkey | 根据名称删除指定的密钥对。已使用该密钥对创建的实例不受影响，删除后无法在查询接口查到，也不能使用该密钥对创建新的实例。 | DELETE | /vmp/osKeypairs/* |
| Vmpquerysecuritygroup | 用于查询客户已创建的安全组基础信息。 | GET | /vmp/security-group |
| Vmpbindsecuritygroup | 用于变更实例与安全组的绑定关系，只有虚拟机实例支持绑定安全组，裸机实例不支持。<br>接口说明：<br>1）该接口是以虚拟机为粒度的全量更新接口，每次更新都会全量覆盖虚拟机的安全组绑定关系；<br>2）如果要增加一个（或多个）安全组绑定，则需要同时传递当前已绑定的安全组id加上新增的安全组id；<br>3）如果要移除一个（或多个）安全组绑定，则需要传递当前已绑定的安全组扣除要移除的安全组后的id；<br>4）如果要解除所有安全组绑定，则securityGroupIds传空数组即可；<br>5）当前已经绑定的安全组可以通过云主机查询接口获得；<br>6）接口支持批量实例，如果指定多个实例，部分实例更新安全组失败，不影响其他实例的更新。 | PUT | /vmp/security-group/server |
| Deletionsecuritygrouprules | 用于删除安全组规则信息。 | DELETE | /vmp/security-group/rule/* |
| Editsecuritygrouprules | 用于修改安全组规则信息。 | PUT | /vmp/security-group/rule |
| Addsecuritygrouprules | 用于添加安全组规则信息。<br>1）同一安全组内，不同规则内容不能完全一样；<br>2）批量添加多个规则时，结果为全部添加成功或全部添加失败。 | POST | /vmp/security-group/rule |
| Deletesecuritygroup | 用于删除安全组信息，如果安全组有定义了规则，则连同规则一起删除。<br>说明：<br>1）如果当前有实例绑定某安全组，则该安全组删除失败；<br>2）批量删除多个安全组时，如果某个安全组删除失败，不影响其他安全组的正常删除。 | DELETE | /vmp/security-group/* |
| Editsecuritygroup | 用于修改安全组名称或备注信息。 | PUT | /vmp/security-group |
| Addsecuritygroup | 用于添加一个安全组。 | POST | /vmp/security-group |