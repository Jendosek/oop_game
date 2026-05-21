class EventLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__log = []
            cls._instance.__listeners = []
        return cls._instance

    def add_listener(self, listener):
        self.__listeners.append(listener)

    def log(self, message):
        self.__log.append(message)
        for listener in self.__listeners:
            listener(message)

    def show_log(self):
        if not self.__log:
            print("Журнал порожній.")
        else:
            for message in self.__log:
                print(f"  {message}")

    def clear(self):
        self.__log = []