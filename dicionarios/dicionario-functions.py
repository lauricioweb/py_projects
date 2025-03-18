user = {
    "nome":"maria",
    "idade":22,
    "email":"maria@gmail.com"
}


def showUser(user):
    for key, value in user.items():
        # title() serve para deixar a primeira letra maiuscula
        print(f"{key.title()} : {value}")

showUser(user)


# retornando dicionarios de funçõeos


def create_user(name,age,email):
    return {
        "name":name,
        "age":age,
        "email":email
    }

print(create_user("mariana", 25,"anamari@gmail.com"))
