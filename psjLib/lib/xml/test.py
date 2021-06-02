import xml.etree.ElementTree as ET

def apply_indent(elem, level = 0):
    # tab = space * 2
    indent = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for elem in elem:
            apply_indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent

"""
doc = ET.parse("C:/Users/ff/PycharmProjects/psjLib/data/xml/table_template_1.xml")
root = doc.getroot()

#print(root)
#print(root.find("owner").text)


root.find("owner").text = "CARMAN"
root.find("eng_name").text = "T_COMM_CODE"
root.find("kor_name").text = "공통코드관리"
root.find("comment").text = "코멘트 내용"

cols = root.find("cols")

print(cols)

print(cols.makeelement())

for col in cols.iter("col"):
    col.find("eng_name").text = "111"
    col.find("kor_name").text = "222"
    col.find("origin_data_type").text = "333"
    col.find("convert_data_type").text = "444"

    #print(col.find("eng_name").text)
    #print(col.find("kor_name").text)
    #print(col.find("origin_data_type").text)
    #print(col.find("convert_data_type").text)

ET.Element("last_updated")
ET.Element("last_updated")
ET.Element("last_updated")
ET.Element("last_updated")

doc.write("C:/Users/ff/PycharmProjects/psjLib/data/output/table_template_1_out.xml",
          encoding="utf-8", xml_declaration=True)

"""
