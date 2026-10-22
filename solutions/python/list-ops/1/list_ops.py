def append(list1, list2):
    
    return [*list1, *list2]

def concat(lists):
  
    return [element for list_element in lists for element in list_element]


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    l = 0
    for _ in list:
        l += 1
    return l

def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    left_acc = initial
    for element in list:
        left_acc = function(left_acc, element)
    return left_acc

def foldr(function, list, initial):
    righ_acc = initial
    for element in list[::-1]:
        righ_acc = function(righ_acc, element)
    return righ_acc
    
def reverse(list):
    return list[::-1]
