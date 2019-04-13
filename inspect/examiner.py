from .processor import Processor


class ExaminerIsIntString(Processor):
    def __init__(self):
        Processor.__init__(self)

    def _do_process(self, value):
        try:
            self._param = value
            return value.isdigit()
        except Exception as e:
            return False

    def _get_fail_reason_msg(self):
        return "Param %s is not integer string."


class ExaminerInEnum(Processor):
    def __init__(self, enum):
        Processor.__init__(self)
        self.__values = tuple(item.value for item in enum)

    def _do_process(self, value):
        try:
            self._param = value
            return value in self.__values
        except Exception as e:
            return False

    def _get_fail_reason_msg(self):
        return "Param %s has invalid value."


class ExaminerWrappedTest(Processor):
    def __init__(self, test, fail_msg_template):
        Processor.__init__(self)
        self.__wrapped_test = test
        self.__fail_msg_template = fail_msg_template

    def _do_process(self, value):
        try:
            self._param = value
            return self.__wrapped_test(value)
        except Exception as e:
            return False

    def _get_fail_reason_msg(self):
        return self.__fail_msg_template
