class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self._prezzo_base = prezzo_base
        self.__espositore = None

    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self,codice):
        if self.__espositore == None:
            self.__espositore = codice

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo_base(self):
        return self._prezzo_base

    def __lt__(self, altro_stand):
        return self._prezzo_base < altro_stand.prezzo_base
    def __str__(self):
        return f"{self.codice} - {self.superficie} - {self.padiglione} - {self.prezzo_base}"
class Stand_p(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, prezzo_aggiuntivo):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prezzo_base = prezzo_aggiuntivo

    @property
    def prezzo_base(self):
        return self._prezzo_base

    @prezzo_base.setter
    def prezzo_base(self, value):
        try:
            self._prezzo_base = self._prezzo_base * (1 + 0.07 * float(value))
        except ValueError:
            self._prezzo_base = self._prezzo_base * 1.30

    def __lt__(self, altro_stand):
        return self._prezzo_base < altro_stand.prezzo_base

    def __str__(self):
        return f"{self.codice} - {self.superficie} - {self.padiglione} - {self.prezzo_base}"