# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-reportstatuscode
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
from wangsu.reportstatuscode.models import *

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
| Querystatuscodedistributionofeachispandprovince | 该接口查询多个域名在各运营商和省份的状态码分布。用户提供时间范围、域名列表，并可选运营商和省份。结果按域名、运营商、省份展示状态码分布，支持1分钟/5分钟/1小时粒度查询。支持`Accept-Language`请求头，仅支持`zh-CN`和`en-US`，默认`zh-CN`。`en-US`时，省份及运营商使用代码，否则返回中文。 | POST | /api/report/status-code/isp-province |
| Querystatuscodedistribution | 该接口用于统计多个域名的边缘状态码数据。用户可选择查询时间范围和域名列表获取数据。返回内容包括每个域名的状态码分布及其对应的请求数。有助于用户分析域名访问状态和优化内容分发策略的用户。 | POST | /api/report/status-code |
| Queryoriginstatuscodedistribution | 多域名的回源状态码统计，针对的是所有节点的回源数据。 | POST | /api/report/status-code/origin |
| Reportstatuscodenodeoriginservice | 该接口用于统计多域名在节点侧的回源状态码分布。用户提供查询的时间范围和域名列表，并可选是否按域名维度返回。返回结果包括域名在对应时间片的状态码及请求数。适用于需要监控和分析从节点回源请求状态码的场景。数据延迟在5~15分钟左右。 | POST | /api/report/status-code/node/origin |
| Reportstatuscoderealtimeoriginservice | 该接口用于查询域名的分钟级别的仅边缘回源状态码信息。用户需提供查询时间范围和域名列表，返回内容包括每个状态码的请求数和时间戳。有助于用户监控网站可用性，帮助优化服务质量。<br> | POST | /api/report/status-code/real-time/origin |
| Queryipv6statusofeachispandprovince | 该接口用于查询多域名在各省各ISP的IPV6状态码。用户可通过传递域名及选择具体的省份和运营商、IP协议类型来获取详细的状态码请求数信息。查询时间粒度可选5分钟/1小时。返回数据包括各域名在不同省份和ISP的详细状态码及请求数量。此接口适用于需要监控和分析网站在不同区域的指定IP协议的访问情况的场景。<br>支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商入参及返回都为code，否则返回的为中文。 | POST | /api/report/statusCode/isp-province/ipv6 |
| Reportstatusallservice | 该接口用于查询账号下所有域名的状态码汇总分布。用户提供查询时间范围来获取账号下所有域名的每个状态码对应的请求数。有助于用户了解所有业务的整体访问状况。 | GET | /api/report/status-code |
| Reportstatuscodeoriginfailrateservice | 该接口的功能是提供分钟级别的回源请求数和错误率的数据。用户需提供时间范围、域名和数据粒度，可以获取每分钟回源请求的总数、失败请求数及其失败率。有助于用户监控网站性能、从而提高服务质量和用户体验。<br> | POST | /api/report/status-code/origin/fail-rate |
| Queryrealtimeoriginstatuscode | 该接口用于查询指定时间范围内每分钟的回源请求状态码。用户需提供时间区间和域名列表，并可选择查询维度，如具体状态码或状态码类型（成功、重定向、服务器错误等）。返回数据包括请求时间和请求总数的详细信息。此接口用于监控网站健康状态，优化源站响应，帮助分析和调整网络架构，以提升服务稳定性和访客体验。 | POST | /api/report/status-code/real-time/origin/total |
| Queryispprovincestatuscode | 该接口查询特定省份和运营商的分钟级状态码统计。用户可设置起止时间、域名、状态码、省份和运营商等参数。返回每分钟状态码请求数及总请求数。支持`Accept-Language`请求头，仅支持`zh-CN`和`en-US`，默认`zh-CN`。若`Accept-Language`为`en-US`，省份及运营商参数和返回值为代码，否则为中文。 | POST | /api/report/status-code/isp-province/total |
| Reportstatuscoderealtimeedgeservice | 该接口用于查询边缘状态码的分钟粒度数据，用户可指定开始时间和结束时间以及域名查询状态码对应请求数数据。请求中可选数据粒度1分钟或5分钟。返回结果包括各状态码在每分钟请求数。 | POST | /api/report/status-code/real-time/edge |
| Reportflvstatuscoderealtimeorigintotalservice | 查询分钟级别的FLV回源状态码 | POST | /api/report/flv/status-code/real-time/origin/total |
| Reportflowprotocolstatuscodeservice | 该接口用于查询多个域名在指定时间段内每5分钟各状态码的HTTP和HTTPS请求数量统计。用户输入开始和结束时间及域名，接口将返回域名的每5分钟状态码的HTTP和HTTPS请求数。 | POST | /api/report/status-code/protocol-version |
| Reportflowipversionstatuscodeservice | 该接口用于查询多个域名每5分钟粒度的IPV6和IPV4状态码数据。用户需提供查询时间范围和域名列表获取数据。返回内容包括域名下每个状态码的IPV4和IPV6的详细数据。此接口有助于用户监控和分析不同IP协议下的状态码分布，以优化网络性能和提高服务质量。 | POST | /api/report/status-code/ip-version |
| Reportflowprotocoloneminstatuscodeservice | 该接口查询多个域名的1分钟粒度HTTP和HTTPS状态码数据。用户指定时间范围和域名，获取状态码统计信息。返回结果包括每个域名的状态码列表、每个时间片对应的HTTP和HTTPS状态码请求数。支持查询最多180天的数据，数据延迟约5分钟。 | POST | /api/report/one-min/status-code/protocol-version |
| Reportstatuscodelogservice | 查询各频道每小时粒度状态码分布 | POST | /api/report/status-code/log |
| Querystatuscodedistributionincountries | 按国家粒度查询状态码分布情况(按服务IP归属) | POST | /api/report/status-code/country |
| Querystatuscodedistributionofeachispandprovincebyuserip | 查询多域名在各ISP各省份的状态码分布，省份运营商基于访客IP归属。 | POST | /api/report/status-code/isp-province/user-ip |
| Reportstatuscodeurltopservice | 用于查询域名及状态码下的TOP URL排行。数据时延：3小时 | POST | /api/report/domain/statuscode/url/top |