import os
import pandas as pd

folder_path = r'C:\Users\Savvycom\Desktop\Amcham\Data P4'
excel_file = 'Page 4.xlsx'
worksheet_name = 'CombinedData'

vcf_data = []

for filename in os.listdir(folder_path):
    if filename.endswith('.vcf'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as vcf_file:
            vcf_content = vcf_file.readlines()
            data = {'Name': '', 'Email': '', 'Company': '', 'Job Title': ''}
            name_fields = ['FN:', 'N:', 'NICKNAME:', 'X-PHONETIC-FIRST-NAME:', 'X-PHONETIC-LAST-NAME:']
            for line in vcf_content:
                for field in name_fields:
                    if line.startswith(field):
                        data['Name'] = line.split(':', 1)[1].strip()
                        break
                if line.startswith('EMAIL;'):
                    data['Email'] = line.split(':')[1].strip()
                elif line.startswith('ORG:'):
                    data['Company'] = line[4:].strip()
                elif line.startswith('TITLE:'):
                    data['Job Title'] = line[6:].strip()
            vcf_data.append(data)

combined_data = pd.DataFrame(vcf_data)

with pd.ExcelWriter(excel_file) as writer:
    combined_data.to_excel(writer, sheet_name=worksheet_name, index=False)
