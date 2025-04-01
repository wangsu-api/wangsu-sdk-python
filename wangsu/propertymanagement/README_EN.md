# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-propertymanagement
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
from wangsu.propertymanagement.models import *

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
| GetAPropertyVersion | Get the detailed configuration of a property version. | GET | /cdn/properties/*/versions/* |
| UpdateAPropertyVersion | This API lets you update a property version. Please note that a property that has already been deployed to production or staging is 'frozen' and cannot be updated or validated again. The only exception is that the version description can be updated. | PATCH | /cdn/properties/*/versions/* |
| DeleteAPropertyVersion | DeleteAPropertyVersion. | DELETE | /cdn/properties/*/versions/* |
| GetAProperty | Returns a summary about a property including the number of versions that have been created and which versions are deployed. | GET | /cdn/properties/* |
| UpdateAProperty | This endpoint changes the name and description of a property. Its versions are unaffected. <br><br>If you wish to change a property's configuration, use the <a href="#operation/updatePropertyVersion">UpdateAProperty version API</a>. | PATCH | /cdn/properties/* |
| DeleteAProperty | Delete a property by its ID. | DELETE | /cdn/properties/* |
| GetListOfPropertyVersions | Get a list of all property versions. A summary of each version including its status and associated hostnames is returned. | GET | /cdn/properties/*/versions |
| CreateAPropertyVersion | Create a new version of a property. | POST | /cdn/properties/*/versions |
| CreateAProperty | Creates a property to define the configuration of one or more hostnames (domains) to deploy to the CDN servers. | POST | /cdn/properties |
| GetListOfProperties | The API returns a summary of properties including the ID, latest version number, comments, staging version number, production version number, and last update time of each one. Use query parameters to filter the list of returned properties. | GET | /cdn/properties |