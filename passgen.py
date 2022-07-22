from random import *

class passgen:

    def generate(num):
        run = True
        import sys
        while run == True: # loop
            print("Can your password contain special characters? (y/n) (you can also type quit)")
            answer = input()
            if answer == "n": # if the answer is no
                for i in range(num):
                    import random
                    import string
                    seqs = string.ascii_lowercase, string.ascii_uppercase, string.digits
                    item = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
                    print(item)
                    break
                break

            elif answer == "Yes" or "yes" or "y": # if the answer is yes
                for i in range(num):
                    import random
                    import string
                    seqs = string.ascii_lowercase, string.ascii_uppercase, string.digits
                    item = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
                    print(item)
                    break
                break

            elif answer != "n" or "y": # if the answer is neither
                print("Please select between 'Yes' and 'No' ")
                continue

            elif answer != "quit":
                sys.exit()
                break
            break