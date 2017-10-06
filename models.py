from flask_restful import Resource

class OrganismeList(Resource):
    def get(self):
        return [{'id':'0','name':'SCFP2850'}]

class Organisme(Resource):
    def get(self, id):
        return {'id':'0','name':'SCFP2850'}

class ConventionList(Resource):
    def get(self, organisme=None):
        return [{'id':'0','name':'toto'}]

class Convention(Resource):
    def get(self, id):
        return {'id':'0','name':'toto'}

class VersionList(Resource):
    def get(self, convention=None):
        return [{'id':'0','periode':'toto'}]

class Version(Resource):
    def get(self, id):
        return {'name':'toto', 'periode':{'deput':'18 juin 2012','fin':'6 janvier 2018'}}

class ArticleList(Resource):
    def get(self, convention=None):
        return [{'id':'0', 'numero':'1', 'nom':'Reconnaissane'}]
