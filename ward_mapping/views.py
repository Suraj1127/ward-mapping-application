from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from .models import Map2011, Map2014
from django.db.models import Q

from .data_accumulator import upload


def accumulate(request, year):
    if request.method == "POST":
        upload(year)
    return render(request, 'ward_mapping/upload.html')


def index(request, year):
    return render(request, 'ward_mapping/index.html', {'year': year})


@csrf_exempt
def index_asJSON(request, year):
    try:
        start = int(request.POST.get('start', 0))
    except ValueError:
        start = 0

    length = int(request.POST.get('length', 10))
    sort_by_index = int(request.POST.get("order[0][column]", 0))

    order = request.POST.get("order[0][dir]", "asc")

    sort_bys = ["zone"] if year == 2011 else ["district"]
    if sort_by_index > 1:
        sort_by_index = 0

    sort_by = sort_bys[sort_by_index]
    if order != "asc":
        sort_by = "-" + sort_by

    query = request.POST.get("search[value]", "").strip()

    total_count = Map2011.objects.all().count() if year == 2011 else Map2014.objects.all().count()

    if query:
        if year == 2011:
            matches = Map2011.objects.filter(
                Q(zone__contains=query.strip())
                | Q(district__contains=query.strip())
                | Q(old_survey_vdc_name__contains=query.strip())
                | Q(old_survey_vdc_code__contains=query.strip())
                | Q(old_ward_no__contains=query.strip())
                | Q(old_survey_ward_code__contains=query.strip())
                | Q(province__contains=query.strip())
                | Q(new_district__contains=query.strip())
                | Q(cbs_district_code__contains=query.strip())
                | Q(category_of_lu__contains=query.strip())
                | Q(lu_name__contains=query.strip())
                | Q(lu_full_name__contains=query.strip())
                | Q(lu_name_nepali__contains=query.strip())
                | Q(cbs_lu_code__contains=query.strip())
                | Q(lu_ward_no__contains=query.strip())
                | Q(cbs_ward_code__contains=query.strip())
            ).order_by(sort_by)
        elif year == 2014:
            matches = Map2014.objects.filter(
                Q(district__contains=query.strip())
                | Q(vdc_muni__contains=query.strip())
                | Q(old_ward_no__contains=query.strip())
                | Q(province__contains=query.strip())
                | Q(cbs_district_code__contains=query.strip())
                | Q(category_of_lu__contains=query.strip())
                | Q(lu_name__contains=query.strip())
                | Q(lu_full_name__contains=query.strip())
                | Q(lu_name_nepali__contains=query.strip())
                | Q(lu_hlcit_code__contains=query.strip())
                | Q(lu_cbs_code__contains=query.strip())
                | Q(new_ward_no__contains=query.strip())
                | Q(cbs_ward_code__contains=query.strip())
            ).order_by(sort_by)
        else:
            pass
    else:
        matches = Map2011.objects.filter().order_by(sort_by) if year == 2011 else Map2014.objects.filter().order_by(sort_by)

    data = []
    for i in matches[start:start+length]:
        data.append(i)
    data = serializers.serialize('json', data)

    response = {
        "draw": int(request.POST.get('draw', 0)),
        "recordsTotal": total_count,
        "recordsFiltered": matches.count(),
        "data": eval(data),
    }
    return JsonResponse(response)
