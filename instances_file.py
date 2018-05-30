class myclass:
    def __init__(self, foo):
        self.myvar = foo

    def get_val(self):
        return self.myvar

    def set_val(self, new_val):
        self.myvar = new_val


my1 = myclass("Hello")
x = my1.get_val()
print(x)
my2 = myclass("Who")
x = my2.get_val()
print(x)
my3 = myclass("Not")
my3.set_val("Dis")
x = my3.get_val()
print(x)