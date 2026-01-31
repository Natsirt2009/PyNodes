

def todo(obj):
    print(f"\033[34mTODO: \033[0m'{obj.__module__}.?.{obj.__name__}'")
    return obj