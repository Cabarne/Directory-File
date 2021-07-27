

class Directory:
    def __init__(self,name):
        self.name = name
        self.files = []
        
    def pasteFile(self,file):
        a = True
        for i in range(len(self.files)):
            if file.name == self.files[i].name:
                a = False
        if a == True:
            self.files.append(file)
        
    def deleteFile(self, fileName):
        for i in self.files:
            if fileName == i.name:
                self.files.remove(i)
                
    def __str__(self):
        content = ""
        for file in self.files:
            content += str(file)
        return f"Dir {self.name:15}\n{content}"

class File:
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f"\tFile --- {self.name:15}\n"

    
photos = Directory("Photos")


photos.pasteFile(File("summer_o1.jpg"))
photos.pasteFile(File("summer_o1.jpg"))
photos.pasteFile(File("summer_o2.jpg"))
photos.pasteFile(File("summer_o2.jpg"))
photos.pasteFile(File("summer_o3.jpg"))

photos.deleteFile(input())

print(photos)

# Отображение всех обьектов происходит в следствии добавления их в content = ""  