import os
import subprocess

host = "your-host"
port = "your-port"
dbname = "your-dbname" 
username = "your-username"
password = "your-password"
backup_file = "your-backup-filename"

# pg_dump komutunu çalıştırma
dump_command = f"PGPASSWORD={password} pg_dump -h {host} -p {port} -U {username} -d {dbname} -F c -b -v -f {backup_file}"

try:
    subprocess.run(dump_command, shell=True, check=True)
    print("Backup successful")
except subprocess.CalledProcessError as e:
    print("Backup failed:", e)




