import rest_framework.pagination as pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'length': self.page.paginator.count,
            'data': data,
        })
