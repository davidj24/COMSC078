import math

def to_decimal(num_deg: int, minutes: int, sec):
    degrees_is_negative = num_deg < 0
    abs_degrees = abs(num_deg)
    abs_minutes = abs(minutes)
    abs_seconds = abs(sec)

    #Rolling over units
    abs_minutes += abs_seconds//60
    abs_seconds %= 60
    abs_degrees += abs_minutes//60
    abs_minutes %= 60

    return ((-1)**degrees_is_negative) * (abs_degrees + abs_minutes/60 + abs_seconds/3600) 




def main():
    degs = int(input("Please enter degrees: "))
    mins = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))
    print(f"That's {to_decimal(degs, mins, seconds)} decimal degrees")
    

if __name__=='__main__':
    main()