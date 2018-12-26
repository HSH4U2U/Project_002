from django.shortcuts import render
from .models import Subject
from django.db.models import Q
# from .importing_class_list import importing_class_list


# Create your views here.
# 이미 importing 작업 끝냄
# importing_class_list()


def base(request):
    if "search" in request.GET:
        search_term = request.GET["search"]
        if search_term:
            subjects = Subject.objects.filter(
                Q(name__icontains=search_term) |
                Q(professor__icontains=search_term)
            ).distinct().order_by('name')
            for subject in subjects:
                subject.name = list(subject.name.partition(search_term))
                subject.professor = list(subject.professor.partition(search_term))
            # select 무엇이 되었는지 구별(족보 등록인지 족보 검색인지)
            if "select" in request.GET:
                select = request.GET["select"]
        ctx = {
            'select': select,
            'search_term': search_term,
            'subjects': subjects
        }
        return render(request, 'asitis/search.html', ctx)
    ctx = {}
    return render(request, 'asitis/base.html', ctx)
