from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        if (self.get_limit(self.request) == 10
           and self.get_offset(self.request) == 0):
            return Response(data)

        return super().get_paginated_response(data)
