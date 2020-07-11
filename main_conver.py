from Disk.ReadWrite import *
from Config.ConfigDan import *
if __name__ == "__main__":
    print("== -- Start programm convert -- ==")
    rw = ReadWrite()
    config = ConfigDan(PathConfig = rw.path_start_config)

    z = config
