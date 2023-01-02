import os

file = open('./_config.yml', 'r')
str = file.read()
file = open('./_config.yml', 'w')

str = str.replace('theme: moonwalk', '# theme: moonwalk')
str = str.replace('# remote_theme: abhinavs/moonwalk', 'remote_theme: abhinavs/moonwalk')

file.write(str)
file.close()
