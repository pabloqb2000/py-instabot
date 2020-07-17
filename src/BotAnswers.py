from instaBot import *

class Reaction:
    def __init__(self, msg, action):
        self.msg = msg
        self.action = action
    
    # Checks if the msg this reaction belongs to is inside the given msg
    # if so triggers the action
    def react(self, msg, account):
        if(self.msg.upper() in msg.upper()):
            print("-> @" + account + " " + self.msg)
            self.action(msg, account)
            return True

class Reactor:
    # Create the list of reactions
    def __init__(self, bot, admin):
        self.bot = bot
        self.reactions = [
            Reaction("hola", self.sayHi),
            Reaction("ayuda", self.sendHelp),
            Reaction("admin", self.sendToAdmin),
            Reaction("sigueme", self.followMe),
            Reaction("fekas", self.sendFekas),
            Reaction("creepies", self.sendCreepies),
        ]
        self.admin = admin


    # Reacts to a given msg
    def process(self, msg, account):
        answ = [r.react(msg, account) for r in self.reactions]
        if not any(answ):
            print("-> @" + account + " fallo: " + msg)
            self.sendNoAnsw(msg, account)


    # Says hi back to the user
    def sayHi(self, msg, account):
        self.bot.sendMsg("Hola " + account + ' escribe "ayuda" para conocer el resto de funciones')

    # Send help messages
    def sendHelp(self, msg, account):
        self.bot.sendMsg('Escribe "Admin [mensaje]" y cambia [mensaje] por el mensaje que le quieras enviar al admin (' + self.admin + ').')
        self.bot.sendMsg('Escribe "Sigueme" para mandarte una solicitud y que asi puedas usar las demas funciones.')
        self.bot.sendMsg('Escribe "Fekas" para ver la lista de fekas a los que sigues pero ellos no te siguen a ti.')
        self.bot.sendMsg('Escribe "Creepies" para ver la lista de gente que te sigue pero ni lo sabes xq no les sigues tu a ellos.')
    
    # Follow the account who send the message
    def followMe(self, msg, account):
        self.bot.sendMsg("Vale, ahora le doy a seguir, si eres privad@ aceptame, sino solo espera")
        self.bot.sendMsg("Es posible que una vez me aceptes tengas que esperar un poco hasta poder usar las otras funciones")
        self.bot.followAccount(account)
    
    # Send message to admin
    def sendToAdmin(self, msg, account):
        self.bot.sendMsg("Okay, ahora me pongo en contacto con el admin")
        self.bot.openChat(self.admin)
        self.bot.sendMsg("@" + account + ": " + msg)
    
    # Send fekas list
    def sendFekas(self, msg, account):
        if account in self.bot.following:
            self.bot.sendMsg("Ahora te mando la lista, dame un momento, esto podria tardar unos minutos")
            fekas = self.bot.getFekasOf(account)
            self.bot.chatMenu()
            self.bot.openChat(account)
            self.bot.sendMsg("-Fekas:")
            for f in fekas:
                self.bot.sendMsg("@" + f)
        else:
            self.bot.sendMsg("Todavia no te sigo, necesito seguirte para poder darte esa informacion")
            self.bot.sendMsg('Escribe "Sigueme" para que empieze a seguirte y asi puedas usar esta funcion')
            self.bot.sendMsg("Si ya me has aceptado la solicitud puede que tengas que esperar un poco y volver a mandar el mensaje")

    # Send creepies list
    def sendCreepies(self, msg, account):
        if account in self.bot.following:
            self.bot.sendMsg("Ahora te mando la lista, dame un momento, esto podria tardar unos minutos")
            creepies = self.bot.getCreepiesOf(account)
            self.bot.chatMenu()
            self.bot.openChat(account)
            self.bot.sendMsg("-Creepies:")
            for c in creepies:
                self.bot.sendMsg("@" + c)
        else:
            self.bot.sendMsg("Todavia no te sigo, necesito seguirte para poder darte esa informacion")
            self.bot.sendMsg('Escribe "Sigueme" para que empieze a seguirte y asi puedas usar esta funcion')
            self.bot.sendMsg("Si ya me has aceptado la solicitud puede que tengas que esperar un poco y volver a mandar el mensaje")

    # Send this messages if no answer is found
    def sendNoAnsw(self, msg, account):
        self.bot.sendMsg("Lo siento " + account + " pero no tengo respuesta para eso :(")
        self.bot.sendMsg('Prueba a escribir "ayuda" para conocer el resto de funciones')
