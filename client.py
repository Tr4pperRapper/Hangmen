#All of necessary data exists in this one file. If you want to read the code with more clarity then just minimize the dictionairy topicswords. I did this because I didn't want to include other files
#The multiplayer feature is seriously coming out 1st of April I just need to figure out one issue and the rest are already there

import json
import os
import random
import socket
import select
import sys
import threading



#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#IP_address = "localhost"
#Port = 8888
#server.connect((IP_address, Port))
active = 0

firstTime = 1
started = 0
topic = 5
difficulty = 2
topics = ["Computer Science", "Physics", "Chemistry", "Biology", "General"]
topicswords = {
  "Computer Science": [
    "algorithms", "programming", "data structures", "software engineering",
    "operating systems", "artificial intelligence", "computer networks",
    "cybersecurity", "machine learning", "web development",
    "database management", "parallel computing", "cryptography",
    "information theory", "computer graphics", "image processing",
    "computer vision", "natural language processing", "programming languages",
    "computer architecture", "computer organization", "data compression",
    "data encryption", "distributed systems", "file systems",
    "human-computer interaction", "multi-agent systems",
    "operating system design", "real-time systems", "robotics",
    "security engineering", "signal processing", "virtual reality",
    "cloud computing", "network security", "web design",
    "mobile application development", "cybercrime", "digital forensics",
    "algorithmic game theory", "formal methods", "graph theory",
    "computational geometry", "bioinformatics", "neural networks",
    "genetic algorithms", "fuzzy logic", "expert systems", "decision trees",
    "machine vision", "intelligent agents", "semantic web",
    "information retrieval", "speech recognition", "image recognition",
    "database systems", "big data", "data mining", "knowledge representation",
    "logic programming", "software testing", "usability engineering",
    "design patterns", "agile software development",
    "object-oriented programming", "functional programming",
    "aspect-oriented programming", "service-oriented architecture",
    "client-server computing", "grid computing", "high-performance computing",
    "distributed computing", "peer-to-peer computing", "concurrent computing",
    "real-time computing", "embedded systems", "computer vision"
  ],
  "Physics": [
    "mechanics", "thermodynamics", "electromagnetism", "optics", "waves",
    "quantum mechanics", "relativity", "astrophysics", "nuclear physics",
    "particle physics", "atomic physics", "condensed matter physics",
    "solid state physics", "plasma physics", "statistical mechanics",
    "cosmology", "gravitation", "black holes", "string theory",
    "supersymmetry", "quantum field theory", "molecular physics", "biophysics",
    "materials science", "acoustics", "fluid mechanics", "geophysics",
    "mechanical engineering", "electrical engineering", "civil engineering",
    "chemical engineering", "biomedical engineering", "systems engineering",
    "astronomy", "astrophotography", "optical astronomy", "radio astronomy",
    "observational astronomy", "celestial mechanics", "space physics",
    "theoretical physics", "experimental physics", "applied physics",
    "mathematical physics", "classical mechanics", "quantum optics",
    "atomic spectroscopy", "neutron scattering", "x-ray diffraction",
    "quantum computing", "information theory", "energy storage",
    "semiconductor physics", "optoelectronics", "nanotechnology",
    "energy conversion", "fusion power", "laser physics",
    "high energy physics", "medical physics", "environmental physics",
    "neurophysics", "time crystals", "spintronics", "quantum materials",
    "optical tweezers", "quantum sensing", "spin qubits",
    "optical coherence tomography", "quantum communication"
  ],
  "Chemistry": [
    "atomic structure", "chemical bonding", "stoichiometry", "thermochemistry",
    "electrochemistry", "acid-base chemistry", "organic chemistry",
    "inorganic chemistry", "analytical chemistry", "biochemistry",
    "physical chemistry", "quantum chemistry", "molecular biology",
    "spectroscopy", "photochemistry", "polymer chemistry", "colloid chemistry",
    "supramolecular chemistry", "material chemistry", "geochemistry",
    "atmospheric chemistry", "environmental chemistry", "forensic chemistry",
    "pharmaceutical chemistry", "green chemistry", "food chemistry",
    "surface chemistry", "petrochemistry", "industrial chemistry",
    "coordination chemistry", "medicinal chemistry", "synthetic chemistry",
    "crystallography", "solid-state chemistry", "thermodynamics", "catalysis",
    "biomaterials", "nanomaterials", "crystal engineering", "microfluidics",
    "lab-on-a-chip", "membrane technology", "supercritical fluids",
    "electrolysis", "chromatography", "mass spectrometry", "NMR spectroscopy",
    "IR spectroscopy", "UV-Vis spectroscopy", "fluorescence spectroscopy",
    "Raman spectroscopy", "X-ray crystallography", "titration",
    "gravimetric analysis", "spectrophotometry",
    "atomic absorption spectroscopy", "gas chromatography",
    "liquid chromatography", "paper chromatography",
    "ion exchange chromatography", "size exclusion chromatography",
    "electrophoresis", "NMR imaging", "polarimetry", "electrogravimetry",
    "potentiometry", "amperometry", "conductometry", "viscometry", "osmometry",
    "calorimetry", "coulometry", "chemical kinetics", "photoelectrochemistry",
    "quantum dots", "surface-enhanced Raman spectroscopy",
    "computational chemistry", "metabolomics", "bioanalytical chemistry",
    "cheminformatics", "heterogeneous catalysis", "homogeneous catalysis",
    "zeolites", "solvothermal synthesis", "nanoparticles", "micelles",
    "emulsions", "colloids", "zeolites", "desalination", "water purification",
    "wastewater treatment", "air pollution", "soil chemistry",
    "pesticide chemistry", "chemical thermodynamics", "bioinorganic chemistry",
    "bioorganic chemistry", "green synthesis", "glycochemistry",
    "organometallic chemistry", "radiochemistry", "actinide chemistry",
    "lanthanide chemistry", "petrochemicals", "aromatic chemistry",
    "aliphatic chemistry", "inorganic synthesis", "physical organic chemistry",
    "asymmetric synthesis", "enantioselective catalysis",
    "metal-organic frameworks", "pharmaceutical analysis", "toxicology",
    "pharmacokinetics", "pharmacodynamics", "drug design", "drug delivery",
    "molecular modeling", "protein chemistry", "enzymology",
    "carbohydrate chemistry", "lipid chemistry", "natural products chemistry",
    "food analysis", "food additives", "flavor chemistry",
    "fragrance chemistry", "cosmetics chemistry", "dye chemistry",
    "pigment chemistry", "ink chemistry", "coatings chemistry",
    "lubricant chemistry", "textile chemistry", "paper chemistry",
    "agrochemistry"
  ],
  "Biology": [
    "synthetic biology", "metagenomics", "structural biology", "phylogenetics",
    "epigenetics", "microbial ecology", "genetic engineering", "gene therapy",
    "stem cell research", "cancer biology", "neurobiology",
    "behavioral genetics", "population genetics",
    "evolutionary developmental biology", "computational biology",
    "immunotherapy", "biological imaging", "biological control",
    "biological invasion", "biomarkers", "biological rhythms",
    "bioluminescence", "bioreactors", "biogeochemistry", "biogeography",
    "biological oceanography", "biological wastewater treatment",
    "biological nitrogen removal", "biological phosphorus removal",
    "biological hydrogen production", "biological desulfurization",
    "biological denitrification", "biological nutrient removal",
    "biological waste gas treatment", "biological soil improvement",
    "biological pest control", "biological weed control",
    "biological fertilizer", "biological insecticide", "biological herbicide",
    "biological fungicide", "biological nematicide", "biological pesticide",
    "biological insect repellent", "biological molluscicide",
    "biological miticide", "biological virucide", "biological antimicrobial",
    "biological disinfectant", "biological sanitizer",
    "biological preservative", "biological control agent",
    "biological additive", "biological product", "biological soil amendment",
    "biological filter", "biological reactor", "biological detoxification",
    "biological remediation", "biological restoration", "biological diversity",
    "biological monitoring", "biological assessment", "biological evaluation",
    "biological risk assessment", "biological assay", "biological marker",
    "biological response modifier", "biological specimen",
    "biological conservation", "biological restoration",
    "biological management", "biological survey",
    "biological impact assessment", "biological indicator",
    "biological reserve", "biological hotspot", "biological corridor",
    "biological invasion assessment", "biological resource management",
    "biological sampling", "biological census", "biological modeling",
    "biological forecasting", "biological planning",
    "biological risk management", "biological emergency response",
    "biological threat assessment", "biological security", "biological safety"
  ],
  "General": [
    "CAS", "Extended Essay", "Theory of Knowledge", "Internal Assessment",
    "External Assessment", "IB Diploma Programme", "IB Learner Profile",
    "Global Contexts", "Approaches to Learning", "Subject Guides",
    "Assessment Criteria", "Criterion-Referenced Assessment",
    "Holistic Assessment", "Summative Assessment", "Formative Assessment",
    "Higher Level", "Standard Level", "Core", "Elective", "Option",
    "Bilingual Diploma", "IBCC", "Recognition Policy", "Grade Boundaries",
    "Academic Honesty", "Plagiarism", "Collaborative Learning",
    "International Mindedness", "Interdisciplinary Learning",
    "Inquiry-Based Learning", "Student-Centered Learning",
    "Teacher Support Material", "Transdisciplinary Skills", "Personal Project"
  ]
}
difficulties = ["Too easy", "Easy", "Medium", "Hard", "Maou too easy"]
answerfield = ""
falseletters = []
word = ""
data = {"username": "Guest", "singleplayer": {"wins": 0, "loses": 0}}

