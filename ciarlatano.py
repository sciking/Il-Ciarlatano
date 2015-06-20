#!/usr/bin/env python
# -*- coding: utf-8 -*
nome = ""
metodo = ""
turno = 1
scelta = 0
immagine = 10
credibilita = 10
mediatico = 0
pazienti = 1
costocura = 500
sostenitori = 20
soldi = 10000
crimine = 0
politico = 0
medici = 1
simv = 0
termv = 0
attivov = 0
danespe = [-5000,-2500,-1000,0,500,1000,2500,5000,10000] #8
import os
import random
aziendelosche = ["Scafisti Tripoli Durazzo Lampedusa","Meschini Srl","Ricettazione Veneto snc","FrodeFiscale Semplice SpA","Lenocino Celere"] #5
investimenti = [1000,2000,5000,10000,25000] #4
pagamento = [1250,2200,5500,11000,28500]
trasmissioni = ["Ridens","Mi manda Rete Uno", "Reportage", "Pomeriggio Milano"]
print "Il Ciarlatano"
while nome == "":
	nome = raw_input("Inserisci il tuo nome, grazie:")
print """Benvenuto %s, il tuo obiettivo è uno in questa piccola nazione,
lo Stato di Milano:
Fare i danè. Come? Semplice, truffando l'intero paese! Corrompi, compra
e appari in TV in modo da avere sostegno. La scienza e i giudici non sono
corrompibili, ma con i tuoi guadagni potrai presto uscire di galera.
Oppure non entrarvi nemmeno.
Come vuoi chiamare il tuo metodo? :"""%(nome,)
while metodo == "":
	metodo = raw_input("Nome metodo:")
def coe():
	global turno
	global metodo
	global credibilita
	global sostenitori
	global politico
	global scelta
	global costocura
	global pazienti
	global immagine
	global simv
	global termv
	global attivov
	global soldi
	global crimine
	global medici
	global nome
	global mediatico
	global sostenitori
	poss = random.randint(1,10)
	os.system("clear")
	print "Notizie"
	if poss == 1:
		print "Un tuo medico ha trovato una parola figa per l'acqua che inietti ai bambini. Boom di richieste in TV e della cura"
		pazienti = pazienti + random.randint(3,7)
		mediatico = mediatico + 5
	if poss == 2:
		print "Ops. Inietti acido fenico al posto dell'acqua. Basta anfetamine!. Molti pazienti muoiono,e ti becchi una bella denuncia"
		pazienti = int(pazienti*0.80)
		crimine = crimine + 2
		soldi = soldi - 3500
		immagine = immagine - 4
	if poss == 3:
		print "Una specie di caprone eletto sindaco dichiara che il tuo metodo funziona. E nemmeno l'hai pagato!"
		politico = politico + 6
		sostenitori = sostenitori + 2
		pazienti = pazienti + 1
	if poss == 4:
		print "Salvo Per Favore ti ha sbufalato nelle sue conferenze assieme a Roberto Vicentino: Annunci querela, che non farai mai, ma perdi sostegno"
		sostenitori = sostenitori - 2
		mediatico = mediatico + 2
		medici = medici - 2
	if poss == 5:
		print "Il massimo esperto di costolette, da te spacciato per megaesperto di malattie, certifica il tuo metodo \n I medici ti schifano, ma il popolo bue no!"
		medici = medici - 3
		sostenitori = sostenitori + 4
		pazienti = pazienti + 1
	if poss == 6:
		print "L'ospedale di Fusello ti ammette a praticare il tuo metodo: Prezzo dimezzato ma client... ehm, pazienti raddoppiati"
		pazienti = pazienti*2
		costocura= costocura/2
	if poss == 7:
		print "Una farmaceutica si offre di aiutarti, tu accetti, per poi lamentarti del boicottaggio delle case farmaceutiche"
		soldi = soldi*1.5
	if poss == 8:
		print "Sputi in faccia ad un debunker. I complottisti apprezzano, ma la tua fedina penale no"
		sostenitori = sostenitori + 3
		crimine = crimine + 1
	if poss == 9:
		print "Un tuo amico in polizia 'trucca' la tua fedina penale"
		crimine = crimine -1
	if poss == 10:
		print "Le foto di bambini malati prese da Internet hanno impietosito i telespettatori. Soldini in arrivo!"
		pazienti = pazienti + 5
		sostenitori = sostenitori + 2
		medici = medici - 1
	raw_input("Premi invio per continuare")
	principale()
