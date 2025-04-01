# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-alertrules
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
from wangsu.alertrules.models import *

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
| Createcloudmonitorrealtimealarmrule | 创建云监控的实时监控告警规则。用户可传入监控规则名称、监控资源对象、告警触发条件阈值、告警联系人等信息生成实时监控规则。适用于对控制台云产品业务需要及时关注监控数据变化的场景。接口创建监控规则当前仅支持按域名监控的部分CDN监控项。<br> | POST | /api/cloudmonitor/alarm/real-time/add |
| Editcloudmonitorrealtimealarmrule | 编辑云监控的实时监控告警规则。本接口修改规则按覆盖式修改。用户可传入监控规则id、可传入要修改的监控规则名称、监控资源对象、告警触发条件阈值、告警联系人等信息将覆盖修改监控规则。<br><br>接口管理监控规则当前仅支持按域名监控的部份监控项。 | POST | /api/cloudmonitor/alarm/real-time/edit |
| Querycloudmonitorrealtimealarmrule | 	<br>查询云监控的实时监控告警规则。用户可传入监控规则id、查询监控规则名称、监控资源对象、告警触发条件阈值、告警联系人等监控规则明细信息。<br><br>接口管理监控规则当前仅支持按域名监控的部份监控项。 | POST | /api/cloudmonitor/alarm/real-time/query |
| Deletecloudmonitorrealtimealarmrule | 删除云监控的实时监控告警规则。用户可传入监控规则id删除指定监控规则。<br><br> | POST | /api/cloudmonitor/alarm/real-time/delete |