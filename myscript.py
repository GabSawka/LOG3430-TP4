import os

badhash = "e6b41c365cf51aa324345c82fa39a7a81059d9c4"
goodhash="bfdccab909c32635457d41eeb6e7fed322026170"

os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')