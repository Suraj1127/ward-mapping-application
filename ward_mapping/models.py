from django.db import models


# models
class Map2011(models.Model):
    zone = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    old_survey_vdc_name = models.CharField(max_length=100)
    old_survey_vdc_code = models.CharField(max_length=30)
    old_ward_no = models.PositiveSmallIntegerField()
    old_survey_ward_code = models.CharField(max_length=30, unique=True)
    province = models.PositiveSmallIntegerField()
    new_district = models.CharField(max_length=30)
    cbs_district_code = models.PositiveSmallIntegerField()
    category_of_lu = models.CharField(max_length=50)
    lu_name = models.CharField(max_length=100)
    lu_full_name = models.CharField(max_length=200)
    lu_name_nepali = models.CharField(max_length=200)
    cbs_lu_code = models.PositiveIntegerField()
    lu_ward_no = models.PositiveSmallIntegerField()
    cbs_ward_code = models.PositiveIntegerField()


class Map2014(models.Model):
    district = models.CharField(max_length=50)
    vdc_muni = models.CharField(max_length=300)
    old_ward_no = models.PositiveSmallIntegerField()
    province = models.PositiveSmallIntegerField()
    cbs_district_code = models.PositiveSmallIntegerField()
    category_of_lu = models.CharField(max_length=50)
    lu_name = models.CharField(max_length=100)
    lu_full_name = models.CharField(max_length=200)
    lu_name_nepali = models.CharField(max_length=200)
    lu_hlcit_code = models.CharField(max_length=30)
    lu_cbs_code = models.PositiveIntegerField()
    new_ward_no = models.PositiveSmallIntegerField()
    cbs_ward_code = models.PositiveIntegerField()
