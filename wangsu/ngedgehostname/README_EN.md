# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-ngedgehostname
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
from wangsu.ngedgehostname.models import *

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
| GetAnEdgeHostname | This API returns information about an edge hostname including the associated client zone rules and operation history. <br> | GET | /cdn/edgeHostnames/* |
| DeleteAnEdgeHostname | Use this API to delete an edge hostname. If you have configured your DNS server with this edge hostname, you should update your DNS records before deleting it. Otherwise, visitors to the associated hostnames will see an error. | DELETE | /cdn/edgeHostnames/* |
| UpdateAnEdgeHostnameAll | Use this API to update an edge hostname. Be sure to enter all fields describing your edge hostname including ones that are not changing. After a request is submitted, it takes a few minutes to deploy the edge hostname. You can call 'Get an edge hostname' and look at the history array in the response to check the deployment status. | PUT | /cdn/edgeHostnames/* |
| UpdateAnEdgeHostnamePart | This API allows you to update an edge hostname by sending only the fields that need to be changed. After a request is submitted, it takes a few minutes to deploy the edge hostname. You can call 'Get an edge hostname' and look at the history array in the response to check the deployment status. | PATCH | /cdn/edgeHostnames/* |
| CreateAnEdgeHostname | This API enables you to create edge hostnames to control how requests from different client zones are handled. You must create CNAME DNS records to point your properties' hostnames to an edge hostname created using this API in order for the CDN to handle your content. <br><br>After a request is submitted, it takes a few minutes to deploy the edge hostname. Please make sure the deployment is finished and the configurations take effect before pointing your hostnames to the edge hostname. You can call 'Get an edge hostname' and look at the history array in the response to check the deployment status. | POST | /cdn/edgeHostnames |
| GetAListOfEdgeHostnames | GetAListOfEdgeHostnames. Specify search, offset, and limit parameters to filter your results. The default is to return the most recently updated edge hostname first. | GET | /cdn/edgeHostnames |
| GetAListOfIsps | Obtain a list of ISPs that can be used in edge hostname client zone rules. | GET | /cdn/edgeHostnames/isps |
| Getclientregions | Get a list of client regions that can be used in edge hostname client zone rules. Query parameters allow you to filter and sort the results. | GET | /cdn/edgeHostnames/clientRegions |