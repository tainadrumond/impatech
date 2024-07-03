# EXERCÍCIO 4
class Point2D():
    def __init__(self, x: float, y: float):
        self.coord: tuple[float, float] = (x, y)
    
    def __str__(self):
        return f'({str(self.coord[0])}, {str(self.coord[1])})'

class Polygon():
    def __init__(self, points: list[Point2D], color: str):
        self.points = points
        self.color = color
    
    def __str__(self):
        lines = [f'color={self.color}']
        for point in self.points:
            lines.append(str(point))
        return '\n'.join(lines)
        
class Polygons():
    def __init__(self):
        # Atributo polygons: Dicionário cuja chave é o nome do polígono e o valor é o objeto de Polygon correspondente.
        # A modelagem dessa classe não permite que sejam armazenados dois objetos de Polygon diferentes com o mesmo nome.
        self.polygons: dict[str, Polygon] = {}
        
    def add_polygon(self, polygon: Polygon, name: str):
        self.polygons[name] = polygon
    
    def remove_polygon(self, name: str):
        if self.polygons.get(name) is not None:
            self.polygons.pop(name) # Retira o polígono com o nome dado do dicionário caso ele exista
            
    def save_to_file(self, filename: str):
        '''
        Salva os polígonos em um arquivo texto no diretório dado. 
        O arquivo tem o seguinte formato para cada polígono salvo:
        "
        POLYGON {polygon name}
        color={polygon color}
        {(x1, y1)}
        {[...]}
        {(xn, yn)}
        "
        '''
        polygons_str = []
        for name in self.polygons.keys():
            polygon_str = f"POLYGON {name}\n"
            polygon_str += str(self.polygons[name])
            polygons_str.append(polygon_str)
            
        file = open(filename, mode='w')
        file.write('\n'.join(polygons_str))
        file.close()
    
    def load_from_file(self, filename: str):
        file = open(filename, mode='r')
        content = file.read()
        
        polygons_info = content.split("POLYGON ") # Separa o conteúdo referente a cada polígono
    
        for polygon_info in polygons_info:
            if polygon_info == '': # Evita a manipulação de elementos vazios após a separação do conteúdo do arquivo
                continue
            
            lines = polygon_info.split('\n') # Pega cada linha de informação do polígono
            name = lines[0] # A primeira linha é correspondente ao nome do polígono
            color = lines[1][6:] # Retira o "color=" para obter apenas a string correspondente à cor
            points = []
            for point_str in lines[2:]:
                if point_str == '': # Evita a manipulação de elementos vazios após a separação das linhas de coordenadas
                    continue
                coordinates_str = point_str[1:-1].split(', ') # Retira os parêntesis e separa as coordenadas pela vírgula
                point = Point2D(float(coordinates_str[0]), float(coordinates_str[1]))
                points.append(point)
            polygon = Polygon(points, color)
            self.add_polygon(polygon, name)

if __name__ == "__main__":
    polygons = Polygons()
    point1 = Point2D(0, 0)
    point2 = Point2D(2, 0)
    point3 = Point2D(1, 1)
    points = [point1, point2, point3]
    triangle = Polygon(points, "blue")
    polygons.add_polygon(triangle, "Triangle")
    
    point1 = Point2D(3, 0)
    point2 = Point2D(3, 2)
    point3 = Point2D(5, 0)
    point4 = Point2D(5, 2)
    points = [point1, point2, point3, point4]
    square = Polygon(points, "purple")
    polygons.add_polygon(square, "Square")
    
    polygons.save_to_file("polygons1.txt")
    polygons.remove_polygon("Triangle")
    polygons.save_to_file("polygons2.txt")
    
    polygons2 = Polygons()
    polygons2.load_from_file("polygons1.txt")
    polygons2.save_to_file("polygons1_copy.txt")