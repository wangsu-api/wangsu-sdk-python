import json
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.domainmanagement.models import *


class Client:
    @staticmethod
    def main():
        cancelApiDomainServiceRequest = CancelApiDomainServiceRequest()
        
        aksk_config = AkSkConfig()
        aksk_config.access_key = "{accessKey}"
        aksk_config.secret_key = "{secretKey}"
        aksk_config.uri = "/api/domain/*/cancel"
        aksk_config.method = "PUT"

        # See AkSkAuth class for more methods, you can edit
        response = AkSkAuth.invoke(aksk_config, json.dumps(cancelApiDomainServiceRequest.to_map()))
        print(response)


if __name__ == "__main__":
    Client.main()
