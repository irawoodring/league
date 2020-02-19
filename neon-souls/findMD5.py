import os
import sys
import hashlib
import json

if len(sys.argv) != 2:
  print('Usage: python3 findMD5.py <path to neon-souls>')
  exit(1)

path = sys.argv[1]

git_path = os.path.join(path, '.git') 

print(path)

md5_dict = dict()

for root, dirs, files in os.walk(path):
  if not root.startswith(git_path) and not bool(root.count('__pycache__')):
    for file in files:
      with open(os.path.join(root, file), 'rb') as f:
        data = f.read()
        md5_data = hashlib.md5(data).hexdigest()
        md5_dict[file] = md5_data

with open('neon-souls-md5-data.json', 'w') as file:
  json.dump(md5_dict, file)

