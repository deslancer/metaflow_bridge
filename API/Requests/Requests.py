import json
import os
from pathlib import Path
import requests

headers = {'Accept': 'application/json'}

API_URL = 'https://metaflow3d.visionexp.io/api/v2'


def sign_in(mail, passwd):
    creds = {
        "email": mail,
        "password": passwd
    }
    r = requests.post(API_URL + '/user/login', json=creds, headers=headers)

    # set output path and file name (set your own)
    current_dir = Path(__file__).resolve().parent
    file_name = os.path.join(current_dir.parents[1], "creds", "user_creds.json")
    json_data = json.dumps(r.json(), ensure_ascii=False, indent=4)

    # write JSON file
    with open(file_name, 'w') as outfile:
        outfile.write(json_data + '\n')

    return r.json()


def upload_model(user_id, file):


    files = {
        'assets': (file.name, file, "application/octet-stream")
    }
    data = {
        'bucketId': 'models',
        'subFolder': f"/{user_id}/",
        'contentType': "application/octet-stream",
    }
    response = requests.post(API_URL + '/assets/upload', files=files, data=data,)

    if response.status_code == 200:
        data = response.json()
        print('Upload successful:', data)
    else:
        print('Error uploading file:', response.status_code, response.text)

