from django.db import models
from django.core.exceptions import ValidationError
from django import forms

def validate_name(value):
    if value.isalpha():
        return value

    else:
        raise ValidationError("This field accepts alphabets only")


def validate_contact_no(value):
    if  value.isdigit():
        return value

    else:
        raise ValidationError("Contact should only contains digit!!")


def validate_dob(value):
    if value.year <= 2004:
        return value
    else:
        raise ValidationError("Please enter valid date of birth!!")


def validate_year(value):
    if value<=2023 and value>=2000:
        return value
    else:
        raise ValidationError("Please Enter valid year in format YYYY!! and not 2024")


def validate_percentage(value):
    if value <=100 and value >=0:
        return value
    else:
        raise ValidationError("Please enter percentage between 0 to 100!!")


def validate_rating(value):
    if value > 0 and value <=10:
        return value
    else:
        raise ValidationError("Rating should be between 1 to 10 !!")




def validate_notice_period(value):
    if value>0 and value <= 12:
        return value
    else:
        raise ValidationError("Notice period should be between 0 to 12!!!")




# Create your models here.
GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female'),
   ('Other','Other')
)

COURSE_CHOICES=(
    ('SSC','SSC'),
    ('HSC','HSC'),
    ('BECHELOR','BECHELOR'),
    ('MASTER','MASTER')
)

LANGUAGE_CHOICES = [('Hindi','Hindi'),('English','English'),('Gujrati', 'Gujrati')]

TECHNOLOGY_CHOICES = [('PHP','PHP'),('Laravel','Laravel'),('Mysql','Mysql'),('Oracle','Oracle')]

PREFER_LOCATION_CHOICES= [('Ahmedabad','Ahmedabad'),('Surat','Surat'),('Rajkot','Rajkot')]

DEPARTMENT_CHOICES = [('Development','Development'),('Design','Design'),('HR','HR'),('Testing','Testing')]




class CandidateMaster(models.Model):
    fname = models.CharField(max_length=30, validators = [validate_name])
    lname = models.CharField(max_length=30,validators = [validate_name])
    surname = models.CharField(max_length=30,validators = [validate_name])
    contact_no = models.CharField(max_length=10, validators = [validate_contact_no])
    city = models.CharField(max_length=30,validators = [validate_name])
    state = models.CharField(max_length=30,validators = [validate_name])
    email = models.EmailField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=30)
    dob = models.DateField(validators=[validate_dob])


class AcademicMaster(models.Model):
    candidate= models.ForeignKey('CandidateMaster',on_delete=models.CASCADE)
    course_name= models.CharField(choices=COURSE_CHOICES,max_length=30)
    name_of_board_university = models.CharField(max_length=30,validators=[validate_name])
    passing_year=models.IntegerField(validators=[validate_year])
    percentage = models.IntegerField(validators=[validate_percentage])



class ExperienceMaster(models.Model):
    candidate = models.ForeignKey('CandidateMaster', on_delete=models.CASCADE)
    company_name= models.CharField(max_length=50,validators=[validate_name])
    designation= models.CharField(max_length=50,validators=[validate_name])
    from_date = models.DateField()
    to_date= models.DateField()


class LanguageKnownMaster(models.Model):
    candidate = models.ForeignKey('CandidateMaster', on_delete=models.CASCADE)
    language= models.CharField(max_length=30,null=True,blank=True)
    read = models.NullBooleanField(blank=True)
    write = models.NullBooleanField(blank=True)
    speak = models.NullBooleanField(blank=True)



class TechnologyKnownMaster(models.Model):
    candidate = models.ForeignKey('CandidateMaster', on_delete=models.CASCADE)
    technology = models.CharField(max_length=30,null=True,blank=True)
    ranting = models.IntegerField(validators=[validate_rating],null=True,blank=True)







class ReferenceMaster(models.Model):
    candidate = models.ForeignKey('CandidateMaster', on_delete=models.CASCADE)
    refe_name = models.CharField(max_length=50, validators=[validate_name])
    refe_contact_no = models.CharField(max_length=10, validators=[validate_contact_no])
    refe_relation = models.CharField(max_length=30,validators=[validate_name])



class PreferenceMaster(models.Model):
    candidate = models.ForeignKey('CandidateMaster', on_delete=models.CASCADE)
    prefer_location = models.CharField(max_length=30, choices=PREFER_LOCATION_CHOICES)
    notice_period = models.IntegerField(validators=[validate_notice_period])
    expected_ctc = models.IntegerField()
    current_ctc = models.IntegerField()
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)

