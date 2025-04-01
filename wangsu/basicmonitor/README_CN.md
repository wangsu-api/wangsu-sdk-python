# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-basicmonitor
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
from wangsu.basicmonitor.models import *

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
| Reportflowdomainispprovinceiaasservice | 该接口用于查询边缘服务器在各ISP和省份的流量数据，支持根据请求头Accept-Language返回中文或英文数据。用户需提供查询的时间范围、域名、ISP和省份等信息，返回内容包含每个ISP和省份的流量明细，以MB为单位，并按5分钟的时间粒度显示。适用于需要分析不同地区和运营商流量分布的用户，帮助优化网络资源和提升服务效率。 | POST | /api/report/flow/domain-isp-province/iaas |
| Vmpqueryservermetric | 查询云主机实例的CPU使用率、内存使用情况和带宽使用情况，以便接入自身的监控系统，掌控云主机的运行情况。提供近90天的监控数据查询，单次查询范围不超过3天，数据粒度为5分钟。如果是裸机实例，当前仅支持查询带宽，不支持查询CPU和内存。 | GET | /vmp/servers/metric |