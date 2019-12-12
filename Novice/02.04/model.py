import json


class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))


   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(self):
      # data = pd.read_json('/mnt/c/Users/HP/Documents/source_python/design_pattern/actor.json', 'r')
      # print(data)
      database = open('/mnt/c/Users/HP/Documents/source_python/design_pattern/actor.json', 'r')
      result = []
      json_list = json.loads(database.read())
      for item in json_list:
         person = Person(item['first_name'], item['last_name'])
         result.append(person)
      return result

   # @classmethod
   # #returns all people inside db.txt as list of Person objects
   # def getAll(self):
   #    with open('/mnt/c/Users/HP/Documents/source_python/design_pattern/actor.json') as json_file:
   #       data = json.load(json_file)
   #       for p in data:
   #          print('first name: ' + p['first_name'])
   #          print('last name: ' + p['last_name'])
   #          print('')