class Processor:
    def __init__(self):
        self._param = None
        self._fail_reason = None

    def process(self, param_name, param):

        if not self._do_process(param):
            self._fail_reason = self._get_fail_reason_msg() % param_name
            return False

        return True

    def _do_process(self, value):
        pass

    def _get_fail_reason_msg(self):
        pass

    def get_param(self):
        return self._param

    def get_fail_reason(self):
        return self._fail_reason
