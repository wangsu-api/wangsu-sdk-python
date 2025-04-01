# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-gtmmanage
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
from wangsu.gtmmanage.models import *

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
| Deldispatchpolicy | 删除调度策略是将域名下的策略配置全部删除。 | POST | /clouddns/Deldispatchpolicy |
| Controldispatchpolicy | 对调度策略进行控制，启用调度策略即下发策略配置并部署生效；停用调度策略时，策略配置不删除，但配置不生效。 | POST | /clouddns/Controldispatchpolicy |
| Querydispatchpolicydetail | 根据ID查询调度详情，查询条件：输入域名ID、策略ID | POST | /clouddns/Querydispatchpolicydetail |
| Savedispatchpolicy | 为域名添加新的调度策略，调度策略分成2种类型：负载均衡；主备+负载均衡。<br>新增、修改调度策略为同一个接口，但json格式部分不一样。 | POST | /clouddns/Savedispatchpolicy |
| Querydispatchpolicies | 分页查询策略信息，包括策略类型、线路信息、策略状态（解析至主源还是备源）、监控配置。 | POST | /clouddns/Querydispatchpolicies |
| Controldispatchresource | 启停调度资源 | POST | /clouddns/Controldispatchresource |
| Controlresourcecluster | 调度策略启用/停用主源 | POST | /clouddns/Controlresourcecluster |