# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-dataquery
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
from wangsu.dataquery.models import *

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
| Sitetotalflowchart | 查询站点分配带宽和实际的带宽趋势 | GET | /api/siteFlow/siteTotalFlowChart |
| Sitesessioninfo | 查询企业站点的会话日志 | GET | /api/siteSession/info |
| Sitequalitychart | 查询企业站点的链路质量趋势数据 | GET | /api/siteTunnel/qualityChart |
| Sitemsdevice | 查询指定企业的双机站点当前使用的CPE | GET | /api/siteDevice/ms |
| Sitelogicchart | 站点连接质量 | GET | /api/siteLogic/qualityChart |
| Allsitesumflow | 查询指定企业下所有站点的累计流量 | GET | /api/siteFlow/orgSumFlow |
| Saassession | 查询站点的上网会话数据. | GET | /api/saasSession/info |