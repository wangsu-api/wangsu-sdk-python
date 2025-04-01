# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-strategymanagement
```


## Requirements

- Python 3.6 or later
- Dependencies:
  - requests >= 2.10.0
  - alibabacloud_tea >= 0.3.3
  - alibabacloud_tea_openapi >= 0.3.6
  - alibabacloud_tea_console >= 0.0.1
  - alibabacloud_tea_util >= 0.3.8

## Quick Start

### Example

The SDK uses AKSK authentication. You need to configure your access key and secret key:

```python
import json
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.strategymanagement.models import *

# Refer to the API list at the end of this document and modify the corresponding {ActionName}, Method, Uri
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



## API List
For detailed API documentation and available methods, please refer to the [official Wangsu API documentation](https://www.wangsu.com/document/api-doc/Overview?productType=all).

| ActionName | enDescription | client_methods | uri |
| --- | --- | --- | --- |
| Listpropagationpolicies | query list of propagation | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies |
| Createpropagationpolicies | create propagation | POST | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies |
| Deletepropagationpolicies | delete propagation | DELETE | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Getpropagationpolicies | query details of propagationpolicy | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Updatepropagationpolicies | update propagation | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/* |
| Putpatchpropagationpolicies | partial update propagationpolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/propagationpolicies/*/ws/patch |
| Updatehorizontalpodautoscaler | update hpa | PUT | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Patchhorizontalpodautoscaler | patch hpa | PATCH | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Deletehorizontalpodautoscaler | delete hpa | DELETE | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Listhorizontalpodautoscaler | list  hpa | GET | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers |
| Gethorizontalpodautoscaler | get hpa | GET | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers/* |
| Createhorizontalpodautoscaler | create  hpa | POST | /apis/autoscaling/v2beta2/namespaces/*/horizontalpodautoscalers |
| Listoverridepolicy | list Overridepolicies | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies |
| Createoverridepolicy | Create Overridepolicyes | POST | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies |
| Getoverridepolicy | Get OverridePolicy | GET | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Putoverridepolicy | Update Overridepolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Deleteoverridepolicy | Delete Overridepolicy | DELETE | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/* |
| Wspatchoverridepolicy | Patch Overridepolicy | PUT | /apis/policy.karmada.io/v1alpha1/namespaces/*/overridepolicies/*/ws/patch |