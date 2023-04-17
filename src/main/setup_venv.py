import os
import subprocess
import sys
import venv
import logging

FORMAT = '[%(asctime)s][%(levelname)s] %(module)s - %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S',)

logging.info("Creating virtual enviroment with required dependencies...")

# Define the name of the virtual environment
venv_name = 'venv'

# Get the current working directory
cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
print(cwd)

# Create the virtual environment
venv.create(os.path.join(cwd, venv_name), with_pip=True)

# Get the full path to the pip executable inside the virtual environment
if os.name == 'nt':  # For Windows
    bin_dir = "Scripts"
    pip_path = os.path.join(venv_name, bin_dir, "pip.exe")
else: # For Unix/Linux
    bin_dir = "bin"
    pip_path = os.path.join(venv_name, bin_dir, "pip")

# Install the required dependencies from requirements.txt
subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])

logging.info("Virtual enviroment setup completed succesfully")
