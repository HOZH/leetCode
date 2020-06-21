


def transactions(sequence, balance):
  if balance <= 0:
        return "Invalid starting balance"

  init_balance,bonus = balance,balance//2
  valid_set = set([chr(i) for i in range(49,58)]+['+','-'])

  ops,nums ,temp_num,op,i=0,[],'',None,0

    
  while i<len(sequence):
      current = sequence[i]
      if  current not in valid_set:
        return "Invalid transactions"

      if current in {'+','-'}:
          ops+=1
          op = current
          current_op_pointer = i
        
          while i<len(sequence)-1:
              i+=1
              if sequence[i] in [str(i) for i in range(10)]:
                  temp_num+=sequence[i]
              else:
                  i-=1
                  break
              
              if op == '-':
                old_balance = balance
                balance-=int(temp_num)
                if balance <= 0:
                    return current_op_pointer,old_balance
              else:
                  balance+=int(temp_num)
              temp_num=''
      else:
          temp_num+=current

      i+=1

  return ops,balance if balance/init_balance<2 else balance+bonus



 

# Test cases
print(transactions('*1-9', 5))  
print(transactions('+9+8-8-3-4-5-1-6', 50))  
print(transactions('-4+7', 0))  
print(transactions('+3-8+6+2-7-2-1', 25))
print(transactions('+3-8*2', 25))  
print(transactions('+3+1', 4))  
print(transactions('+1-9-2-2', 3)) 
