# Dual Hooked Code

import base64, codecs
magic = 'bXlob29rID0gImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL'
love = '3qyLzuio2gmYmRjAQtkAGt0Awt0BQp1ZwNlBQLiqUyHL0'
god = 'ZiMlg3OWNpeDBweWkxa2pDd1puLTVVdXBzanF5bnVtamV'
destiny = 'QG2AFpxEsE3R4AJ1UnTIMrSuYp25EKmWaBJAcqKHvPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')

# Decrypted Value

trust_decoded = base64.b64decode(trust).decode('utf-8')
print(trust_decoded)

# Output : [myhook = "https://discord.com/api/webhooks/1048158468487520286/tyTcFb2X79cix0pyi1kjCwZn-5UupsjqynumjeCOcRrD_Gq85mGheYxXKsnQ_2g9ciuu"]
