#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os



cfg_file = "../cfg/config.yaml"
save_file = "../cfg/save.yaml"
# os.path.join(rospkg.RosPack().get_path('mission_manager'), 'cfg', 'config.yaml')
with open(cfg_file) as file:
    abc = yaml.load(file, Loader= yaml.SafeLoader)
    ab = yaml.dump(abc)

print(abc)
# print(ab)

# for item, doc in abc.items():
#     print(item, ":", doc)

# {'thanh_hoa': {'thu_nhap': 100, 'dan_so': 200}, 'ha_noi': {'thu_nhap': 300, 'dan_so': 500}}

# for x in abc: #.iteritems():
#     print("Dan so của {} là {}".format(x ,abc[x]["dan_so"]))
    # print(type(x))
    # print(x["dan_so"])
    # print(y) #["dan_so"])
    # print(type(y))

# Dan so của thanh_hoa là 200
# Dan so của ha_noi là 500

# for x in abc.iteritems():
#     print(x)
#     print(type(x))
#     print(x[0])
# ('thanh_hoa', {'thu_nhap': 100, 'dan_so': 200})
# <type 'tuple'>
# ('ha_noi', {'thu_nhap': 300, 'dan_so': 500})
# <type 'tuple'>

# ghi file
dict_file = {'year': 2022, 'month': 4,
'title1': [
    {"title2": "Document #2"},
    {"title3": "Document #3"}]}
# [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
# {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(save_file, 'w') as file:
    documents = yaml.dump(dict_file, file, indent=4)