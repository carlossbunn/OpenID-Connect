import subprocess

def start_keycloak_server():
    try:
        # Execute o comando para iniciar o servidor Keycloak em modo de desenvolvimento
        subprocess.run(["./keycloak-23.0.7/bin/kc.sh", "start-dev"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o servidor Keycloak: {e}")

if __name__ == "__main__":
    start_keycloak_server()
