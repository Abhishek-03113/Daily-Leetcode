from stack import Stack

def convert_int_to_bin(dec_num):

  mod = 0 
  stack = Stack()
  answer = ""

  while dec_num!=0:
    mod = dec_num %2 
    stack.push(mod)
    dec_num = dec_num//2
    print(mod,stack.get_stack())

    
  
  print(stack,"stack")
  while stack.is_empty() != True:
    answer += str(stack.pop())



  print(answer,"answer")

convert_int_to_bin(5)
