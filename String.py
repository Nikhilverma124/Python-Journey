#string always take extra space because it store unicord
st='12345 kdjfs   !@#$R%^&'     #we can write in ""  ''  choice or abh charcter khatam krr diya gya hai woh purane version me tha
print(type(st))


a="A"
print(ord(a))    #ord used to the unicord of character o/p- 65

b=65
print(chr(b))   #chr convert unicord into character o/p- A


c="hello brother"   #access with indexing positive which start from start

# there is also negitive indexing which start from end
print(c[3])  #positive index  o/p- l
print(c[-1])  #negitive index  o/p- r


#slice
a="sher coder"

print(a[0:4:1])   #[start : end: step]   #end is not include itself

print(a[5: 10 : 1])
