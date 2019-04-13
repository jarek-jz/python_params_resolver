from .processor import Processor


class TransformerStringToInt(Processor):
    def __init__(self):
        Processor.__init__(self)

    def _do_process(self, value):
        try:
            self._param = int(value)
            return True
        except Exception as e:
            return False

    def _get_fail_reason_msg(self):
        return "Transform param %s to int fail."
