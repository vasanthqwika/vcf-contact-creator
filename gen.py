import pandas as pd

# excelFile = pd.read_excel('qwika builders.xlsx')
datas = '''Rafeek Raja,919791631757
Rafeek Raja,919791631753
Rafeek Raja,919791631754'''


outputFileName = "selamNewCustomer.vcf"
lastName = 'SLM CUST'

vcard = ''

for data in datas.split('\n'):
	x = data.split(',')
	vcard = vcard + f"""
BEGIN:VCARD
VERSION:2.1
FN:{x[0]} ({lastName})
TEL;CELL: +91{x[1]}
END:VCARD"""

print(vcard)

with open(outputFileName, 'w+') as vcardFile:
	vcardFile.write(vcard)

# uncommand in excel file
# vcard = ""
# for data in excelFile.iterrows():
# 	vcard = vcard + f"""
# BEGIN:VCARD
# VERSION:2.1
# FN:{data[1][0]} (lastName)
# TEL;CELL: +{data[1].phone}
# END:VCARD"""

# with open(outputFileName, 'r+') as vcardFile:
# 	vcardFile.write(vcard)