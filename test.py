import os
import subprocess
# Get environment variables
env_var1 = str(os.environ['domain'])
env_var2 = str(os.environ['path'])
print("------------------------------------------")
print("first variable is " + env_var1)
print("second variable is"+env_var2)
print("------------------------------------------")
file_name = f"{env_var1}.txt"

# Create and write to the file
with open(file_name, "w") as file:
     file.write(f"ENV_VAR1: {env_var1}\n")
     file.write(f"ENV_VAR2: {env_var2}\n")

subprocess.run(["scp","-P 2222", file_name ,"zeyad@154.180.31.255:/home/zeyad/Desktop/" ])