def principale():
	global turno
	global metodo
	global credibilita
	global sostenitori
	global politico
	global scelta
	global costocura
	global pazienti
	global immagine
	global simv
	global termv
	global attivov
	global soldi
	global crimine
	global medici
	global nome
	global mediatico
	global sostenitori
	os.system("clear")
	if mediatico < 0:
		mediatico = 0
	if crimine < 0:
		crimine = 0
	if crimine > 15 and politico < 10:
		print "Buongiorno Polizia, lei è in arresto per ciarlataneria. \n Vieni condannato a 3 anni per ciarlataneria"
		exit()
	if crimine > 20 and politico > 10:
		print "Polizia, le sequestro il laboratorio. \n Grazie alle tue amicizie prendi 1 anno con la condizionale. Ma soldi pochi..."
	if turno%10 == 0:
		costocura = costocura*2
	if pazienti < 0:
		pazienti = 0
	if attivov == 1:
		termv = termv - 1
		if termv == 0:
			print "Si riscuote la somma"
			attivov = 0
			soldi = soldi - simv
	if medici < -8:
		medici = -8
	if immagine < -5:
		immagine = -5
	if turno%2 == 0:
		print "Per evitare problemi paghi le tasse allo stato"
		soldi = soldi/1.15
	print "Settimana", turno
	soldi = soldi + (pazienti*costocura)
	soldi = int(soldi)
	print "Hai" ,soldi, "Ambrogi"
	print "Hai", sostenitori, "sostenitori"
	print "Credibilità:", credibilita
	print "Potere mediatico;", mediatico
	print "Sostegno medico:", medici
	print "Immagine:", immagine
	print "La tua influenza sui politici è", politico
	print "Pazienti", pazienti, "\t Costo Cura:", costocura
	pazienti = pazienti + random.randint(-3,3)
	turno = turno + 1
	print "*"*30
	print "Cosa vuoi fare?"
	print "1)Dichiarazione ai giornali\n2)Appari in TV\n3)Compra\n4)Investimenti\n5)Fare Soldi"
	scelta = int(raw_input(":"))
	if scelta == 1:
		print "Cosa vuoi dichiarare all'Indipendente di Milano?"
		print """1) Stanno boicottando il nostro metodo!
2) Lo Stato sta collaborando con il nostro metodo
3) Abbiamo curato moltissime persone, soprattutto bambini
4) Loda la medicina convenzionale
5) Scredita la medicina convenzionale
6) Parla del più e del meno"""
		giornale = int(raw_input(":"))
		print "L'Indipendente di Milano"
		if giornale == 1:
			print "%s dichiara: Ci boicottano" %(nome,)
			credibilita = credibilita - 1
			sostenitori = sostenitori + 2
			mediatico = mediatico + random.randint(-1,3)
			politico = politico + random.randint(-1,1)
		if giornale == 2:
			print "%s dichiara: Milano ci aiuta" %(nome,)
			credibilita = credibilita + 1
			sostenitori = sostenitori + 2
			politico = politico + random.randint(-1,1)
			mediatico = mediatico + random.randint(-1,2)
		if giornale == 3:
			print "%s è forse la cura per molti disturbi" %(metodo,)
			credibilita = credibilita + 1
			sostenitori = sostenitori + 3
			medici = medici - 1
			pazienti = pazienti + random.randint(1,4)
			mediatico = mediatico + random.randint(-2,2)
		if giornale == 4:
			print "%s: Gloria ai medici che aiutano, loro ci riconosceranno" %(nome,)
			credibilita = credibilita - 1
			medici = medici + 2
			sostenitori = sostenitori + 2
			mediatico = mediatico + random.randint(-1,2)
			politico = politico + random.randint(-1,3)
		if giornale == 5:
			print "%s dichiara: Medici cricca contro le vere cure" %(nome,)
			credibilita = credibilita - 3
			sostenitori = sostenitori + 5
			politico = politico + random.randint(-4,1)
			medici = medici - random.randint(1,4)
			mediatico = mediatico + random.randint(-1,2)
		if giornale == 6:
			print "%s ci parla di lavoro a maglia" %(nome,)
			credibilita = credibilita + random.randint(-2,2)
			sostenitori = sostenitori + random.randint(-2,2)
			mediatico = mediatico + random.randint(-1,2)
		raw_input("Premi invio per continuare")
		coe()
	if scelta == 2:
		if mediatico < 11:
			print "Fino al livello mediatico 10 potrai apparire solo su TV locali"
			credibilita = credibilita + random.randint(-2,4)
			sostenitori = sostenitori + random.randint(-2,3)
			raw_input("Premi invio per continuare")
			coe()
		else:
			print "Appari a", trasmissioni[random.randint(0,3)], "dove parli della tua storia"
			if random.randint(1,10) > 7:
				print "Nessuno ti ha creduto"
				credibilita = credibilita - 4
				sostenitori = sostenitori - 4
				politico = politico - 2
				medici = medici - 3
				mediatico = mediatico - 1
			else:
				print "Hai avuto un buon riscontro"
				credibilita = credibilita + 4
				sostenitori = sostenitori + 4
				politico = politico + random.randint(-1,3)
				medici = medici + random.randint(1,3)
				mediatico = mediatico + random.randint(-1,4)
			raw_input("Premi invio per continuare")
			coe()
	if scelta == 3:
		print "Scrivi 1 per comperare un medico (3000), 2 per sostenitori (5000), 3 per giornalista (7500) e 4 per politici (10000)"	
		cesta = int(raw_input(":"))
		if cesta == 1:
			medici = medici + 1
			soldi = soldi  - 3000
		if cesta == 2:
			sostenitori = sostenitori + random.randint(1,3)
			mediatico = mediatico + 1
			soldi = soldi - 5000
		if cesta == 4:
			soldi = soldi - 10000
			politico = politico + random.randint(-1,4)
		if cesta == 3:
			soldi = soldi - 7500
			mediatico = mediatico + 4
		if random.randint(1,7) > 5:
			print "Operazione finita male, no problemi con la legge, ma perdiamo immagine"
			credibilita = credibilita - 3
			immagine = immagine -3
			crimine = crimine + 1
		else:
			print "Operazione andata a buon fine"
		raw_input("Premi invio per continuare")
		coe()
	if scelta == 4:
		print "Investimenti"
		if attivov == 1:
			print "Non puoi fare altri investimenti!"
			raw_input("premi invio per continuare")
			coe()
		inve = random.randint(0,4)
		settimane = random.randint(4,12)
		print "La società", aziendelosche[random.randint(0,4)],"ti offre", investimenti[inve], "a patto di restituire con interessi dopo", settimane, "settimane"
		accettazione = raw_input("Scrivi si per accettare:")
		if accettazione == "si":
			simv = pagamento[inve]
			termv = settimane
			soldi = soldi + investimenti[inve]
			attivov = 1
		coe()
	if scelta == 5:
		k = danespe[random.randint(4,8)]
		print "Fai una ospitata televisiva e guadagni", k
		soldi = soldi + k
		raw_input("premi invio per continuare")
		pazienti = pazienti + random.randint(0,1)
		coe()
	coe()
principale()
