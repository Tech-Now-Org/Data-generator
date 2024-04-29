
def isformat(filename):
    if filename and filename in ['.json', '.csv','.txt','.xlsx']:
        return True
    else:
        return False