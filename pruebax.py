import xml.etree.ElementTree as ET



class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def load_xml(self):
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

    def parse_xml(self):
        if self.root is None:
            self.load_xml()

        self._parse_element(self.root)

    def _parse_element(self, element, level=0):
        # Polimorfismo: Usamos el polimorfismo aquí para manejar diferentes tipos de elementos XML.
        # Dependiendo del tipo de elemento, se pueden tomar acciones diferentes.
        
        if element.attrib:
            print("  " * level + "  Atributos:")
            for key, value in element.attrib.items():
                print("  " * level + f"    {key}: {value}")
        if element.text and element.text.strip():
            print("  " * level + f"  Texto: {element.text.strip()}")

        for child in element:
            self._parse_element(child, level + 1)
            print("")

            
try:

    if __name__ == "__main__":
     file_path = "archivo2.xml"
     parser = XMLParser(file_path)
     parser.parse_xml()
     
except : 
    
    raise ("No se ha podido encontrar o leer el archivo ")
    
    
