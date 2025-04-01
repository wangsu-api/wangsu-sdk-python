# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-strategymanagement
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
from wangsu.strategymanagement.models import *

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
| Listpropagationpolicies | 获取propagation列表 | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies |
| Createpropagationpolicies | 创建Propagation | POST | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies |
| Deletepropagationpolicies | 删除propagation | DELETE | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Getpropagationpolicies | 获取propagation的详细信息 | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Updatepropagationpolicies | 更新propagation | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Putpatchpropagationpolicies | 部分更新PropagationPolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/*/ws/patch |
| Updatehorizontalpodautoscaler | 修改HPA | PUT | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Patchhorizontalpodautoscaler | 部分修改HPA | PATCH | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Deletehorizontalpodautoscaler | 删除HPA | DELETE | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Listhorizontalpodautoscaler | 查询HPA列表 | GET | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers |
| Gethorizontalpodautoscaler | 查询HPA | GET | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Createhorizontalpodautoscaler | 新增HPA | POST | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers |
| Listoverridepolicy | Overridepolicies列表 | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies |
| Createoverridepolicy | 创建Overridepolicies | POST | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies |
| Getoverridepolicy | 获取OverridePolicy的详细信息 | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Putoverridepolicy | 更新OverridePolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Deleteoverridepolicy | 删除OverridePolicy | DELETE | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Wspatchoverridepolicy | 部分更新OverridePolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/*/ws/patch |