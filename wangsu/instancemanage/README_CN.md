# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-instancemanage
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
from wangsu.instancemanage.models import *

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
| Vmpremoveinstance | 销毁指定的实例，支持批量销毁。销毁后实例所使用的物理资源都将被回收，包括磁盘及快照，相关数据全部丢失且永久不可恢复。<br>执行后可再次调用查询实例接口，确认实例是否成功删除。 | POST | /vmp/servers/delete |
| Vmpqueryinstance | 查询某个客户拥有的实例。 | GET | /vmp/servers |
| Vmpinstanceoperation | 假如您发现某个实例不能正常使用（如可以ping但不能登录），可调用该接口尝试强制重启该机器。强制重启等同于传统服务器的断电重启，可能丢失实例操作系统中未写入磁盘的数据。正常关机就是普通shutdown操作。该接口调用成功后需再调用实例查询接口，确认实例的最新状态，以验证是否重启成功。 | POST | /vmp/servers/*/action |
| Vmpcreateinstance | 通过该接口您可以在某个区域申请创建指定规格的云主机实例，实例创建完毕之后，可通过使用实例查询接口获得实例的最新状态。<br>1）如果虚拟机需要使用内网网络并且未指定节点名称，则一次请求的虚拟机都将调度到同一个Cluster（只支持Cluster内的内网互通），非同一次请求的虚拟机无法保证虚拟机间内网互通，因为可能调度到不同的Cluster。不同节点、区域、省份或运营商的虚拟机间不支持内网互通，因为他们必定被调度到不同的Cluster。<br>2）如果创建请求携带了cidr的参数，则要求节点上或者没有虚拟机（可以是创建过但是都销毁了）或者已有虚拟机的cidr与当前请求一致，这样的节点才能创建虚拟机，如果找不到这样的节点，则虚拟机创建失败。如果不指定privateIPv4，cidr的第一个ip地址默认不会分配给虚拟机。例如，cidr=192.168.10.129/25，则虚拟机的ip分配范围从192.168.10.130开始，除非指定参数privateIPv4=192.168.10.129，才能创建ip为129的虚拟机。<br>3）如果请求参数中携带的是裸机模板，则表示创建裸机实例，此时不支持内网、不支持ipv6。 | POST | /vmp/servers |
| Editinstance | 用于修改实例信息，当前仅支持实例名称修改。 | PUT | /vmp/servers |
| Instanceipv6management | 为存量云主机实例分配/移除IPv6地址，裸机实例不支持。<br>分配ipv6说明：<br>1）action= ALLOCATION；<br>2）主机状态必须为运行或停机，主机所在节点必须支持IPv6；<br>3）如果主机当前已存在ipv6则接口会直接返回已有ipv6地址。<br>移除ipv6说明：<br>1）action= REMOVE；<br>2）主机状态必须为运行或停机。 | POST | /vmp/servers/ipv6 |
| Instancediskscaling | 支持实例在线添加磁盘。 | POST | /vmp/servers/attachDisk |
| Manageinstancetags | 管理云主机实例标签，支持修改或删除实例标签。 | PUT | /vmp/server-tags |
| Convertfreetypeinstancetochargetype | 对指定的免费实例进行转正，避免免费实例过期被删除，支持批量转正。转正后实例将转为计费实例。 | POST | /vmp/servers/charge |
| Instancereplaceip | 更换虚拟机ip，支持多ip同时更换 | PUT | /vmp/servers/ipReplace |
| InstanceRebuild | 通过该接口可以对已创建的实例进行重装系统 | POST | /vmp/servers/rebuild |
| Createdeployment | 创建一个容器组 | POST | /api/ecci/v1/deployments |
| Getecciinstance | 获取容器实例详情 | GET | /api/ecci/v1/instances/* |
| Updateecciinstance | 更新一个容器实例 | PUT | /api/ecci/v1/instances/* |
| Deleteecciinstance | 删除一个容器实例 | DELETE | /api/ecci/v1/instances/* |
| Getecciinstancelist | 获取容器实例列表 | GET | /api/ecci/v1/instances |
| Getclusterlist | 获取集群列表 | GET | /api/ecci/v1/clusters |
| Gettoken | 获取认证token | GET | /api/ecci/v1/token |
| Createephoneinstance | 通过该接口可以在某个区域申请创建指定规格的云手机实例。 | POST | /ephone/instances/create |
| Manageephoneinstance | 操作指定的边缘云手机实例，包括边缘云手机删除、重启和一键新机等操作。注意，重启可能丢失边缘云手机实例中未写入磁盘的数据，或者一键新机会丢失云边缘手机实例中所有的磁盘数据。 | POST | /ephone/instances/action |
| Queryinstancelist | 查询指定的边缘云手机实例接口。 | GET | /ephone/instances/list |
| Instancebandwidthaggregationquery | 虚机带宽汇总查询接口,用户查询虚拟机在一个时段内的总流量，单位为MB，其中extTrafficIn：外网流入流量汇总值，extTrafficOut：外网流出流量汇总值 | GET | /vmp/servers/bandwidth_aggregation |
| Querygps | 查询云手机实例的坐标信息。 | GET | /ephone/instances/gps |
| Runephoneadbshell | 通过该接口可以在云手机实例中执行 adb shell 命令 | POST | /ephone/instances/adbshell |
| Screenshotephoneinstance | 指定云手机实例进行截屏。 | POST | /ephone/instances/screenshot |
| Vmpinstancebandwidth5minquery | 查询实例单机5分钟粒度带宽数据 | GET | /vmp/servers/bandwidth_5_minutes |