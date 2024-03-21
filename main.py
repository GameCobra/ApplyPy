class Algebra:
    equationList = []
    Operations = ["+", "-", "*", "/", "!", "=", "(", ")", "^"]

    def __init__(self, equation: str) -> None:
        self.equation = equation

    #converts the equation atribute of the class to the equationList to allow for easyer usage latter
    #seperates each charecter in the equation to a different element in equationList
    def StringToList(self):
        for i in range(len(self.equation)):
            self.equationList.append(self.equation[i])

    
    #designed to be proceaded by the StringToList function
    #Searchs through equationList and removes all space elements
    #Dose this simply by going through every element in the list and removng it if it is a spaced
    def RemoveSpace(self):
        i = 0
        while i < len(self.equationList):
            if self.equationList[i] == " ":
                self.equationList.pop(i)
                i -= 1
            i += 1

    #Designed to be proceaded after the RemoveSpace function
    #will combine adgasent numbers in the equationList var to be a single number in a single element
    #NOTE: Add capability for negative numbers
    def SplitEquation(self):
        newEquationList = [""]
        for i in range(len(self.equationList)):
            for j in range(len(self.Operations)):
                if self.equationList[i] == self.Operations[j] or self.equationList[i - 1] == self.Operations[j]:
                    newEquationList.append("")
            newEquationList[len(newEquationList) - 1] =  str(newEquationList[len(newEquationList) - 1]) + self.equationList[i]
        self.equationList = newEquationList


    #Surchs the equationList var for the provided symobol
    #will return a list of all indexs where that symobol is pressent
    #it will return [] if that symbol is not in the equationList
    def DoseContainSymbol(self, symbolToSearchFor):
        for i in range(len(self.equationList)):
            if self.equationList[i] == symbolToSearchFor:
                return i
    
    def ConvertStringNumbersToInts(self):
        for i in range(self.equationList):
            for j in range(len(self.Operations)):
                pass

    #Gose through the EquationList to find the first "+" and adds the values on eather side of it
    #Takes the combi ned value and replaces the 3 elements used with the new calculated value
    def Addition(self):
        Indexs = self.DoseContainSymbol("+")
        self.equationList[Indexs] = str(float(self.equationList[Indexs - 1]) + float(self.equationList[Indexs + 1]))
        self.equationList.pop(Indexs + 1)
        self.equationList.pop(Indexs - 1)

    #Dose the same this as Addition
    #finds the first instance of "-" and dose subtraction on the 2 elements on either side of it
    def Subtraction(self):
        Indexs = self.DoseContainSymbol("-")
        self.equationList[Indexs] = str(float(self.equationList[Indexs - 1]) - float(self.equationList[Indexs + 1]))
        self.equationList.pop(Indexs + 1)
        self.equationList.pop(Indexs - 1)

    #Dose the same this as Addition
    #finds the first instance of "*" and dose multiplication on the 2 elements on either side of it
    def Multiplication(self):
        Indexs = self.DoseContainSymbol("*")
        self.equationList[Indexs] = str(float(self.equationList[Indexs - 1]) * float(self.equationList[Indexs + 1]))
        self.equationList.pop(Indexs + 1)
        self.equationList.pop(Indexs - 1)
    
    #Dose the same this as Addition
    #finds the first instance of "/" and dose division on the 2 elements on either side of it
    def Divistion(self):
        Indexs = self.DoseContainSymbol("/")
        self.equationList[Indexs] = str(float(self.equationList[Indexs - 1]) / float(self.equationList[Indexs + 1]))
        self.equationList.pop(Indexs + 1)
        self.equationList.pop(Indexs - 1)

    def Simplification(self):
        pass    

a = Algebra("7 + 2 * 10 - 6 / 2")
a.StringToList()
a.RemoveSpace()
a.SplitEquation()
a.Multiplication()
a.Divistion()
a.Addition()
a.Subtraction()
print(a.equationList)
