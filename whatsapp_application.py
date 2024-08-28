class wappv1:
    def __init__(self,mno,name,dp):
        self.mno=mno
        self.name=name
        self.dp=dp
    def details(self):
        print(f'{self.mno}')
        print(f'{self.name}')
        print(f'{self.dp}')
class wappv2:
    def __init__(self,mno,name,dp,audiocall,status,vmsg):
        wappv1.__init__(self,mno,name,dp)
        self.audiocall=audiocall
        self.status=status
        self.vmsg=vmsg
    def details(self):
        wappv1.details(self)
        print(f'{self.audiocall}')
        print(f'{self.status}')
        print(f'{self.vmsg}')
class wappv3:
    def __init__(self,mno,name,dp,audiocall,status,vmsg,videocall,business,channels):
        wappv2.__init__(self,mno,name,dp,audiocall,status,vmsg)
        self.videocall=videocall
        self.business=business
        self.channels=channels
    def details(self):
        wappv2.details(self)
        print(f'{self.videocall}')
        print(f'{self.business}')
        print(f'{self.channels}')
user1=wappv1(1234,'p','given')
user1.details()
print('_'*20)
user2=wappv2(4515,'q','notgiven','yes','no','yes')
user2.details()
print('_'*20)
user3=wappv3(4512,'r','notgiven','yes','no','yes','no','yes','yes')
user3.details()
print('_'*20)
