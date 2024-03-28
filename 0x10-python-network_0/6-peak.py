# a program to find a pick number
# A number is peak if it is not smaller than its neighbor 
def find_peak(list_of_integers):
    peak = None;
    if not list_of_integers:
        return peak
    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                peak = list_of_integers[i]
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                peak = list_of_integers[i]
        else:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    peak = list_of_integers[i]
    return peak;
