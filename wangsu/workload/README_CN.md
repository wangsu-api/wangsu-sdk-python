# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-workload
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
from wangsu.workload.models import *

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
| Listdeployment | 列出用户所有Deployment | GET | /apis/apps/v1/namespaces/*/deployments |
| Getdeployment | 查询Deployment的详细信息 | GET | /apis/apps/v1/namespaces/*/deployments/* |
| Createdeployment | 创建Deployment | POST | /apis/apps/v1/namespaces/*/deployments |
| Updatedeployment | 替换Deployment | PUT | /apis/apps/v1/namespaces/*/deployments/* |
| Deletedeployment | 删除Deployment | DELETE | /apis/apps/v1/namespaces/*/deployments/* |
| Listcrdresource | 获取 crd 类型资源列表 | GET | /apis/custom/v1/namespaces/*/crdresources |
| Getcrdresource | 获取 crd 类型资源的详细信息 | GET | /apis/custom/v1/namespaces/*/crdresources/* |
| Createcrdresource | 创建 crd 类型资源 | POST | /apis/custom/v1/namespaces/*/crdresources |
| Updatecrdresource | 更新 crd 类型资源 | PUT | /apis/custom/v1/namespaces/*/crdresources/* |
| Deletecrdresource | 删除 crd 类型资源 | DELETE | /apis/custom/v1/namespaces/*/crdresources/* |
| Putpatchdeployment | 部分更新Deployment | PUT | /apis/apps/v1/namespaces/*/deployments/*/ws/patch |
| Listclustercrdresource | 获取 crd 类型资源列表 | GET | /apis/custom/v1/clustercrdresources |
| Createclustercrdresource | 创建 crd 类型资源 | POST | /apis/custom/v1/clustercrdresources |
| Getclustercrdresource | 获取 crd 类型资源的详细信息 | GET | /apis/custom/v1/clustercrdresources/* |
| Updateclustercrdresource | 更新 crd 类型资源 | PUT | /apis/custom/v1/clustercrdresources/* |
| Deleteclustercrdresource | 删除 crd 类型资源 | DELETE | /apis/custom/v1/clustercrdresources/* |
| Putpatchclustercrdresource | 部分更新crd资源 | PUT | /apis/custom/v1/clustercrdresources/*/ws/patch |
| Putpatchcrdresource | 部分更新crd资源 | PUT | /apis/custom/v1/namespaces/*/crdresources/*/ws/patch |
| Getwsproxy | 获取边缘集群资源 | GET | /apis/custom/v1/namespaces/*/wsproxy/* |
| Listpod | 查询pod列表 | GET | /openapi/custom/api/v1/pods/list |
| Getcontainerlog | 获取pod相关的容器日志 | GET | /api/v1/namespaces/*/pods/*/log |
| Liststatefulset | 获取statefulset列表 | GET | /apis/apps/v1/namespaces/*/statefulsets |
| Getstatefulset | 获取statefulset的详细信息 | GET | /apis/apps/v1/namespaces/*/statefulsets/* |
| Createstatefulset | 创建statefulset | POST | /apis/apps/v1/namespaces/*/statefulsets |
| Updatestatefulset | 更新statefulset | PUT | /apis/apps/v1/namespaces/*/statefulsets/* |
| Deletestatefulset | 删除statefulset | DELETE | /apis/apps/v1/namespaces/*/statefulsets/* |
| Listevents | 查询event列表 | GET | /openapi/custom/api/v1/events |
| Getresourcestatus | 查询资源状态 | GET | /openapi/custom/api/v1/common/resource/status |
| Deletepod | 删除pod | POST | /openapi/custom/api/v1/pods/delete |
| Listjob | 获取指定namespace中job列表 | GET | /apis/batch/v1/namespaces/*/jobs |
| Getjob | 获取指定namespace中job的详细信息 | GET | /apis/batch/v1/namespaces/*/jobs/* |
| Createjob | 创建指定namespace中指定的job | POST | /apis/batch/v1/namespaces/*/jobs |
| Updatejob | 更新指定namespace中指定的job | PUT | /apis/batch/v1/namespaces/*/jobs/* |
| Deletejob | 删除指定namespace中指定的job | DELETE | /apis/batch/v1/namespaces/*/jobs/* |
| Listpodfromedge | 从边缘查询pod列表 | GET | /openapi/custom/api/v1/pods/edge |
| Getpodfromedge | 从边缘查询pod | GET | /openapi/custom/api/v1/namespaces/*/pods/* |
| Listpodevent | 查询pod event | GET | /openapi/custom/api/v1/pods/events |
| Patchjob | 部分更新指定namespace中指定的job | PATCH | /apis/batch/v1/namespaces/*/jobs/* |
| Patchstatefulset | 部分更新指定namespace中指定的statefulset | PATCH | /apis/apps/v1/namespaces/*/statefulsets/* |
| Getcronjob | 获取指定namespace中指定的cronjob | GET | /apis/batch/v1/namespaces/*/cronjobs/* |
| Listcronjob | 获取指定namespace中的cronjob列表 | GET | /apis/batch/v1/namespaces/*/cronjobs |
| Createcronjob | 在指定namespace中创建cronjob | POST | /apis/batch/v1/namespaces/*/cronjobs |
| Updatecronjob | 在指定的命名空间更新指定的cronjob | PUT | /apis/batch/v1/namespaces/*/cronjobs/* |
| Patchcronjob | 在指定的命名空间部分更新指定的cronjob | PATCH | /apis/batch/v1/namespaces/*/cronjobs/* |
| Deletecronjob | 在指定的命名空间删除指定的cronjob | DELETE | /apis/batch/v1/namespaces/*/cronjobs/* |
| Getephemeralcontainers | 查询Pod的EphemeralContainers的详细信息 | GET | /api/v1/namespaces/*/pods/*/ephemeralcontainers |
| Updateephemeralcontainers | 更新Pod的EphemeralContainers | PUT | /api/v1/namespaces/*/pods/*/ephemeralcontainers |