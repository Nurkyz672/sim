from  rest_framework.pagination import PageNumberPagination

class MovieListAPIViewPagination(PageNumberPagination):
    page_size = 5


class CategoryListAPIViewPagination(PageNumberPagination):
    page_size = 3















