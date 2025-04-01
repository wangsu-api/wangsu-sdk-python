# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-ngreports
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
from wangsu.ngreports.models import *

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
| GetEdgeTrafficVolume | 获取一段时间内的边缘流量数据（以MB为单位）。可以使用查询参数指定时间段和协议。通过在请求体中传递filters对象可进一步指定查询范围。该报表的数据延迟小于两分钟。<br> | POST | /cdn/report/vol |
| GetEdgeRequests | 获取一段时间内的边缘请求数数据。可以使用查询参数指定时间段和协议。通过在请求体中传递filters对象可进一步指定查询范围。该报表的数据延迟小于两分钟。 | POST | /cdn/report/req |
| GetEdgeBandwidth | 获取一段时间内的边缘带宽数据（以Mbps为单位）。可以使用查询参数指定时间段和协议。通过在请求中传递filters对象可进一步指定查询范围。此报表的数据延迟小于两分钟。 | POST | /cdn/report/bandwidth |
| GetOriginFastRouteTrafficVolume | 查询通过快速回源功能传输的回源流量。 | POST | /cdn/report/fastOriginVol |
| GetASummaryOfRequests | 获取一段时间内的请求数汇总数据。可以按加速域名或serverGroups（节点组）进行查询和分组。 | POST | /cdn/report/reqSummary |
| GetASummaryOfTrafficBandwidth | 获取一段时间内的带宽汇总数据。可以按加速域名或serverGroups（节点组）进行查询和分组。 | POST | /cdn/report/bandwidthSummary |
| GetOriginTrafficVolume | 获取一段时间内的回源流量数据（以MB为单位）。可以使用查询参数指定时间段和协议。通过在请求体中传递filters对象可进一步指定查询范围。此报表的数据延迟小于两分钟。<br><br>注意：该接口所返回的统计数据不包括TCP、IP和MAC报头的开销。 | POST | /cdn/report/volOrigin |
| GetEdgeStatusCodeDetails | 获取一段时间内的边缘状态码统计信息。可以使用查询参数指定时间段、协议和数据粒度。通过在请求体中传递filters对象可进一步指定查询范围。此报表的数据延迟最长可达30分钟。 | POST | /cdn/report/statusCodeDetails |
| GetTheNumberOfRequestsToOrigin | 获取一段时间内的回源请求数数据。可以使用查询参数指定时间段和协议。通过在请求体中传递filters对象可进一步指定查询范围。此报表的数据延迟小于两分钟。 | POST | /cdn/report/reqOrigin |
| GetOriginStatusCodeDetails | 获取一段时间内的回源状态码统计信息。可以使用查询参数指定时间段、协议和数据粒度。通过在请求体中传递filters对象可进一步指定查询范围。此报表的数据延迟最长可达30分钟。 | POST | /cdn/report/statusCodeDetailsOrigin |
| GetTheIntermediateTrafficVolume | 获取一段时间内的中间层流量数据（以MB为单位）。中间层流量是指CDN Pro缓存服务器之间的流量。可以使用查询参数指定时间段和协议。通过在请求体中传递filters对象可进一步指定查询范围。此报表的数据延迟小于两分钟。 | POST | /cdn/report/volInterm |
| GetTheEdgeUploadTrafficVolume | 获取一段时间内上传到CDN Pro边缘服务器的流量数据（以MB为单位）。可以使用查询参数指定时间段和协议。通过在请求中传递filters对象可进一步指定查询范围。此报表的数据延迟小于两分钟。<br><br>注意：该接口返回的数据中不包括TCP、IP和MAC报头的开销。 | POST | /cdn/report/upVol |
| GetASummaryOfStatusCodesReturnedByEdgeServers | 获取一段时间内CDN Pro边缘服务器返回的HTTP状态码的汇总数据。可以使用查询参数指定时间段和协议。在请求体中传递filters对象可进一步指定查询范围。此报告的数据延迟最长可达30分钟。 | POST | /cdn/report/edgeStatusSummary |
| GetASummaryOfStatusCodesReturnedByOriginServers | 获取一段时间内源站返回的HTTP状态码的汇总数据。可以使用查询参数指定时间段和协议。在请求体中传递filters对象可进一步指定查询范围。此报告的数据延迟最长可达30分钟。 | POST | /cdn/report/originStatusSummary |
| GetASummaryOfCpuUsage | 获取CPU使用时间汇总信息，包括边缘服务器和中间层服务器的数据。 | POST | /cdn/report/cpuSummary |
| GetOriginFastRouteRequests | 查询通过快速回源功能所产生的回源请求数。 | POST | /cdn/report/fastOriginReq |
| GetEdgeHostnameSummaryStatistics | 获取一段时间内一个或多个调度域名的DNS解析请求数汇总数据。可通过该接口查询每个调度域名的请求数数据。 | POST | /cdn/report/edgeHostnameReqSummary |
| GetCpuTimeUsed | 查询处理用户请求所消耗的CPU时间（以秒为单位）。 | POST | /cdn/report/cpuTime |
| GetASummaryOfTrafficVolume | 获取一段时间内的边缘、中间层（CDN Pro服务器之间）和回源流量的汇总数据。可以在请求体中指定加速域名或serverGroups（节点组）等参数进行查询和分组。<br> | POST | /cdn/report/volSummary |
| Getedgehostnamestatistics | 获取一段时间内对调度域名发起的DNS解析请求数。 | POST | /cdn/report/edgeHostnameReq |