# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


msg = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = 0

def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
        
# check if number is a digit (used in function check())        
def is_one_digit(v):
    if (v < 10) and (v > -10) and ((v % 1) == 0):
        return True
    else:
        return False
        
#  checking the lever of laziness
def check(x, y, oper):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1) or (y == 1):
        msg = msg + msg_7
    if ((x == 0) or (y == 0)) and (oper in ['+', '-', '*']):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)        


while True:
    
    #read values
    print(msg_0)
    x, calc, y = input().split()

    #assigninig memory
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
        
    
    #checking if x, calc, y are correct
    if isfloat(x)==False or isfloat(y)==False:
        print(msg_1)
        continue
    if (calc in ['+', '-', '*', '/'])==False:
        print(msg_2)
        continue
    
    #str -> float
    x = float(x)
    y = float(y)
    
    check(x, y, calc)
    
    
    if calc == '+':
        result = x + y
    elif calc == '-':
        result = x - y
    elif calc == '*':
        result = x * y
    elif calc == '/' and y == 0:
        print(msg_3)
        continue
    else:
        result = x / y
        
    print(result)
    
    #answer: memory
    continue_loop = True
    
    while continue_loop == True:
        print(msg_4)
        answer_4 = input()  
        if answer_4 == 'y':
            
            
            if is_one_digit(result):
                msg_index = 10
    
                while True:
                    print(msg[msg_index])
                    answer3 = input()
                    if answer3 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            continue_loop = False
                            break
                    elif answer3 == 'n':
                            continue_loop = False
                            break
                    else:
                        continue

            else:
                memory = result
                continue_loop = False
            
        elif answer_4 == 'n':
            break
        else:
            continue    
    
    while True:
        print(msg_5)
        answer_5 = input()
        if (answer_5 in ['y','n']) == False:
            continue
        else:
            break
    if answer_5 == 'y':
        continue
    else:
        break