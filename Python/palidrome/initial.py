'''
The Palidrome python file

Finds if a number is a palidrome or not by excepting
user input of a number. Next, the program turns the
string into a list. Then the list is reversed and turned
back into a string where it will be compared to the
input or 'target'. If the list reversed produces the
same result as the target input then the number is a
palidrome, else, it is not...  
'''

class IsPalidrome:
    
    def __init__(self, target: str):
        """
        Checks to see if a number is a palidrome or not meaning, can a number be read the
        same forward and backwards

        Args:
                        
            target (str): The number to determine if it is a palidrome or not
        """
        self.target = target
        self.deli = ""
        
    def is_palidrome_single(self):
        # More of a testing function
        # Turn the target number into a list
        tgt_list = list(str(self.target))
        
        if list(reversed(tgt_list)) == tgt_list:
            print(f"[+] {self.target} is indeed a Palidrome.")
        else:
            print(f"[X] {self.target} is not a Palidrome.")
        

def main():
    # Test numbers
    numbers = [121, "998", "10", -121, 989898, 8899889]
    
    for number in numbers:
        pli = IsPalidrome(number)
        pli.is_palidrome_single()
        
main()
