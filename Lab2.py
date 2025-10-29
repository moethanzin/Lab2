def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers seperated by commas (e.g. 5,67,32)")

def get_user_input():
    print("get_user_input")
    x = input()
    txt = list(x.split(","))
    float_list = list(map(float, txt))
    return(float_list)

def calc_average(values):
    print("calc_average")
    avg = sum(values)/len(values)
    return(avg)

def find_min_max(tlist):
    print("find_min_max")
    mm = [min(tlist),max(tlist)]
    return(mm)

def sort_temperature(slist):
    print("sort_temperature")
    s = sorted(slist)
    return(s)

def calc_median_temperature(mlist):
    print("calc_median_temperature")
    n = len(mlist)
    mid = n // 2
    if n % 2 == 1:
        return mlist[mid]
    else:
        return (mlist[mid - 1] + mlist[mid]) / 2.0

def main():
    print("ET0735(DevOps for AIoT) Lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    print("average= ", average)
    minimum = find_min_max(num_list)
    print("min,max= ", minimum)
    sorted_list = sort_temperature(num_list)
    print("sorted list = ", sorted_list)
    median = calc_median_temperature(sorted_list)
    print("madian= ", median)

if __name__ == "__main__":
    main()