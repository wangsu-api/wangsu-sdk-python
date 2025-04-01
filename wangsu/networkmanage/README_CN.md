# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-networkmanage
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
from wangsu.networkmanage.models import *

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
| Vmpreleaseedgeip | 用于释放独占式和漂移式额外公网IP。<br>说明：<br>1）漂移式额外IP需要先解除和云主机的绑定才能释放，如果未解除绑定会释放失败；<br>2）如果批量释放多个漂移式IP，部分IP已解除绑定，部分IP未解除，则已解除绑定的会正常释放，未解除绑定的会释放失败。<br>3）独占式IP无需解除绑定直接释放。<br> | PUT | /vmp/edgeIp/release |
| Vmpallocateedgeip | 用于申请漂移式额外公网IP。漂移模式支持同一IP为多实例同时使用，常用于主备切换场景，如LVS等。 | POST | /vmp/edgeIp/allocate |
| Vmpassignedgeip | 将申请到的漂移式额外IP绑定到指定实例。<br>漂移式额外IP支持同一IP为多实例同时使用，常用于主备切换场景，如LVS。<br> | PUT | /vmp/edgeIp/assign |
| Vmpunassignedgeip | 可用于解除漂移式额外公网IP和实例的绑定。漂移式额外公网IP支持同一IP为多实例同时使用，常用于主备切换场景，如LVS。<br>说明：<br>1）要解绑的漂移式额外公网IP必须是绑定在指定实例上的IP，不能是绑定在其他虚拟机的IP；<br>2）如果批量解绑多个漂移式额外公网IP，存在部分IP是绑定在其他实例上的，则全部IP都解绑失败，接口返回错误提示信息。 | PUT | /vmp/edgeIp/unassign |
| Vmpqueryedgeip | 用于查询已申请的额外公网IP。 | GET | /vmp/edgeIp |
| Listservice | 获取service列表 | GET | /api/v1/namespaces/*/services |
| Getservice | 获取service的详细信息 | GET | /api/v1/namespaces/*/services/* |
| Createservice | 创建Service | POST | /api/v1/namespaces/*/services |
| Updateservice | 更新service | PUT | /api/v1/namespaces/*/services/* |
| Deleteservice | 删除service | DELETE | /api/v1/namespaces/*/services/* |
| Vmpedgeipallocate4occupancy | 用于申请独占式额外公网IP，IP申请完会同时绑定到指定实例上，一个IP只能绑定一台实例。<br> | POST | /vmp/edgeIp/allocate4Occupancy |
| Putpatchservice | 部分更新service | PUT | /api/v1/namespaces/*/services/*/ws/patch |
| Getnetworkpolicy | 查询网络策略信息 | GET | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Listnetworkpolicy | 查询网络策略列表 | GET | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies |
| Createnetworkpolicy | 创建网络策略 | POST | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies |
| Deletenetworkpolicy | 删除网络策略 | DELETE | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Updatenetworkpolicy | 部分更新网络策略 | PATCH | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Putnetworkpolicy | 全量更新网络策略 | PUT | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Createingresscontroller | 创建路由控制器 | POST | /openapi/custom/api/v1/ingress-contrl |
| Updateingresscontroller | 更新路由控制器 | PUT | /openapi/custom/api/v1/ingress-contrl/* |
| Deleteingresscontroller | 删除路由控制器 | DELETE | /openapi/custom/api/v1/ingress-contrl/* |
| Getingresscontroller | 查询路由控制器详情 | GET | /openapi/custom/api/v1/ingress-contrl/* |
| Listingresscontroller | 查询路由控制器列表 | GET | /openapi/custom/api/v1/ingress-contrl |
| Createingress | 创建路由 | POST | /openapi/custom/api/v1/ingress |
| Updateingress | 更新路由 | PUT | /openapi/custom/api/v1/ingress/* |
| Deleteingress | 删除路由 | DELETE | /openapi/custom/api/v1/ingress/* |
| Getingress | 查询路由详情 | GET | /openapi/custom/api/v1/ingress/* |
| Listingress | 查询路由列表 | GET | /openapi/custom/api/v1/ingress |
| Edgeiprivatepallocate | 用于申请额外内网IP<br> | POST | /vmp/edgeIp/private/allocate |
| Releaseedgeprivateip | 用于释放额外内网IP。 说明： 1）额外IP需要先解除和云主机的绑定才能释放，如果未解除绑定会释放失败； 2）如果批量释放多个漂移式IP，部分IP已解除绑定，部分IP未解除，则已解除绑定的会正常释放，未解除绑定的会释放失败。  | PUT | /vmp/edgeIp/private/release |
| Assignedgeprivateip | 将申请到的额外内网IP和额外公网IP做映射，并一起绑定到指定实例。  | PUT | /vmp/edgeIp/private/assign |
| Unassignedgeprivateip | 可用于解除额外内网IP和额外公网IP以及实例的绑定。 | PUT | /vmp/edgeIp/private/unassign |
| Queryedgeprivateip | 用于查询已申请的额外内网IP。<br> | GET | /vmp/edgeIp/private |
| Vmpqueryavailablecidrs | 用于查询节点中可用的网段信息 | GET | /vmp/cidrs |
| Vmpqueryavailablecidrsdetail | 该接口用于查询指定节点中可用的网段详情信息，可以通过提供节点名称来获取节点下可用的网段、网段的空闲可用IP数、IP原生属性等，用于后续指定网段申请IP或创建实例。 | GET | /vmp/cidrs/detail |