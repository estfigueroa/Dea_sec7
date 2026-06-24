usuarios_list = []

#--------- validaciones -------------
def validar_sexo(sexo):
    if sexo in ["M", "F"]:
        return True
    else:
        print("ERROR es valido F o M")
        return False

def validar_password(password):
    if len (password.strip())>8:
        print("ERROR, minimo 8 caracteres")
        return False
    
    tiene_numero = False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True
    
    tiene_letra = False
    for letra in password:
        if letra.isalpha():
            tiene_letra = True

    if " " in password:
        print("ERROR, no puede estar vacio")
        return False

def imprimir_usuario(usuario):
    print(f"""
        ---------------------------------
        Nombre usuario: {usuario["nombre_usuario"]}
        Sexo: {usuario["sexo"]}
        Password: {usuario["password"]}
        """)

#---------- transacciones --------------
def agregar_usuario():
    pass
def eliminar_usuario():
    pass
def buscar_usuario():
    pass