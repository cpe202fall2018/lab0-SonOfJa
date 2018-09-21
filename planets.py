def weight_on_planets():
   # write your code here
   earthWeight = int(input('What do you weigh on earth? '))
   print('\nOn Mars you would weigh ' + str(earthWeight*.38) + ' pounds.\nOn Jupiter you would weigh ' + str(earthWeight*2.34) + ' pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
