x = -32760
for i in range(180):
    print('{"'+hex(0x100 + i)+'": '+f'{str(x)}'+"},")
    x+= 364