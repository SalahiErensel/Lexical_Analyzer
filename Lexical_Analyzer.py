INPUT_PATH = "readfile.txt"

KEYWORDS={ "for" : "FOR" , "while" : "WHILE" , "if" : "IF" , "else" : "ELSE" , "|" : "BITWISE_OR" , "||" : "LOGICAL_OR" , \
          "&" : "BITWISE_AND" , "&&" : "LOGICAL_AND"}

#symbol table for lexical analyzer

#count = index of last inserted element starts with 3 because first 4 elements are keywords

class SymbolTable :
    
    count = 3
    
    def __init__(self) :
        
        self.table = { "FOR" : "FOR_TOKEN" , "WHILE" : "WHILE_TOKEN" , "IF" : "IF_TOKEN"  , "ELSE" :"ELSE_TOKEN" , "x" : "ID", "size33" : "ID" }
        
        self.inv_table = {val : key for key , val in self.table.items()}
    
    def insert(self, identifier):
        
        if identifier in self.table:
            
            return self.table[identifier]
    
        self.count += 1
        
        self.table[identifier] = self.count
        
        self.inv_table[self.count] = identifier
        
        return self.count

    def str(self):
        
        headline = " ********SYMBOL TABLE********\n"
        
        return headline + "\n".join(["{} ----> {}".format(key,val) for key,val in self.inv_table.items()]) + "\n" + "=" *10

symbol_table = SymbolTable()

#object that lex() returns

class LexResult:
   
    def __init__(self , token , integer_value = None , float_value = None , index = None , unrecognized_string = None):
        
        self.token = token
        
        self.integer_value = integer_value
        
        self.float_value = float_value
       
        self.index = index 
        
        self.unrecognized_string = unrecognized_string
        
    def str(self):
        
        if self.token == "INTEGER":
           
            return "<token = {}, integer_value = {}>".format(self.token, self.integer_value)
        
        elif self.token == "FLOAT":
        
            return "<token = {}, float_value = {}>".format(self.token, self.float_value)
        
        elif self.token == "ID":
        
            return "<token = {}, index = {}>".format(self.token, self.index)
        
        elif self.token == "ERROR":
        
            return "<token = {}, unrecognized_string = {}>".format(self.token, self.unrecognized_string)
        
        else:
        
            return "<token = {}>".format(self.token)
    
    def read_file(path):
        
        file = open(path)
        
        input_string = []
        
        for word in file:
        
            input_string = word.split(" ")
        
        return input_string
        
    def show_menu():

        print("1.Call lex()")
    
        print("2.Show symbol table")
    
        print("3.Exit")

#get list of tokens from input string
    
    def get_tokens(string):
        
        tokens=string.split(' ')
        
        valid_tokens=[]
        
        for s in tokens:
            
            if s != ' ' and s != "" :
               
                if "\n" in s:
                    
                    valid_tokens += s.split("\n")
               
                else:
                   
                    valid_tokens.append(s)
            
            return valid_tokens

#Checking tokens

    def is_int(self, string):
        try:
           
            int(string)
            
            return True
        
        except ValueError:
            
            return False
    
    def is_float(self, string):
        
        try:
           
            float(string)
            
            return True
        
        except ValueError:
            
            return False
    
    def is_identifier(self, string):    
        
        return not self.is_int(self, string[0])

#Analyzing tokens
    
    def analyze(self, token):
        
        if token in KEYWORDS:
            
            return KEYWORDS[token]
       
        elif self.is_int(self, token):
            
            return "INTEGER"
       
        elif self.is_float(self, token):
           
            return "FLOAT"
       
        elif self.is_identifier(self, token):
                      
            return "ID"
       
        else:
           
            return "ERROR"
        
    def lex(self, token) :
        
        lex_result = self.analyze(self, token)
        
        return lex_result

    def Test(self, token):

        print(token)

    
if __name__ == "__main__" :
   while(True):
        lex = LexResult

        input_string = lex.read_file(INPUT_PATH)

        lex.show_menu()

        chosen_option = input("Choose one option:")

        if chosen_option == "3":

            exit(1)

        elif chosen_option == "2":

            print(symbol_table.table)

        elif chosen_option == "1":

            for  token in input_string :

                print(f'\nTOKEN IS = {token}')

                result = lex.lex(lex, token)

                print(f'\nLEXEME IS = {result}')
        else:

           print("ERROR INVALID OPTION!")
