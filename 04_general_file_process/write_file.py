import csv, json
foo = '[{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"13","x":"303085.81599999964","y":"2770737.1679999996"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"14","x":"303079.33000000007","y":"2770749.2290000003"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"15","x":"303081.6660000002","y":"2770734.08"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"53","x":"302427.90699999966","y":"2770939.6760000009"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"65","x":"302827.48199999984","y":"2770789.7559999991"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"67","x":"302841.8049999997","y":"2770791.1779999994"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"94","x":"302819.71499999985","y":"2770770.751"},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"145","x":"302859.67800000031","y":"2770709.5889999997"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"160","x":"302966.21899999958","y":"2770683.1539999992"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"170","x":"303080.43400000036","y":"2770641.135"},{"hasLocate":0,"isNum":0,"SEVEN_AREA":"","CENTER_AREA":"","num":"","SUPPLY_ID":"","x":"","y":""},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"262","x":"302716.64699999988","y":"2770393.9739999995"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"277","x":"302728.16399999987","y":"2770346.25"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"281","x":"302745.15699999966","y":"2770357.1420000009"},{"hasLocate":1,"isNum":0,"SEVEN_AREA":"1","CENTER_AREA":"1","num":"","SUPPLY_ID":"304","x":"302785.96100000013","y":"2770327.489"}]'

f = open('test222.json', 'w')
f.write(foo.encode('utf8'))
f.close()


infile = open('test222.json', 'r')
outfile = open('test222.csv', 'w')

writer = csv.writer(outfile)


x = json.loads(foo)
f = csv.writer(open("test.csv", "wb+"))

#write header
f.writerow(["hasLocate", "isNum", "SEVEN_AREA", "CENTER_AREA", "num"])

#write content
for x in x:
    print(x["y"])
    f.writerow([x["hasLocate"], x["isNum"], x["SEVEN_AREA"], x["CENTER_AREA"], x["num"]])
