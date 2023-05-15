from experta import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
from PyQt5.uic.uiparser import QtCore
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import QCursor, QWindow
import requests
import json

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

disease_content = []

id_disease = ''
disease_details = '''
'''
treatments = '''

'''



G01 = 'yes'
G02 = 'yes'
G03 = 'yes'
G04 = 'yes'
G05 = 'yes'
G06 = 'yes'
G07 = 'yes'
G08 = 'yes'
G09 = 'yes'
G10 = 'yes'
G11 = 'yes'
G12 = 'yes'
G13 = 'yes'


def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()


def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
	global disease_content, id_disease, disease_details, treatments
	print("")
	id_disease = disease
	disease_details = get_details(id_disease)
	treatments = get_treatments(id_disease)
	print("")
	print("The most probable disease that you have is %s\n" %(id_disease))
	id_disease = id_disease
	disease_details = disease_details
	treatments = treatments
	print("A short description of the disease is given below :\n")
	print(disease_details+"\n")
	print("The common medications and procedures suggested by other real doctors are: \n")
	print(treatments+"\n")

	

	# disease_content.append(id_disease)
	# disease_content.append(disease_details)
	# disease_content.append(treatments)


class Greetings(KnowledgeEngine):

	@DefFacts()
	def _initial_action(self):
		print("")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(fear_worry=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(fear_worry = G01)
		
		# input("fear_worry: "))
		)
		

	@Rule(Fact(action='find_disease'), NOT(Fact(panic_attacks=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(panic_attacks = G02
		# input("panic_attacks: ")
		))
		

	@Rule(Fact(action='find_disease'), NOT(Fact(avoidance=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(avoidance = G03
		# input("chest pain: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(trembling=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(trembling = G04
		# input("trembling: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(compulsive=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(compulsive = G05
		# input("compulsive: ")
		))

		print(G05)

	@Rule(Fact(action='find_disease'), NOT(Fact(per_sadness=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(per_sadness=G06
		# input("per_sadness: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(appetite=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(appetite=G07
		# input("sunken eyes: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(interest_loss=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(interest_loss=G08
		# input("low body temperature: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(mood_swings=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(mood_swings=G09
		# input("mood_swings: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(diff_emotions=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(diff_emotions=G10
		# input("sore throat: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(dis_thinking=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(dis_thinking=G11
		# input("dis_thinking: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(reck_behavior=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(reck_behavior=G12
		# input("Nausea: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(relationships=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(relationships=G13
		# input("relationships: ")
		))

	@Rule(Fact(action='find_disease'),Fact(fear_worry="yes"),Fact(panic_attacks="yes"),Fact(avoidance="yes"),Fact(trembling="yes"),Fact(compulsive="yes"),Fact(per_sadness="no"),Fact(appetite="no"),Fact(interest_loss="no"),Fact(mood_swings="no"),Fact(diff_emotions="no"),Fact(dis_thinking="no"),Fact(reck_behavior="no"),Fact(relationships="no"))
	def disease_0(self):
		self.declare(Fact(disease="Anxiety Disorders"))

	@Rule(Fact(action='find_disease'),Fact(fear_worry="no"),Fact(panic_attacks="no"),Fact(avoidance="no"),Fact(trembling="no"),Fact(compulsive="no"),Fact(per_sadness="yes"),Fact(appetite="yes"),Fact(interest_loss="yes"),Fact(mood_swings="yes"),Fact(diff_emotions="no"),Fact(dis_thinking="no"),Fact(reck_behavior="no"),Fact(relationships="no"))
	def disease_1(self):
		self.declare(Fact(disease="Mood Disorders"))

	@Rule(Fact(action='find_disease'),Fact(fear_worry="no"),Fact(panic_attacks="no"),Fact(avoidance="no"),Fact(trembling="no"),Fact(compulsive="no"),Fact(per_sadness="no"),Fact(appetite="no"),Fact(interest_loss="no"),Fact(mood_swings="no"),Fact(diff_emotions="yes"),Fact(dis_thinking="yes"),Fact(reck_behavior="yes"),Fact(relationships="yes"))
	def disease_2(self):
		self.declare(Fact(disease="Personality disorders"))

	@Rule(Fact(action='find_disease'),Fact(fear_worry="no"),Fact(panic_attacks="no"),Fact(avoidance="yes"),Fact(trembling="yes"),Fact(compulsive="no"),Fact(per_sadness="no"),Fact(appetite="no"),Fact(interest_loss="no"),Fact(mood_swings="no"),Fact(diff_emotions="no"),Fact(dis_thinking="yes"),Fact(reck_behavior="no"),Fact(relationships="no"))
	def disease_3(self):
		self.declare(Fact(disease="Schizophrenia"))

	@Rule(Fact(action='find_disease'),Fact(fear_worry="no"),Fact(panic_attacks="no"),Fact(avoidance="yes"),Fact(trembling="yes"),Fact(compulsive="no"),Fact(per_sadness="no"),Fact(appetite="no"),Fact(interest_loss="no"),Fact(mood_swings="yes"),Fact(diff_emotions="no"),Fact(dis_thinking="no"),Fact(reck_behavior="no"),Fact(relationships="no"))
	def disease_4(self):
		self.declare(Fact(disease="Substance Use Disorders"))




	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		global disease_content,id_disease,disease_details,treatments
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		id_disease = id_disease
		disease_details = disease_details
		treatments = treatments
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("A short description of the disease is given below :\n")
		print(disease_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

		

		# disease_content.append(id_disease)
		# disease_content.append(disease_details)
		# disease_content.append(treatments)

	@Rule(Fact(action='find_disease'),
		  Fact(fear_worry=MATCH.fear_worry),
		  Fact(panic_attacks=MATCH.panic_attacks),
		  Fact(avoidance=MATCH.avoidance),
		  Fact(trembling=MATCH.trembling),
		  Fact(compulsive=MATCH.compulsive),
		  Fact(diff_emotions=MATCH.diff_emotions),
		  Fact(per_sadness=MATCH.per_sadness),
		  Fact(interest_loss=MATCH.interest_loss),
		  Fact(mood_swings=MATCH.mood_swings),
		  Fact(dis_thinking=MATCH.dis_thinking),
		  Fact(appetite=MATCH.appetite),
		  Fact(reck_behavior=MATCH.reck_behavior),
		  Fact(relationships=MATCH.relationships),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,fear_worry, panic_attacks, avoidance, trembling, compulsive, diff_emotions, per_sadness, mood_swings,interest_loss ,dis_thinking ,appetite ,reck_behavior ,relationships):
		print("\nDid not find any disease that matches your exact symptoms")
		lis = [fear_worry, panic_attacks, avoidance, trembling, compulsive, diff_emotions, per_sadness, mood_swings,interest_loss ,dis_thinking ,appetite ,reck_behavior ,relationships]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)

class HomeWindow(QMainWindow):

    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi('UI/home.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.d_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button.clicked.connect(self.close)
        # self.register_button.clicked.connect(self.go_to_register_page)
        self.d_button.clicked.connect(self.start_expert)
        self.min_butto.clicked.connect(self.showMinimized)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")



        self.show()

    def start_expert(self):

	    # print("Getting GUI data")

        object1 = Set_data(
		self.G01.text(),
		self.G02.text(),
		self.G03.text(),
		self.G04.text(),
		self.G05.text(),
		self.G06.text(),
		self.G07.text(),
		self.G08.text(),
		self.G09.text(),
		self.G10.text(),
		self.G11.text(),
		self.G12.text(),
		self.G13.text()
		)
        object1.data_transform()

        preprocess()

		
        engine = Greetings()
        engine.reset()
        engine.run()
        self.shortWind = ShortWindow()
        self.close()
        print(engine.facts)

        # self.shortWind.set_info()

		# print("Getting GUI data")
	

# class Set_data()


class Set_data():

	

	def __init__(self,G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11,G12,G13):

		

		self.G01 = G01
		self.G02 = G02
		self.G03 = G03
		self.G04 = G04
		self.G05 = G05
		self.G06 = G06
		self.G07 = G07
		self.G08 = G08
		self.G09 = G09
		self.G10 = G10
		self.G11 = G11
		self.G12 = G12
		self.G13 = G13;

		
	def data_transform(self):
		global G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11,G12,G13

		G01 = self.G01
		G02 = self.G02
		G03 = self.G03
		G04 = self.G04
		G05 = self.G05
		G06 = self.G06
		G07 = self.G07
		G08 = self.G08
		G09 = self.G09
		G10 = self.G10
		G11 = self.G11
		G12 = self.G12
		G13 = self.G13

        # print("Already Set the attributes")

class ShortWindow(QMainWindow):

    def __init__(self):
        super(ShortWindow, self).__init__()
        loadUi('UI/shorty.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.more.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button_2.clicked.connect(self.close)
     
        self.more.clicked.connect(self.start_treat)
        self.min_butto_2.clicked.connect(self.showMinimized)


        self.show()
        self.disease_id.setText(id_disease)
        self.desc.setText(disease_details)

    def start_treat(self):
        self.treaty = TreatWindow()
        self.close()

		# # disease_content.append(id_disease)
		# # disease_content.append(disease_details)
		# # disease_content.append(treatments)
        #     self.disease_id.setText(disease_content[0])
        #     self.desc.setText(disease_content[0])

class TreatWindow(QMainWindow):

    def __init__(self):
        super(TreatWindow, self).__init__()
        loadUi('UI/treat.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.end.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button_2.clicked.connect(self.close)

        self.min_butto_2.clicked.connect(self.showMinimized)

        self.end.clicked.connect(self.close)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")

        self.show()

    
        # global disease_content,id_disease,disease_details,treatments
       
        self.treat.setText(treatments)
		




def run():
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        ff = engine.facts
        print(ff)
        if input() == "no":
        	exit()




if __name__ == "__main__":
    run()
	# preprocess()
	# engine = Greetings()
	# while(1):
	# 	engine.reset()  # Prepare the engine for the execution.
	# 	engine.run()  # Run it!
	# 	print("Would you like to diagnose some other symptoms?")
	# 	if input() == "no":
	# 		exit()
	# 	print(engine.facts)
