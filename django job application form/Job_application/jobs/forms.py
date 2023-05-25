from django import forms
# from .models import CandidateMaster
from .models import CandidateMaster,AcademicMaster,ExperienceMaster, LanguageKnownMaster, ReferenceMaster, PreferenceMaster, TechnologyKnownMaster
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class CandidateMasterForm(forms.ModelForm):
    class Meta:
        model = CandidateMaster
        fields = [
            'fname',
            'lname',
            'surname',
            'contact_no',
            'city',
            'state',
            'email',
            'gender',
            'dob'   ]
        widgets={
            'dob': DateInput(),
        }




class AcademicMasterForm(forms.ModelForm):
    class Meta:
        model= AcademicMaster
        fields=[

            'course_name',
            'name_of_board_university',
            'passing_year',
            'percentage'

        ]



class ExperienceMasterForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")
        print(f'from_date:{from_date} \n to_date: {to_date}')

        if from_date >= to_date:
            raise ValidationError("To date must be greater than from date!!!")


    class Meta:
        model=ExperienceMaster
        fields=[
            'company_name',
            'designation',
            'from_date',
            'to_date'
        ]
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput(),
        }


# LANGUAGE_CHOICES = [('Hindi','Hindi'),('English','English'),('Gujrati', 'Gujrati')]
class LanguageKnownMasterForm(forms.ModelForm):
    class Meta:
        model = LanguageKnownMaster
        # language = forms.CharField(label='language', widget=forms.RadioSelect(choices=LANGUAGE_CHOICES))
        # # language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.RadioSelect())

        # widgets = {'language': forms.Select}
        fields=[]








class TechnologyKnownMasterForm(forms.Form):
    RATING_CHOICES = [
        ('3', 'Begginer'),
        ('6', 'Mediator'),
        ('10', 'Expert')
    ]
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RATING_CHOICES,
    )



class TechnologyKnownMasterModelForm(forms.ModelForm):
    class Meta:
        model = TechnologyKnownMaster
        fields=[]







class ReferenceMasterForm(forms.ModelForm):
    class Meta:
        model= ReferenceMaster
        fields=[
            'refe_name',
            'refe_contact_no',
            'refe_relation'

        ]


class PreferenceMasterForm(forms.ModelForm):
    class Meta:
        model= PreferenceMaster
        fields=[
            'prefer_location',
            'notice_period',
            'expected_ctc',
            'current_ctc',
            'department'

        ]