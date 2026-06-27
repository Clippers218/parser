Server_logs = {
    "log_01": "2026-06-27 12.00.01:443",
    "log_02": "2026-06-27 12.00.15:23",
    "log_03": "2026-06-27 12.01.02:20",
    "log_04": "2026-06-27 12.02.45:3389", 
    "log_05": "2026-06-27 14.04.23:53",
    "log_06": "2026-06-27 14.05.54:53",
}

for log in Server_logs.values():
    words = log.split(" ")
    
    day = words[0]
    time_port = words[1]
    
    ports = time_port.split(":")
    
    port = ports[1]
    time = ports[0]
    
    print(f"port {port} accessed at {time} on {day}")
