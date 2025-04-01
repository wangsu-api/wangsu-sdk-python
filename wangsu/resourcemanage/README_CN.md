# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-resourcemanage
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
from wangsu.resourcemanage.models import *

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
| Vmpqueryflavor | 您可以通过此接口查询得到某个区域能提供的实例的规格列表，然后通过这个规格来创建实例。 | GET | /vmp/flavors |
| Vmpquerynode | 查询边缘计算平台有哪些节点可以提供服务。 | GET | /vmp/nodes |
| Vmpquerybandwidth | 查询您所有在用的节点的实时冗余带宽，有冗余带宽的节点就返回True，无冗余带宽的节点就返回False，如果该节点的带宽数据采集结果不足以支撑该接口的时效性要求，即带宽统计数据较旧暂不满足时效性要求，则返回Undefined。节点是否有冗余带宽的判断方法：节点上限带宽大于节点的实时使用带宽。数据粒度：5分钟。<br>备注：<br>1）只返回客户有使用的节点的带宽冗余情况，有使用的前提是该客户在这个节点至少有1台云主机；<br>2）如果某个节点返回的result是Undefined，表示该节点无10分钟内的实时带宽统计数据，为了保证冗余带宽的时效性，返回Undefined，建议稍后再次调用该接口以查询该节点的最新情况；<br>3）如果节点是双线或多线节点，则分别返回每个运营商的带宽冗余情况；<br>4）节点的实时冗余带宽是动态变化的，若通过该接口的返回结果做业务调度，建议周期获取数据。 | POST | /vmp/redundant-bandwidth |
| Noderedundantbandwidth4pstatp | 用于查询客户所使用节点的实时冗余带宽 | GET | /vmp/nodeRedundantBandwidth4Pstatp |