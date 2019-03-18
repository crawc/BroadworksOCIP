from suds.client import Client
from OCISchemaAS import BroadsoftDocument, AuthenticationRequest

#lol = """&lt;BroadsoftDocument protocol="OCI" xmlns="C"
# xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;&lt;sessionId xmlns=""&gt;4635609806884&lt;/sessionId&gt;&lt;command xmlns="" xsi:type="AuthenticationRequest"&gt;&lt;userId&gt;aaronparfitt@thevoicefactory.co.uk&lt;/userId&gt;&lt;/command&gt;&lt;/BroadsoftDocument&gt;"""

client = Client('http://api.thevoicefactory.co.uk/webservice/services'
                '/ProvisioningService?wsdl')


x = BroadsoftDocument()
x.protocol = "OCI"


y = AuthenticationRequest()
y.set_userId()

#x.add_command()

print(x.build())





print(x.__dict__)
#print (dir(y))
#print (dir(x))


print(client.service.processOCIMessage())
