import argparse
import fileinput
import sys

# i need to read command from terminal and display my results in the terminal.
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input",nargs="*",help = "used for getting input.")
    parser.add_argument("-n",action = "store_true", help="Give the numbering")
    parser.add_argument("-b",action="store_true",help = "numbering without numbering blank lines.")

    args = parser.parse_args()

    if args.input and args.input[0] == "-" and len(args.input)<=1:
        input_data = sys.stdin.read()
        print(input_data)

    if args.n:
        input_data = sys.stdin.read()
        my_list = input_data.splitlines()
        for i in range(0,len(my_list)):
            print(f"{i+1}  ",end="")
            print(my_list[i])
    
    if args.b:
        input_data = sys.stdin.read()
        my_list = input_data.splitlines()
        for i in range(0,len(my_list)):
            if i%2==0:
                print(f"{int(i/2+1)}  ",end="")
                print(my_list[i])
            else:
                print(my_list[i])
    
    elif args.input:
        # print("BBBBBBB")
        for file in args.input:
            if file == "-":
                continue
            try:
                with open (file,"r",encoding="utf-8") as f:
                    content = f.read()
                    print(content,end="")
            except:
                print(f"There is no file name {file}.Please give the correct file name.")

