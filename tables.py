class UnionError(Exception):
    pass

class AppendingError(Exception):
    pass

class Table:
    def __init__(self, includeId=False):
        self.table = []
        self.names = []
        self.includeId = includeId

    def addRow(self, row):
        if(len(self.names) == len(row)):
            self.table.append(row)
        else:
            raise AppendingError("Row and Table is not the same size")
        

    def unionTables(self, table):
        if len(self.table[0]) == len(table.table[0]):
            self.table += table.table
        else:
            raise UnionError("Tables are not same size")
    
    def removeRow(self, id):
        self.table.remove(self.table[id])


    def __getCol(self, index):
        # retrieves a specified column
        col = []
        for i in range(len(self.table)):
            col.append(self.table[i][index])
        return col

    def __stringifyTable(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                self.table[i][j] = str(self.table[i][j])

    def __alignCol(self, col):
        self.__stringifyTable()
        # Aligns a given column
        sortedCol = sorted(col, key=len)
        longestElement = sortedCol[-1]
        for i in range(len(col)):
            if len(col[i]) < len(longestElement):
                dif = abs(len(col[i])-len(longestElement))
                col[i] += " "*dif
                
        return col

    def __alignTable(self):
        for i in range(len(self.table[0])):
            col = self.__alignCol(self.__getCol(i))
            for j in range(len(self.table)):
                for k in range(len(self.table[j])):
                    self.table[j][i] = col[j]

    def setColNames(self, row):
        self.names = row

    def getWidth(self, table):
        lenWords = 0
        endSpacers = 4
        middleSpacer = 3
        for i in range(len(table[0])):
            lenWords += len(table[0][i])

        return lenWords+endSpacers+(middleSpacer*len(table[0])-3)

    def __printSeparator(self):
        tableWidth = self.getWidth(self.table)
        separator = ""
        separator += "+"
        for i in range(len(self.table[0])):
            separator += "-"*(len(self.table[0][i])+2)
            separator += "+"

        print(separator)
        #print("+"+"-"*(tableWidth-2)+"+")

    def sort(self, index):
        self.table.sort(key=lambda x:x[index])

    def showTable(self):        
        self.table.insert(0, self.names)

        if (self.includeId):
            for i in range(len(self.table)):
                if i == 0:
                    self.table[i].append("Id")
                else:
                    self.table[i].append(i-1)

        # aligns the table before printing
        self.__alignTable()

        tableWidth = self.getWidth(self.table)
            
        # prints formatted content of table
        for i in range(len(self.table)):
            if i == 0:
                self.__printSeparator()
                for j in range(len(self.table[i])):
                    print("|", end=" ")
                    print(self.table[i][j], end=" ")
                print("|")
                self.__printSeparator()
                
            else:
                for j in range(len(self.table[i])):
                    print("|", end=" ")
                    print(self.table[i][j], end=" ")
                print("|")
        self.__printSeparator()
