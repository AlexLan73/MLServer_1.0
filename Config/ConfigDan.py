class ConfigDan:
    import os, json, copy

    def __init__(self, **kwargs):
        print("  --- class ConfigDan --")

        _path_file_name_config = kwargs.get("PathConfig", self.os.getcwd()+"\\+mlserver.json")   # path config
        self.all_config = self.read(_path_file_name_config)

        self.car_name = kwargs.get("Car name", "")                                          # name car

        self.clexport, self.lrf_dec, self._config_car = dict(), dict(), dict()

        self.set(self.car_name)

    def save(self, path, dan_json):
        with open(path, 'w') as f:
            f.write(self.json.dumps(dan_json))

    def read(self, file):
        self.all_config = {}
        try:
            k = file.index(".json") > 0
        except:
            file = file + ".json"

        if self.os.path.isfile(file):
            with open(file, 'r') as json_file:
                try:
                    self.all_config = self.json.load(json_file)
                    return self.all_config
                except:
                    print("  Ошибка в файле {}", format(file))
                    return self.all_config
        return self.all_config

    def set(self, car_name):
        def __set_default(self, config):
            self.clexport = self.copy.deepcopy(config.get("clexport", {
                "MDF": " -v -~ -o -t -l \"file_clf\" -MB -O  \"my_dir\" SystemChannel=Binlog_GL.ini"
            }))
            self.lrf_dec = self.copy.deepcopy(config.get("lrf_dec", " -S 20 -L 512 -n -k -v -i "))

        if "Car name" in self.all_config:       # проверка существует ли в конфигурации раздел Car name

            self._config_car = self.all_config["Car name"]
            if car_name in self._config_car:
                _config = self._config_car[car_name]
                __set_default(self, _config)

        else:
            __set_default(self, self.all_config)
