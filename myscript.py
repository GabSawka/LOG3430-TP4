import os
import subprocess

badhash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
goodhash="bfdccab909c32635457d41eeb6e7fed322026170"
os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')