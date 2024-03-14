import time
import subprocess
import multiprocessing

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    scripts = ["sub.py", "sub2.py", "sub3.py", "sub4.py"]

    processes = [multiprocessing.Process(target=run_script, args=(script,)) for script in scripts]

    for process in processes:
        process.start()
        time.sleep(3)

    for process in processes:
        process.join()