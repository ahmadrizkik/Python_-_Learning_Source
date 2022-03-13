      #=========================#
      ####==== Catatan 1 ====####
      # class method
      #=========================#

# semua di class dapat dipanggil
class Player:
    def getName(self, name1):
        self.name = name1
        return self.name

pemain = Player() # cara memanggil class butuh object (var)
                  # not use arg cause not init
print (pemain.getName('Alpha'))


      #=========================#
      ####==== Catatan 2 ====####
      # init in class method
      #=========================#

# init otomatis dipakai saat memanggil class
class Player:
    # init tidak perlu var dan direturn
    def __init__(self, name1, speed1):
        self.name  = name1
        self.speed = speed1
    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed

player1 = Player('alpha', '68') # wajib mengisi parameter karena init
player2 = Player('beta', '78')

print (player1.getName() + ' punya speed ' + player1.getSpeed())
print (player2.getName() + ' punya speed ' + player2.getSpeed())

# atau pakai code ini

class Player:
    def __init__(self, name1, speed1):
        self.name  = name1
        self.speed = speed1

player1 = Player('alpha', '68')
player2 = Player('beta', '78')

# can print str cause init yang telah menjalankan code
print (player1.name, player1.speed)
print (player2.name, player2.speed)


      #=========================#
      ####==== Catatan 3 ====####
      # child class method
      #=========================#

# class utama disebut parent class
class Player:
    def __init__(self, name1, speed1):
        self.name  = name1
        self.speed = speed1

# child class adalah class baru 
# disertai nilai dari parent class
class PlayerLaos(Player):
    def setAge(self, age1):
        self.age = age1
        return self.age

player1 = PlayerLaos('alpha', '89')
print (player1.name + ' umurnya ' + player1.setAge('23'))


      #=========================#
      ####==== Catatan 4 ====####
      # override method
      #=========================#

class Player:
    def __init__(self, name1, speed1):
        self.name  = name1
        self.speed = speed1
    def setSkill(self):
        return 'normal'

# override mirip ganti ([]) di list or dict
class PlayerLaos(Player):
    def setSkill(self):
        return 'gacor'
class PlayerCina(Player):
    pass

player1 = PlayerLaos('alpha', '89')
player2 = PlayerCina('beta', '78')

print (player1.name + ' skillnya ' + player1.setSkill())
print (player2.name + ' skillnya ' + player2.setSkill())


      #=========================#
      ####==== Catatan 5 ====####
      # super method
      #=========================#

class Player:
    def __init__(self, name1):
        self.name  = name1

# saat di print akan eror
# karena ada init di child saat ada init di parent
class PlayerLaos(Player):
    def __init__(self):
        print ('Hallo Player Laos')
pemain1 = PlayerLaos('Alpha')
print (pemain1)

# menggunakan cara ini
class PlayerLaos(Player):
    def __init__(self, name1):
        Player.__init__(self, name1) # gunakan ini
        print ('Hallo Player Laos')
pemain1 = PlayerLaos('Alpha')
print (pemain1.name)

# disederhanakan dengan super
class PlayerLaos(Player):
    def __init__(self, name1):
        super().__init__(name1) # metode super
        print ('Hallo Player Laos')
pemain1 = PlayerLaos('Alpha')
print ('Nama pemain Laos yaitu ' + pemain1.name)


      #=========================#
      ####==== Catatan 6 ====####
      # protected/privated data
      #=========================#

class player:
    def __init__(self, name1):
        self.name = name1
        self._age = '23' # (_) symbol for another programmer
                         # abt privated data
        self.__skill = 'api' # error when being printed,
                             # unless use func
    def getSkill(self):
        return self.__skill
namaplayer = player('alpha')
namaplayer.name = 'Beta' # change value func
namaplayer.__skill = 'air' # will not change
namaplayer._player__skill = 'tanah' # getting change
print (namaplayer.name)
print (namaplayer._age)
print (namaplayer.__skill) # will eror
print (namaplayer.getSkill()) # can acces privated


      #=========================#
      ####==== Catatan 7 ====####
      # classmethod and staticmethod
      #=========================#

class fruit:
    def __init__(self, fruit1, size1):
        self.name1 = fruit1
        self.size1 = size1
    def getSmallFruit(self, fruit2, size2):
        self.name2 = fruit2
        self.size2 = size2
        return self.name2, self.size2

    @staticmethod
    # statmet can print without object and self arg
    def fruitColour(colour1):
        return 'Apple warnanya adalah ' + colour1
    
    @classmethod
    # clasmet same with statmed, but need cls arg
    # classmet can acces statmed, but cant parent
    # bcos parent have self arg
    def fruitColour1(cls, colour2):
        return cls.fruitColour(colour2)

fruitA = fruit('Apple', 'Big')
print (fruitA.name1 + ' ' + fruitA.size1)
print (fruitA.getSmallFruit('Mango', 'Small'))

print (fruit.fruitColour('merah')) # can print without object
print (fruit.fruitColour1('red'))


      #=========================#
      ####==== Catatan 8 ====####
      # property dan setter
      #=========================#

class fruit:
    def __init__(self, name1, size1):
        self.name = name1
        self.size = size1

    @property
    # properti change func into basic variabel
    def infoFruit(self):
        return self.name + ' ukurannya ' + self.size

    @infoFruit.setter
    # setter to change data in property
    def infoFruit(self, data):
        name1, size1 = data.split(' ')
        self.name = name1
        self.size = size1


fruitOne = fruit('Apple', 'Big')
fruitOne.infoFruit = 'AppleFlorin SoBig'
print (fruitOne.infoFruit) # dont use () cause not func