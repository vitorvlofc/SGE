# fix_pep8.py

import subprocess

print("Executando autopep8...")
subprocess.run([
    "autopep8",
    "--in-place",
    "--recursive",
    "--aggressive",
    "--aggressive",
    "."
])

print("Executando autoflake...")
subprocess.run([
    "autoflake",
    "--in-place",
    "--remove-all-unused-imports",
    "--recursive",
    "."
])

print("Concluído!")
