# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
import json
from ducks import Dex


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ipaddr = "127.0.0.1"
port = int(8888)

games = []
gametemplate = Dex(games, {"servername": str, "serverpassowrd": str})
list_of_clients = {}

try:
  server.bind((ipaddr, port))
except socket.error as er:
  str(er)

server.listen(100)
print("Server up and running")

def handle_connections(sock, un, t):
  global list_of_clients
  if t == "connect":
    list_of_clients[sock] = {"username": un}
    print(list_of_clients[sock], " connected")
    return json.dumps({"status": 201, "type": t, "data": {"username": un}})


def create_game(sock, un, sn, sp, t):
  global games
  games.append({
    "creatorname": un,
    "servername": sn,
    "serverpassword": sp,
    "clients": [sock]
  })
  print(games)
  return json.dumps({"status": 201, "type": t, "data": {"username": list_of_clients[sock]["username"], "servername": sn}})

def join_game(sock,un, sn, sp, t):
  for game in games:
    if game["servername"] == sn and game["serverpassword"] == sp:
      game["clients"].append(sock)
      return json.dumps({"status": 200, "type": t, "data": {"username": list_of_clients[sock]["username"], "servername": sn, "members": len(game["clients"])}})
  return json.dumps({"status": 404, "type": t, "data": {"username": list_of_clients[sock]["username"], "servername": sn}})
  
def leave_game(sock,un, sn, t):
  for game in games:
    if game["servername"] == sn:
      game["clients"].remove(sock)
      if len(game["clients"]) < 1:
        games.remove(game)
      print(games)
      return json.dumps({"status": 200, "type": t, "data": {"username": list_of_clients[sock]["username"], "servername": sn, "members": len(game["clients"])}})
  return json.dumps({"status": 404, "type": t, "data": {"username": list_of_clients[sock]["username"], "servername": sn}})
    
def send_message(un, sn, msg, t):
    return json.dumps({
            "status": 200,
            "type": t,
            "data": {
              "username": un,
              "servername": sn,
              "message": msg
            }
          })


def broadcast(message, room, connection, t):
  print(t)
  print("a")
  if t == 0:
    try:
      print(list_of_clients[connection])
      connection.send(message.encode())
    except:
      connection.close()
      remove(connection)
  elif t == 1:
    print("wtff")
    print(list_of_clients)
    for client in list_of_clients.keys():        
        print(list_of_clients[client], list_of_clients[connection])
        try:
          print("just send", message)
          client.send(message.encode())
        except:
          client.close()
          remove(client)


def remove(connection):
  if connection in list_of_clients:
    del list_of_clients[connection]

def clientthread(conn):
  # sends a message to the client whose user object is conn
  while True:
    try:
      msg = json.loads(conn.recv(4096).decode())
      print(msg)
      if msg["type"] == "connect":
        print("connecting user...")
        res = handle_connections(conn, msg["data"]["username"], msg["type"])
        broadcast(res, "", conn, 0)
      elif msg["type"] == "hostgame":
        res = create_game(conn, msg["data"]["username"],
                          msg["data"]["servername"],
                          msg["data"]["serverpassword"], msg["type"])
        broadcast(res, msg["data"]["servername"], conn, 0)
      elif msg["type"] == "connectgame":
        res = join_game(conn,msg["data"]["username"], msg["data"]["servername"],
                        msg["data"]["serverpassword"], msg["type"])
        broadcast(res, msg["data"]["servername"], conn, 1)
      elif msg["type"] == "disconnectgame":
        res = leave_game(conn,msg["data"]["username"], msg["data"]["servername"],
                        msg["type"])
        broadcast(res, msg["data"]["servername"], conn, 1)
      elif msg["type"] == "sendmessage":
        res = send_message(msg["data"]["username"],msg["data"]["servername"],msg["data"]["message"],msg["type"])
        print(res)
        broadcast(res, msg["data"]["servername"], conn, 1)
      else:
        remove(conn)
    except Exception as e:
      print("exception", e)
      conn.close()
      remove(conn)
      return

while True:
  conn, addr = server.accept()
  start_new_thread(clientthread, (conn,))

conn.close()
server.close()
