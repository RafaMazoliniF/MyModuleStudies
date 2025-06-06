import time
import signal
import sys

red = "\033[91m" 
norm = "\033[0m"

def handler(sig, frame):
    print("Encerrando monitoramento...")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

log_file = "results/ProcessosAltoRisco.txt"  # pode mudar o caminho e tem que ter a pasta e o arquivo

print("Monitorando processos de alto risco. Pressione Ctrl+C para sair.")

while True:
    try:
        with open("/proc/tea", "r") as f:
            lines = f.readlines()
            for line in lines[2:]:  
                if "Alto" in line: 
                    pid = line.split()[0]
                    print(f"\n{red}Processo PID: {pid} Alto Risco{norm}")
                    with open(log_file, "a") as log:
                        log.write(line)
        time.sleep(5) 
    except Exception as e:
        print(f"Erro ao acessar /proc/tea: {e}")
        time.sleep(5)
