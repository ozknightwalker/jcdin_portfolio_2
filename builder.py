from __future__ import unicode_literals

import subprocess

steps = (
    'npm install',
    'NODE_ENV=production npm run build:prod',
)

for step in steps:
    subprocess.call(step, shell=True)
