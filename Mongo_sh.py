from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://A-WWW:32125M32125@cluster0.0b6py.mongodb.net/School?retryWrites=true&w=majority")
db = cluster["School"]
collection = db["Class"]
collection_1 = db["Student"]


class School:

    def __init__(self, citi='Kiev', number=268):
        self.citi = citi
        self.number = number

    # добавляет классы в школу
    def class_x(self, number_c):
        self.number_c = number_c
        class_x = {'_id': self.number_c, 'School number ': self.number, 'citi': self.citi,
                   'class number': self.number_c}

        if len(list(collection.find({'class number': self.number_c}))) == 0:
            collection.insert_one(class_x)
        else:
            print("Класс с таким номером уже существует")

    # запрос выводит общий список существующих классов в школе
    def Sch_clas(self):
        print("Школа №", self.number)
        for i in list(collection.find({})):
            print("Класс", i["class number"])

    # связь идет через прямые ссылки, можно DBRef но руководство и ресурсы рекомендуют,
    # что если не больше одной ссылки то лучшге напрямую
    def student(self, first_name, last_name, age, telephone, class_1):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.telephone = telephone
        self.class_1 = class_1
        if len(self.telephone) != 10:
            return print("Проверте правильность введённого` телефонного номера")
        if len(list(collection_1.find({"Телефон": self.telephone}))) != 0:
            return print('этот ученик уже внесен в базу данных школы')
        if len(list(collection.find({'class number': self.class_1}))) == 0:
            return print("Класса с таким номером в школе №", self.number,
                         "не зарегистрированно, проверьте правильность указанных данные")
        else:
            g = list(collection.find({'class number': self.class_1}))
            student_x = {"Фамилия": self.last_name, "Имя": self.first_name, "Возраст": self.age,
                         "Телефон": self.telephone,
                         "Класс": {"_id": self.class_1}}
            collection_1.insert_one(student_x)

        # запрос поиск по номеру телефона (по фамилии не делалал, но он будет практически идентичен по структуре)

    def fon(self, fon_nab):
        self.fon_nab = fon_nab
        if len(self.fon_nab) != 10:
            return print("Проверте правильность введённого` телефонного номера")
        if len(list(collection_1.find({"Телефон": self.fon_nab}))) == 0:
            return print('Ученик с таким ноmером телефона отсутсвует в базе данных школы')
        else:
            r = list(collection_1.find({'Телефон': self.fon_nab}))
            print(list(collection_1.find({'Телефон': self.fon_nab}, {'_id': 0, 'Класс': 0})))
            print(list(collection.find(r[0]['Класс'], {'_id': 0})))

    # удаление записи о ученике
    def delete(self, name):
        self.name = name
        collection_1.delete_one({"Фамилия": self.name})
        if len(list(collection_1.find({"Фамилия": self.name}))) == 0:
            print("Запись о ученике", self.name, "удалена из базы данных школы ")
        else:
            print("Что - то пошло не так")


# все возможные варианы запросов, обнавления полей не переберал, вариантов доствочно много , ограничелся только тем что пришло на ум


test = School()
# test.class_x('2a')
# test.Sch_clas()
# test.test("1a")
test.fon('0000222221')
# test.delete('Ivanov16')
Vova = School()

print('В колекции классы находится', collection.count_documents({}), "документа")
print('В колекции ученики находится', collection_1.count_documents({}), "документа")

# for i in list(collection.find({})):
#       print(i)
# for i in list(collection_1.find({},{'_id': 0})):
#        print(i)
# collection_1.delete_many({})
# collection.delete_many({})

