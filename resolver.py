class ParamsResolver:
    def __init__(self):
        self.__processors = {}
        self.__optionals = {}
        self.__safe_params = {}
        self.__fail_action = lambda _: None
        self.__fail_reason = None

    def register_fail_action(self, action):
        self.__fail_action = action
        return self

    def add(self, param_name, optional=False, default=None, processors=()):
        self.__processors[param_name] = processors
        if optional:
            self.__optionals[param_name] = default

        return self

    def process(self, params):

        for param_name, processors in self.__processors.items():

            if param_name in params:
                param = params[param_name]
            elif param_name in self.__optionals:
                param = self.__optionals[param_name]
            else:
                self.__fail_reason = "Param %s not found." % param_name
                self.__fail_action(self.get_fail_reason())
                return False

            for p in processors:

                if p.process(param_name, param):
                    param = p.get_param()
                else:
                    self.__fail_reason = p.get_fail_reason()
                    self.__fail_action(self.get_fail_reason())
                    return False

            self.__safe_params[param_name] = param

        return True

    def get_fail_reason(self):
        return self.__fail_reason

    def __getitem__(self, name):
        return self.__safe_params.get(name)

    def __iter__(self):
        def g():
            for k, v in self.__safe_params.items():
                yield (k, v)

        return g()
