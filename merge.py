from mailmerge import MailMerge
import pandas as pd
import os

def clear_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print e

def merge_documents(sample_file, template_file, folder):
    '''
    Conduct a mail merge using sample information from
    sample_file, load it into the template_file
    and add the merged file to folder with the fax
    number as the filename.
    '''
    df = pd.read_csv(sample_file)

    for index, row in df.iterrows():
        with MailMerge(template_file) as document:
            document.merge(Name = str(row['Name']),
                    Address = str(row['Address']),
                    ID = str(row['ID']))

            document.write(os.path.join(folder,
                str(row['Fax Number']) + '.docx'))

if __name__ == '__main__':
    folder = 'merged-letters'
    clear_folder(folder)
    merge_documents('sample.csv', 'fax_template.docx', folder)
