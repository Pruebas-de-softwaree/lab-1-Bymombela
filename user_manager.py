import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()
    for i in range(100):
        user_manager.add_user(i,f"Yo soy el num : {i}")
    print("end")
    # for i in range (100):
    #     print(user_manager.find_user(i))

    # for i in range (500):
    #     user_manager.delete_user(i)
    #     print("El usuario fue eliminado:",i)

    # nombre = user_manager.get_all_names()
    # print(f"{nombre}")

    # promedio = user_manager.average_user_id()
    # print ("El promedio es",promedio)

    # for i in range (1000):
    #     user_manager.add_user (i, f"Soy el usuario agregado numero:{i}")
    # print (user_manager.get_all_names())

    # start = time.time()
    # user_manager.find_user(100)
    # end = time.time()
    # print("Duracion ",end-start," segundos")


    duplicados = []
    user_manager.add_user(1,"lol")
    for i in user_manager.get_all_names():
        if user_manager.get_all_names().count(i) > 1 and i not in duplicados:
            duplicados.append(i)

    print("Duplicados:", duplicados)
    # → Duplicados: [1, 2]

