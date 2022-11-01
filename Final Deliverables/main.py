from cloudant.client import Cloudant

#creating the Cloudant Database 
client = Cloudant.iam("1c6f917d-87ac-491b-90a0-6e3ae5b5daca-bluemix","tYJcUyVJYs3WrxF_1absTN4RXrbdQ_RDWBRUy9BX-28c",connect=True)
database = client.create_database("bath4_database")