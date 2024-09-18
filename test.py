import os

# Get environment variables
env_var1 = os.getenv('ENV_VAR1')
env_var2 = os.getenv('ENV_VAR2')
env_var3 = os.getenv('ENV_VAR3')

# Use ENV_VAR1 as the file name
file_name = f"{env_var1}.txt"

# Create and write to the file
with open(file_name, "w") as file:
    file.write(f"ENV_VAR1: {env_var1}\n")
    file.write(f"ENV_VAR2: {env_var2}\n")
    file.write(f"ENV_VAR3: {env_var3}\n")

print(f"File '{file_name}' created successfully with environment variables.")
