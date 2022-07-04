import sys
import os
import time

info='ansible-galaxy init create_'+sys.argv[1] +' --force'
print(info)
os.system(info)
info='chmod -R 777 create_'+sys.argv[1]+'/files'
print(info)
os.system(info)
info='chmod -R 777 create_'+sys.argv[1]+'/vars'
print(info)
os.system(info)
info='cp ansible.cfg create_'+sys.argv[1]+'/ansible.cfg'
print(info)
os.system(info)
info='cp .gitignore create_'+sys.argv[1]+'/.gitignore'
print(info)
os.system(info)

time.sleep(2)
path='create_'+sys.argv[1]+'/tasks/main.yml'
with open(path,'a') as contents:
    print("- include_vars:")
    info="- include_vars:\n"
    contents.write(info)
    num=sys.argv[2]
    for i in range(0, int(num)):
        info1="   dir: \"{{path}}/vars/vars_wip\""
        info="   dir: \"{{path}}/vars/vars_wip\"\n"
        contents.write(info)
        print (info1)
    print("#Execute create_"+sys.argv[1])
    info="#Execute create"+sys.argv[1]+"\n"
    contents.write(info)
    if(sys.argv[5].find('N/A')==-1):
        #has pre-requisite:
        templist=sys.argv[5].split(',')
        for i in range (len(templist)-1):
            info1="- include_tasks: \"{{repository_path}}/post_query_" +templist[i]+".yml\""
            info="- include_tasks: \"{{repository_path}}/post_query_" +templist[i]+".yml\"\n"
            print (info1)
            contents.write(info)
    info1="- include_tasks: \"{{repository_path}}/pre_query_" +sys.argv[1]+".yml\""
    info="- include_tasks: \"{{repository_path}}/pre_query_" +sys.argv[1]+".yml\"\n"
    print (info1)
    contents.write(info)  
    info1="- include_tasks: \"{{repository_path}}/create_" +sys.argv[1]+".yml\""
    info="- include_tasks: \"{{repository_path}}/create_" +sys.argv[1]+".yml\"\n"
    print (info1)
    contents.write(info)
    info1="- include_tasks: \"{{repository_path}}/post_query_" +sys.argv[1]+".yml\""
    info="- include_tasks: \"{{repository_path}}/post_query_" +sys.argv[1]+".yml\"\n"
    print (info1)
    contents.write(info)

path='create_'+sys.argv[1]+'/'+sys.argv[1]+'.yaml'
with open(path,'a') as contents:
    info= ("---\n")
    contents.write(info)
    info=("\n")
    contents.write(info)
    info=("########################################################################\n")
    contents.write(info)
    info=("#"+sys.argv[3]+"\n")
    contents.write(info)
    info=("#Owner: "+sys.argv[4]+"\n")
    contents.write(info)
    info=("#Prerequisites: "+sys.argv[5]+"\n")
    contents.write(info)
    info=("########################################################################\n")
    contents.write(info)
    info=("\n")
    contents.write(info)
    info= ("- name: File CleanUp and Processing before the Change\n")
    contents.write(info)
    info= ("  hosts: localhost\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml  \n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - pre_file_processing\n")
    contents.write(info)
    info= ("  - validate_apic_id\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("- name: tasks related to ACI  \n")
    contents.write(info)
    info= ("  hosts: all\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - create_snapshot_before_change\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("  #related to the role/project\n")
    contents.write(info)
    info= ("  - "+sys.argv[1]+"\n")
    contents.write(info)
    info= ("  - create_snapshot_after_change\n")
    contents.write(info)
    info= ("\n")
    contents.write(info)
    info= ("- name: File CleanUp after the Change\n")
    contents.write(info)
    info= ("  hosts: localhost\n")
    contents.write(info)
    info= ("  connection: local\n")
    contents.write(info)
    info= ("  gather_facts: no\n")
    contents.write(info)
    info= ("  vars_files:\n")
    contents.write(info)
    info= ("    - ../../vars/global.yaml\n")
    contents.write(info)
    info= ("  \n")
    contents.write(info)
    info= ("  roles:\n")
    contents.write(info)
    info= ("  - post_file_cleanup\n")
    contents.write(info)

path='create_'+sys.argv[1]+'/meta/main.yml'
with open(path,'r') as contents:
    filedata=contents.read()
filedata = filedata.replace('  author: your name', '  author: '+sys.argv[4])
filedata = filedata.replace('  description: your role description', '  description: '+sys.argv[3])
filedata = filedata.replace('  company: your company (optional)', '  company: Intel')
with open(path,'w') as contents:
    contents.write(filedata)
