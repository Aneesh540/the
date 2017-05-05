#creating a simple class program 
class Enemy:
	life =3
	def attack(self):
		print('ouch!')
		self.life -= 1

	def checklife(self):
			if self.life <= 0 :
				print("I'm dead")
			else:	
				print(self.life,'life left')



enemy1=Enemy()
enemy2=Enemy()

enemy1.attack()
enemy2.attack()
enemy1.attack()

enemy1.checklife()
enemy2.checklife()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')			

#Tap to open output
'''OUTPUT :
		ouch!
		ouch!
		ouch!
		1 life left 
		2 life left
'''
