import subprocess
# Install dependencies if not already installed
subprocess.call(['pip', 'install', 'psutil'])
subprocess.call(['pip', 'install', 'py-cpuinfo'])


import platform
import psutil
import cpuinfo


def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return system_info

def get_cpu_info():
    cpu_info = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "CPU Frequency": f"{psutil.cpu_freq().current:.2f} MHz"
    }
    return cpu_info

def get_memory_info():
    memory_info = {
        "Total Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "Available Memory": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
        "Used Memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
        "Memory Usage": f"{psutil.virtual_memory().percent}%"
    }
    return memory_info

def get_disk_info():
    disk_info = {}
    partitions = psutil.disk_partitions()
    for i, partition in enumerate(partitions):
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info[f"Disk {i+1}"] = {
                "Device": partition.device,
                "Mountpoint": partition.mountpoint,
                "File System Type": partition.fstype,
                "Total Size": f"{partition_usage.total / (1024 ** 3):.2f} GB",
                "Used": f"{partition_usage.used / (1024 ** 3):.2f} GB",
                "Free": f"{partition_usage.free / (1024 ** 3):.2f} GB",
                "Usage": f"{partition_usage.percent}%"
            }
        except PermissionError:
            continue
    return disk_info

if __name__ == "__main__":
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    cpu_info = get_cpu_info()
    print("\nCPU Information:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    memory_info = get_memory_info()
    print("\nMemory Information:")
    for key, value in memory_info.items():
        print(f"{key}: {value}")

    disk_info = get_disk_info()
    print("\nDisk Information:")
    for disk, details in disk_info.items():
        print(f"{disk}:")
        for key, value in details.items():
            print(f"\t{key}: {value}")
