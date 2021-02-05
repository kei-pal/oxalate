from import_export import resources
from lookup.models import Ingredient

class MemberResource(resources.ModelResource):
    class Meta:
        model = Ingredient