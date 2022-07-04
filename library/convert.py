#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import sys
import pandas as pd


def convert():
  # define available arguments/parameters a user can pass to the module
  fields = {
  "filepath": {"required": True, "type": "str"},
  "filename": {"required": True, "type": "str"}
  }
  module = AnsibleModule(argument_spec=fields)
  excel_file = os.path.expanduser(module.params['filename'])
  file_path= module.params['filepath']
  all_sheets = pd.read_excel(excel_file, sheet_name=None)
  
  sheets = all_sheets.keys()

  for sheet_name in sheets:    
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    # #control part
    # sheet1=sheet.replace('"$','',regex=True)
    # sheet1.replace('^"*','',regex=True).to_csv("./var/vars_wip/%s.csv" % sheet_name, index=False)
    sheet.to_csv("%s/files/files_wip/%s.csv" % (file_path, sheet_name), index=False)

  module.exit_json(msg=sheets)  


def main():
    convert()


if __name__ == '__main__':
    main()