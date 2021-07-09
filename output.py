import subprocess

with open("output_certs.txt", "w+", encoding='utf-8') as output:
    subprocess.call(["python", "./certs_check.py"], stdout=output);
