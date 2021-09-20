from django.core.validators import validate_email

from core.serializer.accountserialize import AccountSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics

from core.serializer.accountserialize import AccountSerializer


class AccountRegisterView(APIView):

    @swagger_auto_schema(
        operation_id='유저 목록조회',
        operation_description="유저 데이터 조회입니다",

        manual_parameters=[
            openapi.Parameter('nickname', openapi.IN_QUERY, required=True, description="회원 nickname",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('email', openapi.IN_QUERY, required=True, description="회원 nickname",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('password', openapi.IN_QUERY, required=True, description="회원 nickname",
                              type=openapi.TYPE_NUMBER),
        ],

        responses={
            200: openapi.Response(
                description="정상적인 경우",
                schema=AccountSerializer(many=True)
            )
        }
    )
    def get(self, request):
        return Response({"message": "ok"})

    @swagger_auto_schema(
        operation_id="유저 생성하기",
        operation_description="유저 생성하기",

        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'reg_nickname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'reg_email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'reg_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            },
            required=['reg_nickname', 'reg_email', 'reg_password']
        ),
        responses={
            200: 'ok',
        }

    )
    def post(self, request):
        serializer = AccountSerializer(data=request.POST)
        print(serializer.is_valid())

        return Response(200)
