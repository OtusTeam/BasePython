import configparser

config = configparser.ConfigParser()
config.read('config.ini')

for el in config:
    print(el)
    print(config[el].items())

# print(config.sections())
#
# print(config.read('config.ini'))
#
# # print(config.sections())
# # print(config['DEFAULT'])
# # print(config['bitbucket.org'])
# # print(config['topsecret.server.com'])
# # print(dir(config['topsecret.server.com']))
#
# print(config['bitbucket.org']['User'])
# print(config['DEFAULT']['Compression'])
# topsecret = config['topsecret.server.com']
# print(topsecret['ForwardX11'])
# print(topsecret['Port'])
# for key in config['bitbucket.org']:
#     print(key)
