import sqlite3
from django.apps import AppConfig


class DailyphotoConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'dailyphoto'

def load_feed_by_time():
  conn=sqlite3.connect("db.sqlite3")
  cursor=conn.cursor()

#   cursor.execute("SELECT * FROM post")
#   print(cursor.fetchall())

  cursor.execute("SELECT * FROM dailyphoto_post ORDER BY id DESC")
#   print(cursor.fetchall())

  card_list=[]
  for i in range(3):
    c=  cursor.fetchone() #튜플
    card_list.append(c) 
    # print(c)
    # print(type(c)) #튜플이라고 한다 

  print(card_list)

  cursor.close()
  conn.close()

  return card_list

# load_feed_by_time()