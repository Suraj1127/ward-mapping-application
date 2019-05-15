# Generated by Django 2.2 on 2019-05-15 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ward_mapping', '0002_auto_20190515_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map2011',
            old_name='category_of_lu_2018',
            new_name='category_of_lu',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='cbs_district_code_2018',
            new_name='cbs_district_code',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='cbs_lu_code_2018',
            new_name='cbs_lu_code',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='cbs_lu_ward_code_2018',
            new_name='cbs_ward_code',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='district_2011',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='lu_full_name_2018',
            new_name='lu_full_name',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='lu_name_2018',
            new_name='lu_name',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='lu_name_nepali_2018',
            new_name='lu_name_nepali',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='lu_ward_no_2018',
            new_name='lu_ward_no',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='new_district_2018',
            new_name='new_district',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='old_survey_vdc_code_2011',
            new_name='old_survey_vdc_code',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='old_survey_vdc_name_2011',
            new_name='old_survey_vdc_name',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='old_survey_ward_code_2011',
            new_name='old_survey_ward_code',
        ),
        migrations.RenameField(
            model_name='map2011',
            old_name='old_ward_no_2011',
            new_name='old_ward_no',
        ),
    ]
