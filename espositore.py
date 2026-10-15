class Espositore:
    def __init__(self,codice,nome,cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        self._stand_assegnatogli = None
    @property
    def stand_assegnatogli(self):
        return self._stand_assegnatogli
    @stand_assegnatogli.setter
    def stand_assegnatogli(self,stand):
        if self._stand_assegnatogli == None:
            self._stand_assegnatogli = stand
        else:
            print(f"{self.__codice} assegnato a {self._stand_assegnatogli}")

    @property
    def codice(self):
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome
