# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-reportvisitor
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
from wangsu.reportvisitor.models import *

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
| Querytotalnumberofuniqueipundersingledomain | 该接口用于查询单个域名内的各流名的独立IP数量。用户提供具体的域名和时间，获取在此期间指定流的信息（以天为粒度）。接口返回的结果包括域名及其下对应流名的独立IP统计信息。有助于用户了解每路流的访问者分布，从而优化流量配置或评估流媒体服务的使用情况。 | POST | /api/report/visitor/total/stream |
| Reportuvispprovinceservice | 该接口用于查询多域名在不同省份和运营商的独立访客IP数。用户可指定时间范围、域名、省份、运营商，并选择按域名、省份或运营商分组。结果帮助分析区域访问趋势，优化内容分发。支持Accept-Language头（仅zh-CN和en-US），默认为zh-CN。Accept-Language为en-US时，省份和运营商参数及返回为代码，否则为中文。 | POST | /api/report/uv/isp-province |
| Reportiptopdetailsservice | 查询多域名的5分钟明细的访客 TOP IP | POST | /api/report/ip/top-details |
| Reportreferrertopdetailsservice | 这个接口用于查询域名每5分钟的TOP访客来源详情。用户需提供域名以及时间范围，返回内容包括每个refer来源的详细数据，可选值包含流量、带宽和请求数。该接口有助于用户分析站点流量，从而做出相应的业务决策。<br> | POST | /api/report/referrer/top-details |
| Reporturltopdetailsservice | 该接口用于统计多域名5分钟内的TOP URL信息。用户需提供时间范围和域名。返回内容包括域名的TOP URL的流量或带宽 或请求数信息。有助于用户了解热门访问链接，从而进行资源配置优化。 | POST | /api/report/url/top-details |
| Reportvisitorcustomtopdailyservice | 查询天粒度访客IP的自定义TOP排行 | POST | /api/report/visitor/custom-top/daily |