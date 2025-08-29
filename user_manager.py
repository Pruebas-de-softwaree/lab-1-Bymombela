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
    # for i in range(100):
    #     user_manager.add_user(i,f"Yo soy el num : {i}")
    # print("end")
    # for i in range (100):
    #     print(user_manager.find_user(i))

    # for i in range (500):
    #     user_manager.delete_user(i)
    #     print("El usuario fue eliminado:",i)

    # nombre = user_manager.get_all_names()
    # print(f"{nombre}")

    # promedio = user_manager.average_user_id()
    # print ("El promedio es",promedio)

    for i in range (1000):
        user_manager.add_user (i, f"Soy el usuario agregado numero:{i}")
    print (user_manager.get_all_names())


