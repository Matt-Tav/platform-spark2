import csv

sep = ','
pad = 'FFFF'
base = '201901ELC'
part = '218-0004-001-A'
bootver = '01.00.00.00000'
bootver_hex = ''.join(format(ord(c), "x") for c in bootver)
part_hex = ''.join(format(ord(c), "x") for c in part)
sn_start = 1
sn_end = 201
csv_row_data = []


for x in range(sn_start, sn_end):
	serial = '%s%05d' %(base, x)
	serial_hex = ''.join(format(ord(c), "x") for c in serial)
	config_hex = ''.join((serial_hex, pad, part_hex, pad, bootver_hex, pad))
	csv_row_data.append((serial, part, config_hex))
    #print(sep.join(csv_row_data))
    
    
with open('config.csv', mode='wb') as config_csv:
    config_csv = csv.writer(config_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in csv_row_data:
        config_csv.writerow(x)
        print x