import sys
import os
import logging
from datetime import datetime

# Configuración básica
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "debug_extraction.log")
CONSOLE_LOG_FILE = os.path.join(LOG_DIR, "app_console_full.log")

# Configurar logger estructurado
logger = logging.getLogger("debug_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)

def log_debug(message):
    logger.debug(message)
    print(f"[LOG] {message}") 

def log_error(message):
    logger.error(message)
    print(f"[LOG ERROR] {message}")

# --- Nueva funcionalidad: Capturar todo STDOUT/STDERR ---

class DualLogger:
    """Escribe tanto en terminal como en archivo."""
    def __init__(self, filepath, stream):
        self.terminal = stream
        try:
            self.log = open(filepath, 'a', encoding='utf-8')
        except Exception as e:
            # Fallback if file cannot be opened, though this should be rare given check in setup
            self.terminal.write(f"!! Error opening log file {filepath}: {e}\n")
            self.log = None

    def write(self, message):
        self.terminal.write(message)
        if self.log:
            self.log.write(message)
            self.log.flush()  # Force write to disk

    def flush(self):
        self.terminal.flush()
        if self.log:
            self.log.flush()

def setup_full_console_logging():
    """Redirige sys.stdout y sys.stderr al archivo de log."""
    # Evitar doble redirección si ya se llamó
    if isinstance(sys.stdout, DualLogger):
        return

    print(f"--> Iniciando captura completa de consola a: {CONSOLE_LOG_FILE}")
    sys.stdout = DualLogger(CONSOLE_LOG_FILE, sys.stdout)
    sys.stderr = DualLogger(CONSOLE_LOG_FILE, sys.stderr)
