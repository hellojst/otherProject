#! usr/bin/python
import mytestpyhon
# def method

def prin_tstr(str):
    print(str)
    return


# use method

prin_tstr("my def")


def change(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值:", mylist)
    return mylist


mylis = [20, 30, 50]
change(mylis)


