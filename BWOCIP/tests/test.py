import StringIO


y = StringIO.StringIO()
r = OCISchemaAS.OCIMessage()
r.protocol = "OCI"
r.export(y,0)
print y.getvalue()


