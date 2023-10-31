from mongoengine import *


connect(host ="mongodb+srv://IrynaHryma:2213@cluster7.oesajgi.mongodb.net/web13?retryWrites=true&w=majority",ssl= True)

class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField()
    born_location = StringField(max_length=50)
    description = SequenceField(max_length=50)




class Quote(Document):
    author = ReferenceField(Author,reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    quote= StringField(required=True)
    
    meta = {'allow_inheritance': True} 

class TextPost(Quote):
    content = StringField()


