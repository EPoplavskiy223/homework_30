from rest_framework.serializers import ModelSerializer

from education.serializers import CourseDetailSerializer, LessonSerializer
from users.models import Payment, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            "id",
            "user",
            "payment_date",
            "payment_amount",
            "payment_method",
            "paid_course",
            "paid_lesson",
        )


class PaymentDetailSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)
    paid_course = CourseDetailSerializer(read_only=True)
    paid_lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"


class UserDetailSerializer(ModelSerializer):

    paid_course = CourseDetailSerializer(read_only=True)
    paid_lesson = LessonSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "date_joined",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "paid_course",
            "paid_lesson",
        ]
