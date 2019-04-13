from enum import Enum
from resolver import ParamsResolver
from inspect.examiner import ExaminerIsIntString
from inspect.examiner import ExaminerInEnum
from inspect.examiner import ExaminerWrappedTest
from inspect.transformer import TransformerStringToInt

if __name__ == '__main__':

    class SortDirection(Enum):
        ASC = "asc"
        DESC = "desc"
    
    def fail_action(fail_reason):
        print("Fail action called, fail_reason %s" % fail_reason)
        
    def is_valid_col_name(column_name):
        return column_name in ("id", "name", "format")        
    
    pr = ParamsResolver();
    pr.register_fail_action(
        fail_action
    ).add(
        "page-index", processors=(ExaminerIsIntString(), TransformerStringToInt()), 
        optional=True, default="0"
    ).add(
        "page-size", processors=(ExaminerIsIntString(), TransformerStringToInt()), 
        optional=True, default="5"
    ).add(
        "sort-col",
        processors=(ExaminerWrappedTest(is_valid_col_name, "Param %s has invalid value."),),
        optional=True, default="id"
    ).add(
        "sort-direct",
        processors=(ExaminerInEnum(SortDirection),),
        optional=True, default="asc"
    )

    request_args = {
        "page-index": "1",
        "page-size": "100",
        "sort-col": "id",
        "sort-direct": "asc"
    }

    r = pr.process(request_args)
    
    print("Result: %s" % r)
    
    for param in pr:
        print("Param %s=%s, type of %s" % (param[0], param[1], type(param[1])))