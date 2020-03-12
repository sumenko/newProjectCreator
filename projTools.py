#coding:utf-8


class newProjectCreator:
    properties = {  "projectName" : "НовыйП", 
                    "templateDir" : ".\\", 
                    "destDir" : "00 New"
                }
    def __init__(self, name):
        self.create(name)
        pass
    def create(self, name):
        print(f"Create '{name}'")
        self.copyPaths()

        for k,v in self.properties.items():
            print(f"{k} = {v}")

    def copyPaths(self):
        # скопировать папки с файлами, попутно заменить в файлах ключевое слово на имя проекта
        # создать файл с инфо о проекте
        pass

if __name__=="__main__":
    print(createNewProject({"K": "V"}))