#Server variables
messages = []
members = -1

#Clear function
def clear():
  #Windows
  if os.name == 'nt':
    _ = os.system('cls')
  #Unix
  else:
    _ = os.system('clear')


#Check user local data
if os.path.exists("local.txt"):
  file = open("local.txt", "r+")
  for line in file.readlines():
    data["username"] = line.split()[0]
    data["singleplayer"]["wins"] = int(line.split()[1])
    data["singleplayer"]["loses"] = int(line.split()[2])
  firstTime = 0
else:
  open("local.txt", "w").close()
  file = open("local.txt", "r+")


def save_data():
  global data
  file.seek(0)
  file.truncate(0)
  file.write(data["username"])
  file.write(" ")
  file.write(str(data["singleplayer"]["wins"]))
  file.write(" ")
  file.write(str(data["singleplayer"]["loses"]))


def end_game_menu(cond):
  clear()
  print("The hangmen - Game End\n")
  global word
  if cond == 0:
    print("You lost :(")
    print("\nThe word was:", word)
    print("Its okay better luck next time!")
    print("\nMenu")
    print("1. Play again")
    print("2. Back to settings")
    print("3. Back to menu")
    ans = input()
    if ans == "1":
      start_game("local", 0)
    elif ans == "2":
      singleplayer_menu()
    elif ans == "3":
      menu()
    else:
      print("Invalid option\n")
      end_game_menu(0)
  if cond == 1:
    print("GGs")
    print("\nYou found the word", word, "succesfully.")
    print("Next time find it faster if you can!")
    print("\nMenu")
    print("1. Play again")
    print("2. Back to settings")
    print("3. Back to menu")
    ans = input()
    if ans == "1":
      start_game("local", 0)
    elif ans == "2":
      singleplayer_menu()
    elif ans == "3":
      menu()
    else:
      print("Invalid option\n")
      end_game_menu(1)


