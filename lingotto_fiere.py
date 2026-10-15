import stand
import espositore
from csv import reader
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.lista_stand = []
        self.lista_espositori = []
    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            with open(file_path, "r") as f:
                file = reader(f)
                for row in file:
                    if len(row)<4:
                        codice_espositore,nome,cognome = row
                        e = espositore.Espositore(codice_espositore,nome,cognome)
                        self.lista_espositori.append(e)
                    elif len(row) == 4:
                        codice_stand, superficie, padiglione, prezzo_base = row
                        prezzo_base = float(prezzo_base)
                        s = stand.Stand(codice_stand,superficie,padiglione,prezzo_base)
                        self.lista_stand.append(s)
                    else:
                        if len(row) == 5:
                            coice_stand, superficie, padiglione, prezzo,valore = row
                            prezzo = float(prezzo)
                            s = stand.Stand_p(coice_stand,superficie,padiglione,prezzo,valore)
                            self.lista_stand.append(s)
                        else:
                            raise self.lista_stand.append("Errore")
        except FileNotFoundError:
            return FileNotFoundError

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        for i in self.lista_stand:
            if i.codice==codice_stand:
                oggetto_stand = i
                break

        for j in self.lista_espositori:
            if j.codice==codice_espositore:
                oggetto_espositore = j
                break

        if oggetto_stand and oggetto_espositore:
            oggetto_stand.espositore1 = codice_espositore
            oggetto_espositore.stand_assegnatogli = oggetto_stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for oggetto in self.lista_espositori:
            print(oggetto.codice,oggetto.nome,oggetto.cognome,oggetto.stand_assegnatogli)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        self.lista_stand.sort()
        return self.lista_stand