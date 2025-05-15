"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    pass 
    result = dict(students_dict)
    try:
        if operation=="add" :
            name, score = args
            result[name] = score
            return result
        elif operation =="remove":
            name = args[0]
            del result[name]
            return result
        elif operation =="update":
            name, new_score = args
            result[name] = new_score
            return result
        elif operation =="get":
            name = args[0]
            return result[name]
    except Exception as e:
        return students_dict 
    
    return result 