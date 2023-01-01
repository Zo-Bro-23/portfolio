import os

file = open('../../_config.yml', 'w+')

str = file.read()
str.replace('theme: moonwalk', '# theme: moonwalk')
str.replace('# remote_theme: abhinavs/moonwalk', 'remote_theme: abhinavs/moonwalk')

file.write(str)
file.close()
