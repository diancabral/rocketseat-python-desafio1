# Rocket Agenda
# Dian Carlos <dian.cabral@gmail.com>

from utils import drawBox

options = [
  "Lista de Contatos",
  "Lista de Favoritos",
  "Adicionar um contato",
  "Editar um contato", # aqui marca como favorito
  "Apagar um contato",
  "Sair"
]

phoneBook = []

def checkPhoneBook(func):
  def wrapper(*args, **kwargs):
    if len(phoneBook) == 0:
      print("❌ Você não tem nenhum contato em sua agenda 😭")
      print(f"ℹ️  Primeiro, escolha a opção 3 para adicionar um novo contato 😉\n")
    else:
      func(*args, **kwargs)
  return wrapper

def getUserContactAction(func):
  def wrapper():
    showBookList()
    try:
      userInput = input("\n⌨️  Digite o índice do usuário -> ")
      index = int(userInput)
      if index > 0 and index <= len(phoneBook):
        indexTransformed = index - 1
        name = phoneBook[indexTransformed].get('name')

        print(f"\n✅ Você escolheu o usuário nº{index} -> {name}\n")

        func(indexTransformed=indexTransformed, name=name)
      else:
        raise Exception
    except Exception as error:
        print(error)
        print(f"\n❌ A opção {userInput} é inválida. Tente novamente!\n")

  return wrapper

@checkPhoneBook
def showBookList(favorites = False):
  getList = phoneBook if favorites == False else list(filter(lambda contact: contact.get("favorite") == True, phoneBook))
  if len(getList) == 0 and favorites:
    print("❌ Você não tem nenhum contato favorito em sua agenda 😭")
    print(f"ℹ️  Primeiro, escolha a opção 4 para editar um contato como favorito 😉\n")
  if len(getList):
    for index, contact in enumerate(getList, start=1):
      name = contact["name"]
      drawBox([
        f"┌--------┐",
        f"|        | Contato #{str(index)}",
        f"|        |",
        f"|        | {'⭐️ ' if contact['favorite'] else ''}{contact['name']}",
        f"|        | {contact['phone']} - {contact['email']}",
        f"└--------┘"
      ], center=False, paddingY=False)

def handleContact(mode="add", indexTransformed=0):
  isEdit = False if mode == "add" else True
  newLabel = 'novo ' if isEdit else ''

  if isEdit:
    print("ℹ️  Deixe o campo em branco para manter o valor original!\n")

  name = input(f"👽 Digite o {newLabel}nome: ")
  phone = input(f"☎️ Digite o {newLabel}número de telefone [(00) 0000-0000]: ")
  email = input(f"📨 Digite o {newLabel}e-mail [email@dominio.com]: ")
  favorite = input("⭐️ Deseja marcar como favorito? [S = SIM, N = NÃO]: ")

  if favorite != '' and favorite.lower() not in ("s", "n"):
    print("\n❌ Opção de favorito inválida. Definido como padrão NÃO")

  if isEdit:
    print()

  isFavorite = True if favorite.lower() == "s" else False

  if isEdit == False:
    phoneBook.append( {
      "name": name,
      "phone": phone,
      "email": email,
      "favorite": isFavorite
    })
    print(f"\n✅ O contato \"{name}\" foi adicionado com sucesso em sua agenda!\n")
  else:
    if name == '' and phone == '' and email == '' and favorite == '':
      print(f"⭕️  Nenhum campo alterado. Operação cancelada!\n")
    else:
      drawBox(["Revise sua edição"])

      oldData = phoneBook[indexTransformed]

      newName = oldData.get("name") if name == '' else name
      newPhone = oldData.get("phone") if phone == '' else phone
      newEmail = oldData.get("email") if email == '' else email
      newFavorite = oldData.get("favorite") if favorite == '' else isFavorite

      print(f"[Nome] {oldData.get('name')} -> {newName}")
      print(f"[Telefone] {oldData.get('phone')} -> {newPhone}")
      print(f"[E-mail] {oldData.get('email')} -> {newEmail}")
      print(f"[Favorito] {('Sim' if oldData.get('favorite') else 'Não')} -> {('Sim' if newFavorite else 'Não')}\n")

      userAnswer = input("⁉️  Você realmente deseja editar esse usuário? [S = SIM, N = NÃO]: ")

      if userAnswer.lower() not in ("s", "n"):
        print("\n❌ Opção de edição inválida. Tente novamente!\n")
      else:
        sholdEdit = True if userAnswer.lower() == "s" else False

        if sholdEdit:
          phoneBook[indexTransformed] = {
            "name": newName,
            "phone": newPhone,
            "email": newEmail,
            "favorite": newFavorite
          }
          print(f"\n✅ O contato \"{newName}\" foi editado com sucesso!\n")
        else:
          print(f"\n⭕️  Operação cancelada!\n")

