from phaxio import PhaxioApi
import os
import time
import csv

live_key = 'insert live key'
live_secret = 'insert live secret'

test_key = 'insert test key'
test_secret = 'insert test secret'

def send_fax(key, secret, fax_number, filename):
    #The Phaxio rate limit is 1 request per second
    #See https://www.phaxio.com/faq
    time.sleep(1.5)
    api = PhaxioApi(key, secret)
    response = api.Fax.send(to = fax_number,
            files = filename)

def get_file_dirs(folder):
    '''
    Returns a list of the path of each file
    to send via fax
    '''
    return [os.path.join(folder, the_file) for the_file in os.listdir(folder)
            if the_file.split('.')[1] == 'docx']


def get_fax_number_from_file_dir(file_dir):
    '''
    Returns the fax number for a given respondent ID
    Assumes that the fax number is the filename
    '''
    filename = os.path.basename(file_dir)
    return filename.split('.')[0]

if __name__ == '__main__':
    file_dirs = get_file_dirs('merged-letters')

    for file_dir in file_dirs:
        send_fax(test_key, test_secret,
                get_fax_number_from_file_dir(file_dir),
                file_dir)
