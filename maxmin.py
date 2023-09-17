def ask_user_for_num_list(msg):
  #Keeps requesting an input from the user with the given msg until an integer is entered
  bln_valid_input = False
  while not bln_valid_input:
    bln_valid_input = True
    num_list = input(msg).strip("[]").replace(" ","").split(",")
    for num in num_list:
      if not num.lstrip("-").isnumeric():
        bln_valid_input = False
        print("Invalid input - please try again.\n")
  
  return [int(num) for num in num_list]

def minmax(num_list):
  min = num_list[0]
  max = num_list[0]
  for num in num_list:
    if num > max:
      max = num
    elif num < min:
      min = num
  return min, max


num_list = ask_user_for_num_list("Please enter a list of numbers (in the format '[num1,num2,...,numx]'): ")
print(list(minmax(num_list)))