import os

import bpy
import requests
import json

headers = {'Accept': 'application/json'}


def sign_in(mail, passwd):
    creds = {
        "email": mail,
        "password": passwd
    }
    r = requests.post('https://metaflow3d.visionexp.io/api/v2/user/login', json=creds, headers=headers)

    # encode dict as JSON

    # # set output path and file name (set your own)
    # save_path = 'E:\\'
    # file_name = os.path.join(save_path, "export_data.json")
    #
    # # write JSON file
    # with open(file_name, 'w') as outfile:
    #     outfile.write(json_data + '\n')

    return r.json()