#Pick a word from list
def pick_word():
  global word, topics, topic, topicswords
  word = random.choice(topicswords[topics[topic - 1]])
  word = word.lower()


#Initiate game variables
def init_game_vars():
  global word, score, answerfield, started, falseletters
  started = 1
  pick_word()
  score = 0
  falseletters = []
  answerfield = ""
  for idx, i in enumerate(word):
    if i.isspace():
      answerfield = answerfield[:idx] + " " + answerfield[idx + 1:]
    elif i == "-" or i == "." or i == "," or i == ":" or i == ";":
      answerfield = answerfield[:idx] + i + answerfield[idx + 1:]
    else:
      answerfield = answerfield[:idx] + "_" + answerfield[idx + 1:]


#Is letter included in the word?
def letter_check(letter):
  global word, score, answerfield, falseletters
  flag = 0

  for idx, i in enumerate(word):
    if letter == i:
      if flag == 0:
        flag = 1
      answerfield = answerfield[:idx] + i + answerfield[idx + 1:]

  for i in falseletters:
    if i == letter:
      flag = 2

  if flag == 0:
    score = score + 1
    falseletters.append(letter)
  return flag


#Hangman template
def hangman_template(t, warn):
  clear()
  global score, answerfield, falseletters, started, data
  if started == 1:
    if t == 0:
      print("The hangmen - Singleplayer - Game\n")
      if score == 0:
        print("|------|    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print(warn)
      elif score == 1:
        print("|------|    ")
        print("|      O    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print(warn)
      elif score == 2:
        print("|------|    ")
        print("|      O    ")
        print("|      |    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("Bzzzz. Wrong letter")
      elif score == 3:
        print("|------|    ")
        print("|      O    ")
        print("|      |\\   ")
        print("|           ")
        print("|           ")
        print("|           ")
        print(warn)
      elif score == 4:
        print("|------|    ")
        print("|      O    ")
        print("|     /|\\   ")
        print("|           ")
        print("|           ")
        print("|           ")
        print(warn)
      elif score == 5:
        print("|------|    ")
        print("|      O    ")
        print("|     /|\\   ")
        print("|       \\   ")
        print("|           ")
        print("|           ")
        print(warn)
      elif score == 6:
        print("|------|    ")
        print("|      O    ")
        print("|     /|\\   ")
        print("|     / \\   ")
        print("|           ")
        print("|           ")
        print(warn)
      print("Word:", answerfield)
      print("Letters not included:", falseletters)
      ans = input("Choose a letter\n")
      if len(ans) != 1:
        hangman_template(t, "Type only one letter please.")
      else:
        flag = letter_check(ans.lower())
        if answerfield == word:
          data["singleplayer"]["wins"] += 1
          save_data()
          end_game_menu(1)
        elif score > 6:
          data["singleplayer"]["loses"] += 1
          save_data()
          end_game_menu(0)
        else:
          if flag == 0:
            hangman_template(t, "Bzzzz. Wrong letter.")
          elif flag == 1:
            hangman_template(t, "Damn thats a correct choice.")
          elif flag == 2:
            hangman_template(t, "Type a different letter.")
    elif t == 1:
      if score == 0:
        print("The hangmen - Multiplayer - Game")
    #  elif score == 1:
    # elif score == 2:
    #  elif score == 3:
  #   elif score == 4:
  #  elif score == 5:
  elif started == 0:
    print("End")


#Start game
def start_game(sn, t):
  clear()
  init_game_vars()
  print("Game is starting...\n")
  if t == 1:
    hangman_template(t, "")
  elif t == 0:
    hangman_template(t, "")



#Send message - Send to Server --> compile
def send_message(sn, msg):
  global data
  send_to_server(data["username"],
                 json.dumps({
                   "sn": sn,
                   "msg": msg
                 }), "sendmessage")


def game_lobby_template(sn):
  global members
  clear()
  print("The hangmen - Multiplayer - Game lobby")
  print("\nWelcome to the room:", sn)
  print("Players waiting:", members, "\n")
  print("Whenever you want to start the game just send \"start game\"\n")
  print("\nChat Section:")
  for msg in messages:
    print(msg)

#Game Lobby - Before start of the game
def game_lobby(sn):
  game_lobby_template(sn)
  while started != 1:
    msg = ""
    while msg == "":
      msg = input()
      if msg != "leave":
        send_message(sn, msg)
      else:
        leave_game(sn)
  start_game(sn, 1)


#Confirm game creation by Server
def game_created(sn):
  global members
  members = 1
  game_lobby(sn)


def reload_template(res,t):
  if t == 0:
    clear()
    messages.append(str(res["data"]["username"], ": ", res["data"]["message"]))
    game_lobby_template(res["data"]["sn"])
  elif t == 1:
    return

def get_msg(buffer):
        global server
        while not '\n' in buffer:
            data = server.recv(4096)
            if not data:
                return ''
            buffer += data
        sentinel = buffer.index('\n') + 1
        msg,buffer = buffer[:sentinel],buffer[sentinel:]
        return msg

#Receive from Server
def receive_from_server():
  global server,members,data
  res = ""
  #Issue with buffering information. For some reason the information is not buffered although transmited succesfully from server
  while True:
    buffer = (server.recv(4096))
    if len(buffer) != 0:
      print(buffer)
      res = res + buffer
    else:
      res = json.loads((buffer).decode())
      print(res)
      if res["type"] == "hostgame":
        print(res["status"])
        if res["status"] == 201:
          game_created(res["data"]["servername"])
      elif res["type"] == "sendmessage":
        if res["status"] == 200:
          reload_template(res,0)
      elif res["type"] == "connectgame":
        if res["status"] == 200:
          members = res["data"]["members"]
          if res["data"]["username"] == data["username"]:
            game_lobby(res["data"]["servername"])
          else:
            reload_template(res,0)
      elif res["type"] == "disconnectgame":
        if res["status"] == 200:
          members = res["data"]["members"]
          if res["data"]["username"] == data["username"]:
            menu()
          else:
            reload_template(res,0)
      res = ""      

#Send over to Server data
def send_to_server(un, d, type):
  global server
  if type == "hostgame" or type == "connectgame":
    d = json.loads(d)
    server.send(
      json.dumps({
      "type": type,
      "data": {
      "username": un,
      "servername": d["sn"],
      "serverpassword": d["sp"]
      }
    }).encode())
  elif type == "disconnectgame":
    d = json.loads(d)
    server.send(
      json.dumps({
      "type": type,
      "data": {
      "username": un,
      "servername": d["sn"],
      }
    }).encode())
  elif type == "sendmessage":
    d = json.loads(d)
    server.send(
      json.dumps({
        "type": type,
        "data": {
        "username": un,
        "servername": d["sn"],
        "message": d["msg"]
        }
      }).encode())
  elif type == "connect":
    server.send(
      json.dumps({
        "type": type,
        "data": {
        "username": un
        }
      }).encode())
  elif type == "disconnect":
    server.send(
      json.dumps({
      "type": type,
      "data": {
      "username": un
      }
    }).encode())


#Create game - From menu
def create_game():
  global data
  clear()
  print("The hangmen - Multiplayer - Creating game\n")
  print("Hosting a new game...\n")
  servername = input("Server name\n")
  serverpassword = input("Server password\n")
  send_to_server(data["username"],
                 json.dumps({
                   "sn": servername,
                   "sp": serverpassword
                 }), "hostgame")


#Join game - From menu
def join_game():
  global data
  clear()
  print("The hangmen - Multiplayer - Joining game\n")
  print("\nJoining game...\n")
  servername = input("Server name\n")
  serverpassword = input("Server password\n")
  send_to_server(data["username"],
                 json.dumps({
                   "sn": servername,
                   "sp": serverpassword
                 }), "connectgame")
#Leave game - From room
def leave_game(servername):
  global data
  send_to_server(data["username"],
                 json.dumps({
                   "sn": servername,
                 }), "disconnectgame")
  menu()
  

def stats():
  global data
  clear()
  print("The hangmen - Settings - Stats\n")
  print("Singleplayer")
  print("  Wins:", data["singleplayer"]["wins"])
  print("  Loses:", data["singleplayer"]["loses"])
  print("\nPress 1 to go back")
  ans = input()
  if ans == "1":
    settings()
  else:
    print("Invalid option\n")
    stats()


#Settings - From menu
def settings():
  global data
  clear()
  print("The hangmen - Settings\n")
  print("1. Change username")
  print("2. See stats")
  print("3. Back")
  ans = input()
  if ans == "1":
    clear()
    print("The hangmen - Settings - Username\n")
    print("Your current username is", data["username"])
    print("Write \"cancel\" if you changed your mind")
    ans = input("Pick a username\n")
    if ans != "cancel":
      data["username"] = ans
      save_data()
      settings()
    elif ans == "cancel":
      settings()
  elif ans == "2":
    stats()
  elif ans == "3":
    menu()
  else:
    print("Invalid option\n")
    settings()


#Exit - From menu
def exit():
  clear()
  if active == 1:
    server.close()
  print("Exiting..")
  sys.exit()

#Game settings
def game_settings(t):
  global topic, difficulty, topics, difficulties
  clear()
  print("The Hangmen - Singleplayer - Game settings\n")
  if t == 1:
    print("Topic: {}".format(topics[topic - 1]))
    print("1. Computer science")
    print("2. Physics")
    print("3. Chemistry")
    print("4. Biology")
    print("5. General")
    print("6. Back")
    ans = input()
    if ans == "6":
      game_settings_menu()
    else:
      topic = int(ans)
      if topic > 6 and topic < 1:
        print("Invalid option\n")
        game_settings(1)
      else:
        game_settings_menu()
  elif t == 2:
    print("Difficulty: {}".format(difficulties[difficulty - 1]))
    print("1. Too easy")
    print("2. Easy")
    print("3. Medium")
    print("4. Hard")
    print("5. Maou too easy (impossible)")
    print("6. Back")
    ans = input()
    if ans == "6":
      game_settings_menu()
    else:
      difficulty = int(ans)
      if difficulty > 6 and difficulty < 1:
        print("Invalid option\n")
        game_settings(1)
      else:
        game_settings_menu()


#Game settings menu
def game_settings_menu():
  global topic, difficulty, topics, difficulties
  clear()
  print("The Hangmen - Singleplayer - Game settings\n")
  print("Topic: {}".format(topics[topic - 1]))
  print("Difficulty: {}".format(difficulties[difficulty - 1]))
  print("1. Choose topic of words")
  print("2. Difficulty")
  print("3. Back")
  ans = input()
  if ans == "1":
    game_settings(1)
  elif ans == "2":
    game_settings(2)
  elif ans == "3":
    singleplayer_menu()
  else:
    print("Invalid option\n")
    game_settings_menu()


#Singleplayer menu
def singleplayer_menu():
  clear()
  print("The hangmen - Singleplayer\n")
  print("1. Start game")
  print("2. Game settings")
  print("3. Back")
  ans = input()
  if ans == "1":
    start_game("local", 0)
  elif ans == "2":
    game_settings_menu()
  elif ans == "3":
    menu()
  else:
    print("Invalid option\n")
    singleplayer_menu()

#Multiplayer menu
def multiplayer_menu():
  if active == 1:
    global data
    send_to_server(data["username"], "", "connect")
    clear()
    print("The hangmen - Multiplayer\n")
    print("1. Create a game")
    print("2. Join a game")
    print("3. Back")
    ans = input()
    if ans == "1":
      create_game()
    elif ans == "2":
      join_game()
    elif ans == "3":
      menu()
    else:
      print("Invalid option\n")
      multiplayer_menu()
  elif active == 0:
    clear()
    print("The hangmen - Multiplayer\n")
    print("Feature rolling out 1st of April")
    print("1. Back")
  ans = input()
  if ans == "1":
    menu()
  else:
    print("Invalid option\n")
    multiplayer_menu()


#The menu
def menu():
  clear()
  print("The hangmen\n")
  print("1. Singleplayer")
  print("2. Multiplayer")
  print("3. Settings")
  print("4. Exit")
  ans = input()
  if ans == "1":
    singleplayer_menu()
  elif ans == "2":
    multiplayer_menu()
  elif ans == "3":
    settings()
  elif ans == "4":
    exit()
  else:
    print("Invalid option\n")
    menu()


#Start
clear()
print("Welcome to the hangmen\n")
print(
  "Hangmen is an interactive multiplayer CLI game based on the original game Hangman, originated in 17th century\n"
)

if firstTime == 1:
  print("As this is your first time playing, you should set up a username")
  data["username"] = input()
  firstTime = 0
  save_data()

if active == 1:
  receive_thread = threading.Thread(target=receive_from_server)
  receive_thread.start()  


try:
  menu()
except KeyboardInterrupt:
        clear()
        print('Ctrl + C just pressed, exiting...')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)