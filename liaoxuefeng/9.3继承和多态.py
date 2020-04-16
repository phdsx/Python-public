class Animal():

    def run(self):
        print(f'{Animal.name(self)} is running...')
    def name(self):
        name="a"
        return name

b=Animal()
b.run()
