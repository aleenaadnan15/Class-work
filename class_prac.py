class human():
    def __init__(self,fav_dish = 'biryani', name ='Ailn'):
        self.fav_dish = fav_dish
        self.name = name
        print('i am constructor')

h1 = human()
h2 = human('biryani' , 'Ad')
h3 = human()
h4 = human()
print(h1.name)
print(h2.name)
print(h2.fav_dish)