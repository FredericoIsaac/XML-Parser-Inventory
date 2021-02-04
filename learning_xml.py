
import xml.etree.ElementTree as ET


tree = ET.parse('exercice.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    """
    Output:
    country {'name': 'Liechtenstein'}
    country {'name': 'Singapore'}
    country {'name': 'Panama'}
    """
    
# root[0] acede ao primeiro filho

print(root[0][1].text)  # 2008
print(root[0][2].text)  # 141100

