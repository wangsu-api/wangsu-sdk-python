# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-nghostnames
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
from wangsu.nghostnames.models import *

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
| GetListOfHostnamesThatHaveBeenDeployed | Get a list of hostnames belonging to properties that have been deployed to production or staging. | GET | /cdn/hostnames |
| GetHistoricalInformationAboutHostnames | Get a list of hostnames belonging to properties that were successfully <a href="#tag/Deployment-Management">deployed</a> to production or staging during a particular timeframe. | GET | /cdn/hostnames/historical |
| GetHistoricalInformationAboutOneHostname | This API returns information about a hostname's deployments to production and staging. Query parameters let you specify a timeframe to search. | GET | /cdn/hostnames/historical/* |
| GetInformationAboutASpecificHostname | This API returns information about a specific hostname belonging to a property that has been deployed to production or staging. | GET | /cdn/hostnames/* |
| Querynghostnameandedgehostnameforwplus | This api is used to query the relationship between the cdnpro acceleration name and the real service domain. Used to query all information without passing parameters, or to query specified information by providing hostName or edgeHostName, including hostName e and edgeHostName. | POST | /api/ngcdn/hostname/edgehostname |