from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(data)
