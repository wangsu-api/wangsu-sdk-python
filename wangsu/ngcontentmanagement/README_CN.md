# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-ngcontentmanagement
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
from wangsu.ngcontentmanagement.models import *

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
| CreateAPurgeRequest | 创建一个刷新任务来强制刷新存储在CDN Pro缓存服务器中的内容。当您更新了源站的内容，并希望访客立即看到更新后的内容，您可以创建一个刷新任务立即刷新内容。 | POST | /cdn/purges |
| GetListOfPurgeRequests | 获取刷新请求列表。接口仅支持查询近15天内的刷新请求。 | GET | /cdn/purges |
| GetPurgeSummary | 查询某个时间范围内的刷新请求的汇总信息。可通过查询参数指定时间范围和目标环境。 | GET | /cdn/purges/purgeSummary |
| GetPurgeRequestStatus | 获取刷新请求的详细信息，包括涉及的加速域名和刷新任务的执行状态等。 | GET | /cdn/purges/* |
| CreateAPrefetchRequest | 创建一个预取请求，从您的源站预取内容来预热CDN Pro的缓存。通过内容提前预取，可避免大量请求涌入源站服务器。发起预取之前，必须先将域名对应的加速项目部署到生产环境。 | POST | /cdn/prefetches |
| GetListOfPrefetchRequests | 获取预取请求列表。接口仅支持查询近15天内的预取请求。 | GET | /cdn/prefetches |
| GetPrefetchRequestStatus | 获取预取请求的详细信息。 | GET | /cdn/prefetches/* |
| GetAvailablePurgeRequests | 该接口返回您可以在演练或生产环境进行目录和文件刷新的额度。使用限额每日有一个固定值。您可以临时超过该限额，但这会减少第二天可用的刷新额度。 | GET | /cdn/purges/purgeTokens |