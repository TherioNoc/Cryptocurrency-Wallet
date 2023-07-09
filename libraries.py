import subprocess

# List of required libraries
libraries = ['hashlib', 'ecdsa', 'web3', 'ccxt']

# Install each library using pip
for library in libraries:
    try:
        subprocess.check_call(['pip', 'install', library])
        print(f"Successfully installed {library}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {library}: {e}")
