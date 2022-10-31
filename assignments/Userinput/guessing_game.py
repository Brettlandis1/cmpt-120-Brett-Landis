def start():
    
   # target to guess
   print('you have 3 tries')
   answer = 'Elephant'
   guess = ''
   guessNum = 1
  
   while(answer != guess and guessNum <= 3):
 
       guess = input('Guess an animal: ')
 
       if(answer == guess):
           print('good job')
           return True
       
       else:
           print('incorrect')   
           guessNum += 1
 
   return None
 
start()
