import subprocess
import os

def run_command(command):
    """Uruchamia polecenie systemowe i wyświetla jego wynik."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Polecenie wykonane pomyślnie:")
        print(stdout.decode())
    else:
        print("Błąd podczas wykonywania polecenia:")
        print(stderr.decode())

def grant_execute_permission():
    """Nadaje skryptowi uprawnienia do wykonywania."""
    script_path = os.path.abspath(__file__)
    print(f"Nadawanie uprawnień wykonywalnych dla: {script_path}")
    run_command(f"chmod +x {script_path}")

def update_system():
    """Wykonuje aktualizację i uaktualnienie systemu."""
    print("Rozpoczynam aktualizację systemu...")
    run_command("sudo apt update")

    print("\nRozpoczynam uaktualnienie pakietów...")
    run_command("sudo apt upgrade -y")

    print("\nAktualizacja i uaktualnienie zakończone.")

if __name__ == "__main__":
    grant_execute_permission()
    update_system()
