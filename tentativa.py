import xml.etree.ElementTree as ET
import csv

product_list = []
count_number_lines = 0
# Get info from XML
def info_xml(file_xml):

    tree = ET.parse(file_xml)
    root = tree.getroot()
    first_time = True

    for child in root:
        if first_time:
            first_time = False
            continue

        productCode = child[1].text
        productDescription = child[2].text
        productNumberCode = child[3].text
        closingStockQuantity = child[4].text
        closingStockValue = child[6].text
        global count_number_lines
        count_number_lines += 1


        product_list.append([productCode, productDescription, productNumberCode, closingStockQuantity, closingStockValue])




def write_csv(product_info):
  
    with open("first_try.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["productCode", "productDescription", "productNumberCode", "closingStockQuantity", "closingStockValue"])
        writer.writerows(product_list)





info_xml("piece_xml_30358.xml")
#print(product_list) 
#[['00000000000000000000', 'VELAS', '8428451021900', '17', '0.5691'], ['A11', 'SAPATO', 'A11', '4', '6.8699']]

#write_csv(product_list)




total_number_of_lines = count_number_lines * 9 + 1 + 9

file_number_of_lines = (242578) 

print(count_number_lines)
print(total_number_of_lines)
print(file_number_of_lines)
print(file_number_of_lines - total_number_of_lines)