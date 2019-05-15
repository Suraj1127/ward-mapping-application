import csv
from .models import Map2011, Map2014


def upload(year):
    with open('ward_mapping/static/mapping_data/mapping_{}.csv'.format(year)) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:

            if year == 2011:
                _, created = Map2011.objects.get_or_create(
                    zone=row[0],
                    district=row[1],
                    old_survey_vdc_name=row[2],
                    old_survey_vdc_code=row[3],
                    old_ward_no=row[4],
                    old_survey_ward_code=row[5],
                    province=row[6],
                    new_district=row[7],
                    cbs_district_code=row[8],
                    category_of_lu=row[9],
                    lu_name=row[10],
                    lu_full_name=row[11],
                    lu_name_nepali=row[12],
                    cbs_lu_code=row[13],
                    lu_ward_no=row[14],
                    cbs_ward_code=row[15],
                )
            elif year == 2014:
                _, created = Map2014.objects.get_or_create(
                    district=row[0],
                    vdc_muni=row[1],
                    old_ward_no=row[2],
                    province=row[3],
                    cbs_district_code=row[4],
                    category_of_lu=row[5],
                    lu_name=row[6],
                    lu_full_name=row[7],
                    lu_name_nepali=row[8],
                    lu_hlcit_code=row[9],
                    lu_cbs_code=row[10],
                    new_ward_no=row[11],
                    cbs_ward_code=row[12],
                )
            else:
                pass
