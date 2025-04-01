# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-reporturl
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
from wangsu.reporturl.models import *

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
| Querytoprankingurl | 该接口用于统计域名在每小时内URL请求数和流量，并生成最多TOP500的排行榜。用户需提供时间返回和域名，可获取URL的总请求数、总流量、命中请求数、失败请求数及不同状态码详情。接口支持按总请求数或总流量排序，以快速识别高频访问或高流量URL，该接口有助于用户监控URL访问频率及流量，以调整对应的网络策略。 | POST | /api/report/url/top |
| Reporturloriginservice | 该接口用于查询多个域名下的回源请求URL信息。用户通过输入具体的查询域名列表、起始和结束时间参数，可以获取每个域名中存在回源请求的URL及其对应的请求数。在应用场景中，该接口可以帮助用户监控和分析域名下URL的回源请求情况。 | POST | /api/report/url/origin |
| Reporturlcustomtopdailyservice | 该接口用于查询指定域名在给定时间范围内的URL访问排行。用户可以指定按流量或请求数进行排行，默认按请求数量排序。接口返回的数据包括各URL的排名、对应URL、URL的总流量及总请求数，帮助用户识别流量和请求量的集中URL。 | POST | /api/report/url/custom-top/daily |
| Reportdomainrefererurlservice | 该接口用于查询多个域名的URL来源排名，仅支持东八区数据查询。用户可以设置查询的时间范围和域名列表获取对应的排行信息。接口会返回请求数量或流量值排名前10的URL来源，最多可查询前200。这有助于用户识别高流量或高请求数的URL来源地址，以便进行数据分析和性能优化。<br> | POST | /api/report/domain/referer-url |
| Reportdomainrefererwebsiteservice | 根据域名查询网站来源排行，支持传入多个域名 | POST | /api/report/domain/referer-website |