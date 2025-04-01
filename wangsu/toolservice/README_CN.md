# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-toolservice
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
from wangsu.toolservice.models import *

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
| Querybandwidthlimittasklistservice | 此接口用于查询账号下的带宽限制任务列表，返回所有有带宽的任务详细信息。返回内容包括域名、任务名称以及设置的最大带宽值。该接口适用于需要评估和管理流量控制策略的场景，帮助用户快速识别并管理当前设置的带宽限制任务。 | POST | /api/tools/queryBandwidthLimitTaskList |
| Icpqueryservice | 查询所指定的域名是否在中国大陆工信部进行备案。 | GET | /api/icp |
| Akamaiipforbiddenservice | 该接口用于封禁特定IP地址对AKAMAI服务的访问，用户可通过输入要封禁的IP列表来实现操作。此接口有助于用户阻挡不可信或有害IP地址的访问，提升网络安全性。<br> | POST | /api/tools/ip-forbid/akamai |
| Reportserveripcountrycodeservice | 该接口用于查询特定域名在不同国家的CDN服务IP列表。用户提供域名以及国家来获取信息。返回的数据包括每个域名在指定国家覆盖节点的IP列表。适用于用户有效查看CDN在全球范围内的覆盖和服务节点分布。 | POST | /api/report/service-ip/country |
| Akamaiippermitservice | 解封AKAMAI访问IP | POST | /api/tools/ip-permit/akamai |
| Forbidorresumevisitoripsbydomainservice | 对访问指定域名的IP，进行封禁解禁操作。 | POST | /api/spider/ip-forbid |
| Queryforbiddingvisitoripsbydomainservice | 查询域名粒度的封禁IP信息，支持分页查询。 | POST | /api/spider/ip-forbid/query |
| Ipdomainservice | 该接口用于根据IP地址查询正在使用该IP的域名。用户输入IP地址来获取与该IP相关联的域名列表。接口返回的信息包含IP当前使用状态，以及使用该IP的域名列表。在实际应用中，此接口可帮助用户检测特定IP的域名使用情况，适用于网络监控和管理。 | POST | /api/tools/ip/domain-list |
| Queryallbandwidthlimittasklistservice | 该接口用于查询用户账号下配置的所有带宽限制任务。用户在调用时可以选择是否包含任务所涉及的所有客户域名以及决定是否返回所有任务状态的信息。返回的数据以清单方式展示每个带宽限制任务的详细信息，包括任务名称、类别、状态以及相关控制策略和参数。此接口有助于用户管理带宽设置，可以及时对特定的流量和请求进行有效的控制和处理。 | POST | /api/tools/queryAllBandwidthLimitTaskList |
| Queryforbiddingvisitoripsbylabelcodeservice | 查询标签粒度的封禁IP信息，支持分页查询。 | POST | /api/spider/label-ip-forbid/query |
| Forbidorresumevisitoripsbylabelcodeservice | 一个客户可以创建一个标签，该标签可以关联若干域名，通过该标签进行封禁解禁访问IP的操作，效果等同于对该标签关联的所有域名，进行封禁解禁指定的访客IP。 | POST | /api/spider/label-ip-forbid/operate |
| Addorremoveforbiddingipwhitelistservice | 提供添加或删除封禁时的IP白名单的功能。所添加的白名单IP，视其粒度，将在进行“标签粒度”、“域名粒度”的封禁请求时被过滤。<br>支持下发以下三个粒度的IP白名单，分别为：<br>“客户粒度”：按客户粒度管理的IP白名单，作用于该客户下，所有生效的加速域名、生效标签，即对“标签粒度”、“域名粒度”的封禁请求均生效；<br>“域名粒度”：按域名粒度管理的IP白名单，作用于该生效的加速域名，即仅对“域名粒度”的封禁请求生效；<br>“标签粒度”：按标签粒度管理的IP白名单，作用于该生效标签，即仅对“标签粒度”的封禁请求生效；<br>新增时，可以同时解禁对应粒度下还处于封禁中的IP。 | POST | /api/spider/ip-whitelist/operate |
| Queryforbiddingipwhitelistservice | 提供查询封禁IP白名单列表的功能。 | POST | /api/spider/ip-whitelist/query |