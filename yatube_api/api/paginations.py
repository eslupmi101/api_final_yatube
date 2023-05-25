from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        if self.limit is None and self.offset is None:
            return Response(data)

        return super().get_paginated_response(data)

    def paginate_queryset(self, queryset, request, view=None):
        if (
            request.GET.get('limit') is None
            and request.GET.get('offset') is None
        ):
            return None

        return super().paginate_queryset(queryset, request, view)
