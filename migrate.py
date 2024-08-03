import subprocess
import os

# Hedef PostgreSQL sunucusuna bağlantı bilgileri
host = "your-host"
port = "your-port"
dbname = "your-dbname" 
username = "your-username"
password = "your-password"
backup_file = "your-backup-filename"
# pg_restore komutunu oluşturma
restore_command = (
    f"PGPASSWORD={password} pg_restore "
    f"-h {host} -p {port} -U {username} -d {dbname} -v {backup_file}"
)

try:
    # pg_restore komutunu çalıştırma
    subprocess.run(restore_command, shell=True, check=True)
    print("Restore successful")
except subprocess.CalledProcessError as e:
    print("Restore failed:", e)
