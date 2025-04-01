# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-domainmanagement
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
from wangsu.domainmanagement.models import *

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
| Cancelapidomainservice | 取消指定域名的CDN加速服务，即从DNS层面强制让域名请求直接回源。多用于客户不及时响应处理涉黄网站。 | PUT | /api/domain/*/cancel |
| Restoreapidomainservice | 恢复指定域名的CDN加速服务，即从DNS层面让域名请求回到CDN节点。 | PUT | /api/domain/*/restore |
| Enablesingledomainservice | 启用某个状态为“禁用”的加速域名，使用已有的配置提供加速服务。 | PUT | /api/domain/*/enable |
| Disablesingledomainservice | 禁用指定加速域名，禁用后加速域名的请求将被直接拒绝，不会回源。 | PUT | /api/domain/*/disable |
| Deleteapidomainservice | 删除已添加的某个加速域名。删除后不能启用，只能重新创建加速域名。 | DELETE | /api/domain/* |
| Getfuzzypagingdomainlist | 查询用户账号下所有的、或者指定的加速域名和状态，每个加速域名包含概要信息，返回的加速域名列表按照首字母顺序排序。 | POST | /api/domain/domainList |
| Querydomainbyoriginip | 查询用户账号下，源站IP对应的所有域名名称列表。 | GET | /api/originaldomainlist |
| Createdomain | 为指定的域名申请加速服务 | POST | /api/domain |
| Queryapidomainlistservice | 查询用户账号下所有的、或者指定cname-label的加速域名和状态，每个加速域名包含概要信息，返回的加速域名列表按照首字母顺序排序。<br>请注意：禁用的域名（即enabled值为false）不可修改。 | GET | /api/domain |
| Querycustomerdomainnamegroupservice | 该接口用于查询客户的域名组下的域名信息。用户可以通过该接口检索一个或多个域名组。接口返回每个域名组的基础信息及其包含的域名列表。该接口适用于需要管理多个域名组的场景，有助于用户根据不同业务场景获取对应业务域名集。 | POST | /api/report/domainlist/domain |
| Queryapidomainattribution | 查询域名列表 | GET | /api/domainlist |
| Controldomain | 用于批量启停域名 | POST | /clouddns/Controldomain |
| Deldispatchdomain | 删除调度域名后，相关配置一并删除，调度失效。 | POST | /clouddns/Deldispatchdomain |
| Adddomain | 用于添加域名。CloudDNS支持批量添加多个域名 | POST | /clouddns/Adddomain |
| Deletedomain | 域名删除时是将域名的配置全部删除 | POST | /clouddns/DelDomain |
| Adddispatchdomain | 添加域名，生成调度cname，从域名注册商处填入调度cname，实现调度功能。 | POST | /clouddns/Adddispatchdomain |
| Querydispatchdomains | 域名数较多时，可通过分页查询展示域名信息，包括域名名称、调度CNAME、策略数。 | POST | /clouddns/Querydispatchdomains |
| Querydomains | 用于查询用户的域名及域名信息 | POST | /clouddns/Querydomains |
| Dispatchwarnlog | 查询调度告警日志 | POST | /clouddns/Dispatchwarnlog |
| Updatedispatchdomain | 编辑调度域名 | POST | /clouddns/Updatedispatchdomain |
| Controldispatchdomain | 启停调度域名 | POST | /clouddns/Controldispatchdomain |
| Channelaccetype | 查询客户频道及其加速类型 | POST | /myview/Channelaccetype |
| Adddomaingroup | 域名组可将域名进行分组，便于您可快捷分组查询域名的相关数据。<br>本API提供新增域名组功能 | POST | /api/report/domainlist/domaingroup/add |
| Editdomaingroup | 域名组可将域名进行分组，便于您可快捷分组查询域名的相关数据。<br>本API提供修改域名组内关联的域名功能 | POST | /api/report/domainlist/domaingroup/edit |
| Getpagingdomainlist | 查询用户账号下所有的、或者指定的加速域名和状态，每个加速域名包含概要信息，返回的加速域名列表按照版本排序。<br> | POST | /api/domain/list |
| Querycustomeranycastipforwplus | 查询客户AnycastIP | GET | /api/anycast-ips |
| Predeploychangeserverconfig | 通过接口自助预部署【接入域名跳转】配置。接口url的*可为域名名称或域名id。 | PUT | /api/predeploy/changeserver/* |
| Updatechangeserver | 通过接口自助修改【接入域名跳转】配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/changeserver/* |
| Querychangeserver | 通过接口自助查询【接入域名跳转】配置。接口url的*可为域名名称或域名id。 | GET | /api/config/changeserver/* |
| Enablecdndomainservice | 启用某个状态为“禁用”的加速域名，使用已有的配置提供加速服务。 | PUT | /cdn/domains/*/enable |
| Disablecdndomainservice | 禁用指定加速域名，禁用后加速域名的请求将被直接拒绝，不会回源。 | PUT | /cdn/domains/*/disable |
| Deletecdndomainservice | 删除已添加的某个加速域名。删除后不能启用，只能重新创建加速域名。 | DELETE | /cdn/domains/* |
| Updatecustomeranycastiprecordstatus | 修改Anycast IP的record status | POST | /api/anycast-ips/record-status |
| Deletehwdomain | 删除已经添加的某个华为云加速域名，通过在URI指定域名可以实现删除华为云加速域名，删除后域名将停止加速该域名。例如：/v1/domain/www.test.com。 | DELETE | /v1/domain/* |
| Enabledisablehwdomain | 启用/停用华为云域名。例如：state传入online，表示启用域名。state传入offline，表示停用域名。 | PUT | /v1/domain/*/state |