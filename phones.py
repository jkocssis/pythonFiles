import phonenumbers
from phonenumbers import geocoder, carrier

fone = phonenumbers.parse("+5519989168370")
operadora = carrier.name_for_number(fone, 'pt-br')
regiao = geocoder.descrtiption_for_number(fone, 'pt-br')
print(operadora)
print(regiao)