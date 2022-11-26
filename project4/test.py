class Test:
	def __init__(self,x,y):
		self.x=x
		
	def getX(self):
		return self.x
		
	
def main():
	b = Test(2,3)
	
	print(b.getX())
	
main()
	
