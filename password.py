# Question num 6:

'''   PASSWORD CHECKER '''

def password_check(passwd): 
      
    SpecialSym =['!','@', '#', '$', '%', '^','&', '*', '( )', '+', '=', '_', '-','{ }', '[ ]', ':', ';', '”', '’', '?', '< >' ,','] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 25: 
        print('length should be not be greater than 24') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one digit 0-9') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter A-Z') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter a-z') 
        val = False

    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols !$@#%') 
        val = False
    if val: 
        return val 

def main(): 
    passwd = "Fhg93@"       
    if (password_check(passwd)): 
        print("Password is valid")
    elif passwd is "P1zz@":
        print('false // too short')
    else: 
        print("Invalid Password!") 
                   
main() 
