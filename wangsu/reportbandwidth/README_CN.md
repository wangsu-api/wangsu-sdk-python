# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-reportbandwidth
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
from wangsu.reportbandwidth.models import *

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
| Queryp2pbandwidth | 查询CDN带宽、P2P带宽、总带宽和计费值 | POST | /myview/BandWidthP2p |
| Bandwidthchannelprotocol | 查询分协议带宽情况 | POST | /myview/Bandwidthchannelprotocol |
| Channelvaluesum | 按计费方式汇总频道计费值（域名列表、计费说明、计费值），查询周期内相同计费方式的域名带宽进行累加计费 | POST | /myview/Channelvaluesum |
| Bandwidthmiddle | 查询中间缓存带宽，输出分钟粒度的中间缓存带宽、动态hit、动态misss、静态hit、静态miss带宽 | POST | /myview/bandwidth-middle |
| Querydomainbandwidth | 该接口用于统计多个域名在指定时间内的带宽汇总信息。用户需提供加速域名及时间参数来生成汇总数据，返回内容包括每个时间片的带宽汇总数据。此接口有助于用户监控和分析域名的流量使用情况，以便更好地进行网络优化和成本控制。<br> | POST | /api/report/domainbandwidth |
| Billingorder | 查询客户正式订单计费信息，包括计费方式说明、计费值、详情等 | POST | /myview/Billingorder |
| Queryipv6bandwidthofeachispandprovince | 根据访客访问日志，查询域名在各ISP各省份不同IP类型的带宽<br>支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。 | POST | /api/report/bandwidth/isp-province/ipv6 |
| Getbandwidthlog | 查询客户的日志带宽（域名、分钟粒度的日志带宽） | POST | /myview/bandwidth-log |
| Bandwidthpeakranking | 对频道进行带宽峰值排行，输出按照峰值排行后的频道、峰值时间、峰值、总流量 | POST | /myview/bandwidth-peak-ranking |
| Bandwidthchannel | 查询域名带宽（域名、分钟粒度的带宽） | POST | /myview/bandwidth-channel |
| Reportbandwidthrealtimeedgeservice | 该接口用于查询多个域名分钟粒度的边缘带宽汇总数据。用户需要提供开始时间、结束时间、域名列表和期望的数据粒度。接口返回信息包括每分钟的边缘带宽值、峰值时间、峰值带宽以及总流量。接口有利于用户对多个域名的带宽、流量波动进行监测分析，从而优化带宽资源的使用和调整网络策略。 | POST | /api/report/bandwidth/real-time/edge |
| Querybandwidthbyispprovince | 该接口用于查询中国大陆访客IP在各省和ISP的带宽信息。用户可指定时间段、域名、地区和ISP等参数，获取5分钟粒度的带宽数据，以Mbps为单位。接口返回包括时间戳和相应带宽值，帮助用户分析不同地区和ISP的带宽使用情况，从而优化网络资源配置和提升用户体验。 | POST | /api/report/bandwidth/area/isp-province |
| Querybandwidthoforiginminutely | 该接口用于查询多域名的分钟级别回源带宽。用户需提供开始和结束时间，指定域名和数据粒度。返回结果包括每个域名的带宽峰值、回源总流量及每分钟的回源带宽。 | POST | /api/report/bandwidth/multi-domain/real-time/origin |
| Querybandwidthminutely | 该接口用于查询多个域名在分钟级别的实时带宽信息。用户需要提供时间跨度和域名列表，查询时间范围限制单次最多可查30分钟。返回的数据包括带宽峰值，每分钟的带宽值。该接口适用于需要对不同域名的带宽流量进行细粒度实时监控的场景。 | POST | /api/report/bandwidth/multi-domain/real-time |
| Querycpsbandwidth | 专线带宽接口 | POST | /myview/bandwidth-HK |
| Bandwidthvm | 查询域名带宽，输出分钟粒度的带宽和对应计费信息。 | POST | /api/bandwidth-vm |
| Queryrealtimebandwidthformultidomain | 该接口用于查询域名分钟级别的边缘带宽，用户需提供时间范围和域名来获取详细的带宽使用数据。返回内容包括每个域名的总流量、分钟级别带宽数据，以及带宽峰值等。有助于用户分析网站或应用的流量情况，从而优化资源管理和提升性能。<br> | POST | /api/report/bandwidth/multi-domain/real-time/edge |
| Reportlogflowispprovinceservice | 该接口用于查询多域名在不同ISP和省份的日志带宽及流量数据，根据请求头Accept-Language可获取中文或英文的返回结果。用户需提供查询时间范围、域名、省份、ISP获取数据。返回结果包括每个域名在各ISP和省份的带宽和流量。该接口有助于用户分析网络性能和流量分布，以优化资源配置和提高服务质量。 | POST | /api/report/flow/log/isp-province |
| Reportbandwidthwildcarddomainservice | 查询泛域名的明细域名P2P带宽数据 | POST | /api/report/bandwidth/wildcard-domain |
| Reportp2pbandwidthdomainservice | 该接口用于查真实加速域名（含泛域名和非泛域名的真实域名）的明细域名P2P带宽数据。用户需提供查询时间和相关域名信息以获取结果。返回的数据包括每个详细域名的CDN带宽、P2P带宽和P2P带宽中的IPv6带宽，均以Mbps显示。有助于用户监控和管理域名的网络环境，分析网络流量，以优化域名资源。 | POST | /api/report/p2p/bandwidth |
| Bandwidthtotal | 查询频道总流量 | POST | /myview/bandwidth-total |
| Reportlowdelaycountrybandwidthservice | 该接口用于查询在特定时间段内指定域名的各国家带宽数据。支持指指定查询国家地区。接口返回每个域名在各个国家相应时间的带宽值。此接口可用于监控分析不同国家和地区的带宽情况，数据延时较低。 | POST | /api/report/low-delay/country-bandwidth |
| Perzonebilling | 查询perzone计费数据 | POST | /myview/perzone-billing |
| Reportcountryserverbandwidthservice | 该接口用于查询服务器IP所属国家的带宽明细。用户需提供时间范围、域名、国家地区代码以及数据粒度。返回内容包含指定时间段内的每个时间点的边缘流量和带宽值。此接口有助于用户了解当前在全球不同国家的服务流量分布和使用情况。 | POST | /api/report/server/country-bandwidth |
| Reportipv6bandwidthservice | 该接口用于查询多个域名的IPV6带宽和流量数据。用户提供时间范围和域名获取相应数据。返回内容包括每个域名的详细流量（单位MB）和带宽（单位Mbps）。有助于用户分监控流量和带宽，及时优化网络资源和检测异常流量情况。 | POST | /api/report/ipv6-bandwidth |
| Reportlogbandwidthmultidomainecdnedgeservice | 该接口用于查询多个域名的分钟级别ECDN节点的日志带宽详情。用户需提供开始时间和结束时间，可指定域名、区域查询，并可选查询结果是否按域名维度分组。接口返回域名ECDN节点的边缘总流量、带宽峰值及峰值时间，以及五分钟粒度的详细带宽数据。 | POST | /api/report/bandwidth/multi-domain/log/ecdnedge |
| Bandwidthecdn | 查询客户的ECDN带宽 | POST | /myview/Bandwidthecdn |
| Bandwidthlogecdn | 查询客户的ECDN日志带宽。 | POST | /myview/Bandwidthlogecdn |
| Wsiinfo | 查询全站隔离的信息，包括：域名数均值、带宽、请求数 | POST | /myview/Wsiinfo |
| Reportp2sporiginbandwidthwildcarddomainservice | 该接口用于查询特定泛域名下的点播P2SP回源带宽数据。用户可以通过提供查询时间范围和指定的泛域名来获取具体的回源带宽信息。返回的数据包括各个泛域名及其明细域名每个时间片的回源带宽和带宽值。有助于用户监控和分析不同域名在指定时间段内带宽使用情况，从而优化带宽资源及提升服务质量。<br> | POST | /api/report/p2sp/wildcard-origin-bandwidth |
| Reportdirbandwidthinfoservice | 查询域名下多级目录的带宽及流量明细 | POST | /api/report/flow-bandwidth/dir/info |
| Reportdomainoriginresponsetimeservice | 该接口用于查询特定域名的回源响应时间，用户可以通过提供域名、开始时间和结束时间来获取相应的数据。返回的信息包括每个域名每分钟的响应时间数据，以毫秒为单位，精确到小数点后两位。此接口对于了解网站的回源性能表现至关重要，用户可根据查询结果进行性能优化和故障排查。 | POST | /api/report/origin/response-time |
| Reportbandwidthrequestbyipispprovince | 该接口用于查询多域名根据访客IP归属的指定时间范围内各省份运营商的IPv6和IPv4带宽或请求数。用户需提供时间范围和域名进行查询，可选择按域名或省份或运营商进行分组返回，支持可选返回1分钟或5分钟粒度数据。响应返回对应域名省份运营商的IPv6和IPv4带宽或请求数。 | POST | /api/report/bandwidth-request/isp-province/multi-ip-version |