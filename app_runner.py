import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen(["<version/of/Python/used/within/the/venv>", "user_app/app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen(["<version/of/Python/used/within/the/venv>", "post_app/app.py"])

# Run the service corresponding to the shared messaging app
def run_shared_service():
    subprocess.Popen(["<version/of/Python/used/within/the/venv>", "message_app/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()
    run_shared_service()

    # Graceful Termination of the three subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating all processes. Alvida!")
