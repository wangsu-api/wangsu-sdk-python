# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-workload
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
from wangsu.workload.models import *

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
| Listdeployment | list all Deployments of user | GET | /apis/apps/v1/namespaces/*/deployments |
| Getdeployment | query details of Deployment | GET | /apis/apps/v1/namespaces/*/deployments/* |
| Createdeployment | create Deployment | POST | /apis/apps/v1/namespaces/*/deployments |
| Updatedeployment | replace Deployment | PUT | /apis/apps/v1/namespaces/*/deployments/* |
| Deletedeployment | delete Deployment | DELETE | /apis/apps/v1/namespaces/*/deployments/* |
| Listcrdresource | query list of crd resources | GET | /apis/custom/v1/namespaces/*/crdresources |
| Getcrdresource | query details of crd resource | GET | /apis/custom/v1/namespaces/*/crdresources/* |
| Createcrdresource | create crd resource | POST | /apis/custom/v1/namespaces/*/crdresources |
| Updatecrdresource | update crd resource | PUT | /apis/custom/v1/namespaces/*/crdresources/* |
| Deletecrdresource | delete crd resource | DELETE | /apis/custom/v1/namespaces/*/crdresources/* |
| Putpatchdeployment | partial update Deployment | PUT | /apis/apps/v1/namespaces/*/deployments/*/ws/patch |
| Listclustercrdresource | query crd resource list of cluster | GET | /apis/custom/v1/clustercrdresources |
| Createclustercrdresource | create crd resource of cluster | POST | /apis/custom/v1/clustercrdresources |
| Getclustercrdresource | query crd resource details of cluster | GET | /apis/custom/v1/clustercrdresources/* |
| Updateclustercrdresource | update crd resource of cluster | PUT | /apis/custom/v1/clustercrdresources/* |
| Deleteclustercrdresource | delete crd resource of cluster | DELETE | /apis/custom/v1/clustercrdresources/* |
| Putpatchclustercrdresource | partial update crd resource of cluster | PUT | /apis/custom/v1/clustercrdresources/*/ws/patch |
| Putpatchcrdresource | partial update crd resource | PUT | /apis/custom/v1/namespaces/*/crdresources/*/ws/patch |
| Getwsproxy | query edge cluster resources | GET | /apis/custom/v1/namespaces/*/wsproxy/* |
| Listpod | listPod | GET | /openapi/custom/api/v1/pods/list |
| Getcontainerlog | Query the list of poolclusters for which the user has permissions | GET | /api/v1/namespaces/*/pods/*/log |
| Liststatefulset | list statefulset | GET | /apis/apps/v1/namespaces/*/statefulsets |
| Getstatefulset | get statefulset detail | GET | /apis/apps/v1/namespaces/*/statefulsets/* |
| Createstatefulset | create statefulset | POST | /apis/apps/v1/namespaces/*/statefulsets |
| Updatestatefulset | update statefulset | PUT | /apis/apps/v1/namespaces/*/statefulsets/* |
| Deletestatefulset | delete statefulset | DELETE | /apis/apps/v1/namespaces/*/statefulsets/* |
| Listevents | query list of events | GET | /openapi/custom/api/v1/events |
| Getresourcestatus | get resource status | GET | /openapi/custom/api/v1/common/resource/status |
| Deletepod | delete  pod | POST | /openapi/custom/api/v1/pods/delete |
| Listjob | list job on namespace | GET | /apis/batch/v1/namespaces/*/jobs |
| Getjob | get job detail on namespace | GET | /apis/batch/v1/namespaces/*/jobs/* |
| Createjob | create job on namespace | POST | /apis/batch/v1/namespaces/*/jobs |
| Updatejob | update job on namespace | PUT | /apis/batch/v1/namespaces/*/jobs/* |
| Deletejob | delete job on namespace | DELETE | /apis/batch/v1/namespaces/*/jobs/* |
| Listpodfromedge | listPodFromEdge | GET | /openapi/custom/api/v1/pods/edge |
| Getpodfromedge | Get pod list information from the edge | GET | /openapi/custom/api/v1/namespaces/*/pods/* |
| Listpodevent | listPodEvent | GET | /openapi/custom/api/v1/pods/events |
| Patchjob | patch job on namespace | PATCH | /apis/batch/v1/namespaces/*/jobs/* |
| Patchstatefulset | patch statefulset on namespace | PATCH | /apis/apps/v1/namespaces/*/statefulsets/* |
| Getcronjob | get cronjob detail on namespace | GET | /apis/batch/v1/namespaces/*/cronjobs/* |
| Listcronjob | list cronjob on namespace | GET | /apis/batch/v1/namespaces/*/cronjobs |
| Createcronjob | create cronjob on namespace | POST | /apis/batch/v1/namespaces/*/cronjobs |
| Updatecronjob | update cronjob on namespace | PUT | /apis/batch/v1/namespaces/*/cronjobs/* |
| Patchcronjob | patch cronjob on namespace | PATCH | /apis/batch/v1/namespaces/*/cronjobs/* |
| Deletecronjob | delete cronjob on namespace | DELETE | /apis/batch/v1/namespaces/*/cronjobs/* |
| Getephemeralcontainers | query details of Pod's EphemeralContainers | GET | /api/v1/namespaces/*/pods/*/ephemeralcontainers |
| Updateephemeralcontainers | update EphemeralContainers of Pod | PUT | /api/v1/namespaces/*/pods/*/ephemeralcontainers |