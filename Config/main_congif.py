
from ConfigDan import *


if __name__ == "__main__":
    print(" ~~~  Test ")
    _path_config = r"E:\MLserver\MLServer1.0"
    _config = ConfigDan()
    _name_file_config = "mlserver"
    _config_dan = _config.read(_path_config+"\\"+_name_file_config)
    _config.set("PS0001")
    k=1
