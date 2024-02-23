import subprocess
import os

# Define the paths to the scripts that need to be run
scripts_to_run = [
    os.path.join(os.path.dirname(__file__), 'csv_json.py'),
    os.path.join(os.path.dirname(__file__), 'download.py'),
    os.path.join(os.path.dirname(__file__), 'save_path.py')
]

# Iterate through each script and execute them one by one
for script in scripts_to_run:
    print(f"Running {script}")
    subprocess.run(['python', script], check=True)
    print(f"Finished running {script}")
