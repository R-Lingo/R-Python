import os

print(os.path.split('python/py'))
class scan():
    def __init__(self):
        self.d=[]
    def scan(self,dir):
        for i in os.scandir(dir):
            if i.is_dir():
                print(i.name)
                self.scan(i)
            else:
                self.d.append(i.path)
        
if __name__ == '__main__':
    sc = scan()
    sc.scan(dir='')