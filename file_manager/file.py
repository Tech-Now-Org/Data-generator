from extension import isformat

class File_manager:
    """_summary_: Create file, delete, update
    """
    def __init__(self):
        pass

    def create(self, filename):
        self.filename = filename

        if isformat(self.filename):
            try:
              f = open(self.filename, 'x')
              f.close()
              print(f'{filename} created!')
            except:
              print('Something went wrong')
            finally:
              print('The try except is finished')
        else:
          print('file extension is not acceptable')

    def gettinfo(self, filename, type):
        self.filename = filename
        self.type = type
        x = ''
        try:
          print(x)
        except:
          print('Something went wrong')
        finally:
          print('The try except is finished')
    
    def update(self, filename, update, position):
        self.filename = filename
        self.update = update
        self.position = position
        x= ''
        try:
          print(x)
        except:
          print('Something went wrong')
        finally:
          print('The try except is finished')
    
    def delete(self, filename):
        self.filename = filename
        x = ''
        try:
          print(x)
        except:
          print('Something went wrong')
        finally:
          print('The try except is finished')
  
    def save(self, save_as):
        
        self.save_as = save_as

        # check if filename include the supprted file type
        try:
            with open(self.save_as, 'w') as f:
               f.writelines()
            print(f'{save_as} saved!')
        except:
            print('Something went wrong when saving file content')
        finally:
            print('The try except is finished')