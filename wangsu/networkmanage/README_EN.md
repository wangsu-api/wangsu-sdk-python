# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-networkmanage
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
from wangsu.networkmanage.models import *

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
| Vmpreleaseedgeip | Used to release exclusive and drifting additional public IP addresses.<br>Explanation:<br>1) Drift type additional IP needs to be unbound with the cloud host before it can be released. If it is not unbound, the release will fail;<br>2) If multiple drifting IPs are released in bulk, some IPs have been unbound and some IPs have not been unbound, the unbound ones will be released normally, while the unbound ones will fail to be released.<br>3) Exclusive IP is released without unbinding. | PUT | /vmp/edgeIp/release |
| Vmpallocateedgeip | Used to apply for drift type additional public IP. Drift mode supports the simultaneous use of multiple instances of the same IP, and is commonly used in master-slave switching scenarios, such as LVS. | POST | /vmp/edgeIp/allocate |
| Vmpassignedgeip | Bind the requested drifting additional IP to the specified instance.<br>Drift type additional IP supports the simultaneous use of multiple instances of the same IP, commonly used in master-slave switching scenarios, such as LVS. | PUT | /vmp/edgeIp/assign |
| Vmpunassignedgeip | Can be used to unbind drifting additional public network IPs and instances. Drift type additional public IP supports the simultaneous use of multiple instances of the same IP, and is commonly used in master-slave switching scenarios, such as LVS.<br>Explanation:<br>1) The drifting additional public IP to unbind must be an IP bound to the specified instance, and cannot be an IP bound to other virtual machines;<br>2) If multiple drifting additional public network IPs are unbound in bulk, and some IPs are bound to other instances, all IPs fail to be unbound, and the interface returns an error message. | PUT | /vmp/edgeIp/unassign |
| Vmpqueryedgeip | Used to query edge public IP addresses that have been applied for. | GET | /vmp/edgeIp |
| Listservice | query list of service | GET | /api/v1/namespaces/*/services |
| Getservice | query details of service | GET | /api/v1/namespaces/*/services/* |
| Createservice | create service | POST | /api/v1/namespaces/*/services |
| Updateservice | update service | PUT | /api/v1/namespaces/*/services/* |
| Deleteservice | delete service | DELETE | /api/v1/namespaces/*/services/* |
| Vmpedgeipallocate4occupancy | Used to apply for exclusive additional public IP addresses. Once the IP is applied, it will be bound to the specified instance simultaneously. One IP can only be bound to one instance. | POST | /vmp/edgeIp/allocate4Occupancy |
| Putpatchservice | partial update service | PUT | /api/v1/namespaces/*/services/*/ws/patch |
| Getnetworkpolicy | get network policy details info | GET | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Listnetworkpolicy | list network policy | GET | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies |
| Createnetworkpolicy | create network policy | POST | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies |
| Deletenetworkpolicy | delete network policy | DELETE | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Updatenetworkpolicy | update network policy | PATCH | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Putnetworkpolicy | put network policy | PUT | /apis/networking.k8s.io/v1/namespaces/*/networkpolicies/* |
| Createingresscontroller | create ingress controller | POST | /openapi/custom/api/v1/ingress-contrl |
| Updateingresscontroller | update ingress controller | PUT | /openapi/custom/api/v1/ingress-contrl/* |
| Deleteingresscontroller | delete ingress controller | DELETE | /openapi/custom/api/v1/ingress-contrl/* |
| Getingresscontroller | query ingress controller detail | GET | /openapi/custom/api/v1/ingress-contrl/* |
| Listingresscontroller | query ingress controller list | GET | /openapi/custom/api/v1/ingress-contrl |
| Createingress | create ingress | POST | /openapi/custom/api/v1/ingress |
| Updateingress | update ingress | PUT | /openapi/custom/api/v1/ingress/* |
| Deleteingress | delete ingress | DELETE | /openapi/custom/api/v1/ingress/* |
| Getingress | query ingress detail | GET | /openapi/custom/api/v1/ingress/* |
| Listingress | query ingress list | GET | /openapi/custom/api/v1/ingress |
| Edgeiprivatepallocate | Used to apply for drift type additional private IP | POST | /vmp/edgeIp/private/allocate |
| Releaseedgeprivateip | Release edge private IP | PUT | /vmp/edgeIp/private/release |
| Assignedgeprivateip | Assign edge private IP | PUT | /vmp/edgeIp/private/assign |
| Unassignedgeprivateip | Unassign edge private IP | PUT | /vmp/edgeIp/private/unassign |
| Queryedgeprivateip | Query edge private IP | GET | /vmp/edgeIp/private |
| Vmpqueryavailablecidrs | Query available cidrs in a node | GET | /vmp/cidrs |
| Vmpqueryavailablecidrsdetail | This interface fetches available subnet details, including free IP count and attributes, within a specified node by its name, for IP allocation or instance creation. | GET | /vmp/cidrs/detail |