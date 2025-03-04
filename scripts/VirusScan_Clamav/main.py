import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Błąd: {e.stderr.decode()}")

def main():
    print("Zatrzymywanie usługi ClamAV Freshclam...")
    execute_command("sudo systemctl stop clamav-freshclam")
    
    print("Aktualizacja bazy wirusów...")
    execute_command("sudo freshclam")
    
    print("Uruchamianie i włączanie usługi ClamAV Freshclam...")
    execute_command("sudo systemctl start clamav-freshclam && sudo systemctl enable clamav-freshclam")
    
    print("Skanowanie dysku...")
    execute_command("sudo clamscan -r /")

if __name__ == "__main__":
    main()