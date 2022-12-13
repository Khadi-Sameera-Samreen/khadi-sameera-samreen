def test(list):
    list=[5,6,5,19,19,5,5]
    return list.count(19)==2 and list.count(5)>=3
print(test(list))    