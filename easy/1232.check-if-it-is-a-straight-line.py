class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x_1 = coordinates[0][0]
        x_2 = coordinates[1][0]
        y_1 = coordinates[0][1]
        y_2 = coordinates[1][1]
        for i in range(2,len(coordinates)):
            x_3 = coordinates[i][0]
            y_3 = coordinates[i][1]
            #if ((x_3 - x_1) / (x_2 - x_1) != (y_3 - y_1) / (y_2 - y_1)):
            if ((x_3 - x_1) * (y_2 - y_1) != (y_3 - y_1) * (x_2 - x_1) ):
                return False
        return True
            
        #Tol = 1e-10 //По требованиям задачи или задать как входной параметр
#if abs((x_3 - x_1) / (x_2 - x_1) - (y_3 - y_1) / (y_2 - y_1)) <= Tol // Точки лежат на прямой