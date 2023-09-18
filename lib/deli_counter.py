def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for index, name in enumerate(katz_deli, start=1):
            line_status += f" {index}. {name}"
        print(line_status) 


def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    position = len(katz_deli)
    print(f"Welcome, {new_customer}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!") 
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")       