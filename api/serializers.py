

"""

login
referal
payment gateway
enrollment system of courses
invoice email
review
deals

"""




from user_accounts.models import staff, Product
from rest_framework.serializers import Serializer, CharField, ModelSerializer, SerializerMethodField


class product_serializer(Serializer):
    name = CharField(read_only=True)


class peopleserializer(Serializer):
    username = CharField(read_only=True)


class staff_serializers(ModelSerializer):
    people = SerializerMethodField()
    # Corrected field name to start with lowercase
    other_courses = SerializerMethodField()

    class Meta:
        model = staff
        fields = [
            "name",
            "referal_code",
            "people",
            "other_courses",  # Corrected field name to match the method
        ]

    def get_other_courses(self, obj):  # Corrected method name to start with lowercase
        qs = Product.objects.filter(referal=obj)
        b = []
        for i in qs:
            b.append(product_serializer(i).data["name"])
        return b

    def get_people(self, obj):
        a = []
        qs = obj.people_joined.all()
        for i in qs:
            data = peopleserializer(i).data
            a.append(data["username"])
        return a