@checkPhoneBook
@getUserContactAction
def handleContactEdit(indexTransformed, name):
  handleContact(mode="edit", indexTransformed=indexTransformed)

@checkPhoneBook
@getUserContactAction
def deleteContact(indexTransformed, name):
  userAnswer = input("⁉️  Você realmente deseja excluir esse usuário? [S = SIM, N = NÃO]: ")

  if userAnswer.lower() not in ("s", "n"):
    print("\n❌ Opção de exclusão inválida. Tente novamente!\n")
  else:
    shouldDelete = True if userAnswer.lower() == "s" else False

    if shouldDelete:
      del phoneBook[indexTransformed]
      print(f"\n✅ O contato \"{name}\" foi excluído com sucesso em sua agenda!\n")
    else:
      print(f"\n⭕️  Operação cancelada!\n")

@checkPhoneBook
@getUserContactAction
def editContact(indexTransformed, name):
  userAnswer = input("⁉️  Você realmente deseja excluir esse usuário? [S = SIM, N = NÃO]: ")

  if userAnswer.lower() not in ("s", "n"):
    print("\n❌ Opção de exclusão inválida. Tente novamente!\n")
  else:
    shouldDelete = True if userAnswer.lower() == "s" else False

    if shouldDelete:
      del phoneBook[indexTransformed]
      print(f"\n✅ O contato \"{name}\" foi editado com sucesso em sua agenda!\n")
    else:
      print(f"\n⭕️  Operação cancelada!\n")

def showOptions():
  print("-\n")
  for index, value in enumerate(options):
    optionNumber = index + 1
    print(f"{optionNumber}. {value}")
  print("\n-")

def getUserOptionInput():
  try:
    userInput = input("\n⌨️  Digite sua opção -> ")
    index = int(userInput)
    if index > 0 and index <= len(options):
      indexTransformed = index - 1
      print(f"\n✅ Você escolheu a opção nº{index} -> {options[indexTransformed]}\n")
      return index
    else:
      raise Exception
  except Exception:
      print(f"\n❌ A opção {userInput} é inválida. Tente novamente!\n")

def handleOption(index):
  if index == 1:
    drawBox(["Seus contatos"])
    showBookList()
  elif index == 2:
    drawBox(["Seus Favoritos"])
    showBookList(favorites=True)
  elif index == 3:
    drawBox(["Criar novo contato"])
    handleContact()
  elif index == 4:
    drawBox(["Editar contato"])
    handleContactEdit()
  elif index == 5:
    drawBox(["Apagar contato"])
    deleteContact()
  elif index == 6:
    return False
  else:
    return True

###

drawBox(["RocketSeat", "", "Boas vindas à RocketAgenda", "Para começar, escolha uma opção abaixo"])

while True:
  showOptions()
  option = getUserOptionInput()

  if handleOption(option) == False:
    drawBox(["Obrigado por utilizar a RocketAgenda!",  "Nos vemos em breve :)"])
    break
