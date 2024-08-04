import time
import subprocess
import sys

def run_script():
    try:
        # Replace 'your_script.py' with the name of your script
        subprocess.run([sys.executable, 'thread3.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Script failed with error: {e}")
        print("Waiting for 1 minute before restarting...")
        time.sleep(180)  # Wait for 1 minute (60 seconds)
        run_script()  # Restart the script

if __name__ == "__main__":
    run_script()
