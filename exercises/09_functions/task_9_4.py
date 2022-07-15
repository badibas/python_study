# -*- coding: utf-8 -*-
from pprint import pprint

ignore = ["duplex", "alias", "configuration"]
ign1, ign2, ign3  = ignore
config = {}
with open("config_sw1.txt", "r") as f:
     for line in f:
#         pprint(line)
         if ('!' not in line) and (ign1  not  in  line) and (ign2 not in line) and (ign3 not in line):
            line_config = line
#            pprint(line)
            if not  line_config.startswith(" "):
                keys = line_config
                config[keys] = {}
            else:
                config[keys] = line_config
            pprint(config)
#         else:
#           config[line]=line
#     pprint(config) 
#def ignore_command(command, ignore):
#    for word in ignore:
#        if word in command:
#            ignore_status = True
#    return ignore_status
