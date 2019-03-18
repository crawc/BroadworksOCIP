from utils.broadworks.schema.OCISchemaAS as AuthReq
from utils.broadworks.schema.OCISchemaAS import BroadsoftDocument

class AuthenticationRequest:

    def __init__(self, userId):
        self.userId = userId
        self.broadsoft_doc = BroadsoftDocument()
        self.command = AuthReq()
        self.broadsoft_doc.protocol = "OCI"






