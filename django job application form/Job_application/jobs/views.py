from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.


from django.views.generic.edit import CreateView
from .models import CandidateMaster,AcademicMaster,ExperienceMaster,LanguageKnownMaster,TechnologyKnownMaster, ReferenceMaster,PreferenceMaster
# from .forms import CandidateMasterForm
from .forms import CandidateMasterForm, AcademicMasterForm, ExperienceMasterForm, LanguageKnownMasterForm, TechnologyKnownMasterForm,TechnologyKnownMasterModelForm ,ReferenceMasterForm, PreferenceMasterForm


def create_view(request):
    if request.user.is_superuser:
        context = {}
        form = CandidateMasterForm(request.POST or None)
        form_acade= AcademicMasterForm(request.POST or None)
        form_exper = ExperienceMasterForm(request.POST or None)
        form_langu = LanguageKnownMasterForm(request.POST or None)
        form_refer = ReferenceMasterForm(request.POST or None)
        form_prefe = PreferenceMasterForm(request.POST or None)
        form_techn = TechnologyKnownMasterForm(request.POST or None)
        form_techn_model = TechnologyKnownMasterModelForm(request.POST or None)

        # print("check box btn value for php :::", request.POST['PHP'])








        # if request.POST['PHP'] == 'PHP':
        #     php = request.POST['PHPradio']
        # if request.POST['Laravel'] == 'Laravel':
        #     laravel = request.POST['Laravelradio']
        # if request.POST['Mysql'] == 'Mysql':
        #     mysql = request.POST['Mysql']
        # if request.POST['Oracle'] == 'Oracle':
        #     oracle = request.POST['Oracle']







        # print("radio btn value for php :::", php)







        if form.is_valid() and form_acade.is_valid() and form_exper.is_valid()  and form_refer.is_valid() and form_prefe.is_valid():
            intance= form.save(commit=True)

            print("intance.....", intance)

            print("user id.......", request.user.id)

            # intance.user = CandidateMaster.objects.get(pk=request.user.id)


            # intance.user= CandidateMaster.objects.get(id=request.user.id)

            intance.save()
            # print("........................INSTANT ID:::", intance.id, intance.user)

            profile = form_acade.save(commit=False)
            profile.candidate = intance
            profile.save()

            profile = form_exper.save(commit=False)
            profile.candidate = intance
            profile.save()

            # ........

            profile = form_langu.save(commit=False)
            profile.candidate = intance

            if "Hindi" in request.POST:
                if "Hindiread" in request.POST:
                    profile.language = "Hindi"
                    profile.read = True
                    profile.write = False
                    profile.speak = False

                if "Hindiwrite" in request.POST:
                    profile.language = "Hindi"
                    profile.write = True
                    profile.read = False
                    profile.speak = False

                if "Hindispeak" in request.POST:
                    profile.language = "Hindi"
                    profile.speak = True
                    profile.write = False
                    profile.read = False



            if "Gujrati" in request.POST:
                if "Gujratiread" in request.POST:
                    profile.language = "Gujrati"
                    profile.read = True
                    profile.write = False
                    profile.speak = False

                if "Gujratiwrite" in request.POST:
                    profile.language = "Gujrati"
                    profile.write = True
                    profile.read = False
                    profile.speak = False

                if "Gujratispeak" in request.POST:
                    profile.language = "Gujrati"
                    profile.speak = True
                    profile.write = False
                    profile.read = False

            if "English" in request.POST:
                if "Englishread" in request.POST:
                    profile.language = "English"
                    profile.read = True
                    profile.write = False
                    profile.speak = False

                if "Englishwrite" in request.POST:
                    profile.language = "English"
                    profile.write = True
                    profile.read = False
                    profile.speak = False

                if "Englishspeak" in request.POST:
                    profile.language = "English"
                    profile.speak = True
                    profile.write = False
                    profile.read = False




            # profile.language= 'Hindi'

            # print(";;;;;;;;;form data::::::::", form_langu.cleaned_data)
            profile.save()



            # ...........

            profile = form_techn_model.save(commit=False)
            profile.candidate = intance

            if 'PHP' in request.POST:
                php = request.POST['PHPradio']
                if php == "begginer":
                    profile.technology='PHP'
                    profile.ranting=3

                elif php == "mediator":
                    profile.technology = 'PHP'
                    profile.ranting = 6

                elif php == "expert":
                    profile.technology = 'PHP'
                    profile.ranting = 10

                else:
                    profile.technology = 'PHP'
                    profile.ranting = 3




            if 'Laravel' in request.POST:
                laravel = request.POST['Laravelradio']
                if laravel == "begginer":
                    profile.technology = 'Laravel'
                    profile.ranting = 3

                elif laravel == "mediator":
                    profile.technology = 'Laravel'
                    profile.ranting = 6

                elif laravel == "expert":
                    profile.technology = 'Laravel'
                    profile.ranting = 10

                else:
                    profile.technology = 'Laravel'
                    profile.ranting = 3



            if 'Mysql' in request.POST:
                mysql = request.POST['Mysql']
                if mysql == "begginer":
                    profile.technology = 'Mysql'
                    profile.ranting = 3

                elif mysql == "mediator":
                    profile.technology = 'Mysql'
                    profile.ranting = 6

                elif mysql == "expert":
                    profile.technology = 'Mysql'
                    profile.ranting = 10

                else:
                    profile.technology = 'Mysql'
                    profile.ranting = 3



            if 'Oracle' in request.POST:
                oracle = request.POST['Oracle']
                if oracle == "begginer":
                    profile.technology = 'Oracle'
                    profile.ranting = 3

                elif oracle == "mediator":
                    profile.technology = 'Oracle'
                    profile.ranting = 6

                elif oracle == "expert":
                    profile.technology = 'Oracle'
                    profile.ranting = 10

                else:
                    profile.technology = 'Oracle'
                    profile.ranting = 3





            # profile.ranting = '10'
            # profile.technology='PHP'
            # print(";;;;;;;;;form data::::::::", form_techn.cleaned_data)
            # profile.ranting = form_techn.cleaned_data['rating']
            profile.save()

            # .........

            profile = form_refer.save(commit=False)
            profile.candidate = intance
            profile.save()

            # ........
            profile = form_prefe.save(commit=False)
            profile.candidate = intance
            profile.save()


            return HttpResponseRedirect("/job/success/")


        context["form"] = form
        context["form_acade"] = form_acade
        context["form_exper"] = form_exper
        context["form_langu"] = form_langu
        context["form_techn"] = form_techn
        context["form_refer"] = form_refer
        context["form_prefe"] = form_prefe
        context["data"] = ["Hindi", "Gujrati","English"]
        context["tech"] = ["PHP" ,"Laravel","Mysql","Oracle"]
        context["lang_rws"] = ['read','write','speak']

        return render(request, "create_view.html", context)
    else:
        return HttpResponseRedirect("/admin/")


#     ..............................List view...................................

def list_view(request):
    context={}
    context["cand"] = CandidateMaster.objects.all()
    context["acad"] = AcademicMaster.objects.all()
    context["expe"] = ExperienceMaster.objects.all()
    context["lang"] = LanguageKnownMaster.objects.all()
    context["tech"] = TechnologyKnownMaster.objects.all()
    context["refe"] = ReferenceMaster.objects.all()
    context["pref"] = PreferenceMaster.objects.all()

    return render(request,"list_view.html", context)




# ...........................Delete view.............................

def delete_view(request, id):
    context={}
    # obj = get_object_or_404(CandidateMaster, id=id)

    obj = CandidateMaster.objects.filter(id=id).first()

    print("deleted object//////", obj)
    if request.method == 'POST':
        print("Helloooo")
        obj.delete()
        print("deleted object..........", obj)
        return HttpResponseRedirect("/job/list/")
    return render(request,"delete_view.html",context)



# .................update view........................

def update_view(request,id):
    context={}
    obj_cand = CandidateMaster.objects.filter(id=id).first()
    obj_acad = AcademicMaster.objects.filter(candidate=obj_cand).first()
    obj_expe = ExperienceMaster.objects.filter(candidate=obj_cand).first()
    obj_lang = LanguageKnownMaster.objects.filter(candidate=obj_cand).first()
    obj_tech = TechnologyKnownMaster.objects.filter(candidate=obj_cand).first()
    obj_refe = ReferenceMaster.objects.filter(candidate=obj_cand).first()
    obj_pref = PreferenceMaster.objects.filter(candidate=obj_cand).first()


    print("updated value language object.....", obj_lang.language,obj_lang.read,obj_lang.write, obj_lang.speak)
    print("updated value  technology object.....", obj_tech.technology,  obj_tech.ranting)




    form = CandidateMasterForm(request.POST or None, instance=obj_cand)
    form_acade = AcademicMasterForm(request.POST or None, instance=obj_acad)
    form_exper = ExperienceMasterForm(request.POST or None, instance=obj_expe)
    form_langu = LanguageKnownMasterForm(request.POST or None, instance=obj_lang)
    form_techn = TechnologyKnownMasterModelForm(request.POST or None, instance=obj_tech)
    form_refer = ReferenceMasterForm(request.POST or None, instance=obj_refe)
    form_prefe = PreferenceMasterForm(request.POST or None, instance=obj_pref)

    if form.is_valid() and form_acade.is_valid() and form_exper.is_valid() and form_refer.is_valid() and form_prefe.is_valid():
        form.save()
        form_acade.save()
        form_exper.save()
        # form_langu.save()
        # form_techn.save()
        form_refer.save()
        form_prefe.save()

        profile = form_langu.save(commit=False)


        if "Hindi" in request.POST:
            if "Hindiread" in request.POST:
                profile.language = "Hindi"
                profile.read = True
                profile.write = False
                profile.speak = False

            if "Hindiwrite" in request.POST:
                profile.language = "Hindi"
                profile.write = True
                profile.read = False
                profile.speak = False

            if "Hindispeak" in request.POST:
                profile.language = "Hindi"
                profile.speak = True
                profile.write = False
                profile.read = False

        if "Gujrati" in request.POST:
            if "Gujratiread" in request.POST:
                profile.language = "Gujrati"
                profile.read = True
                profile.write = False
                profile.speak = False

            if "Gujratiwrite" in request.POST:
                profile.language = "Gujrati"
                profile.write = True
                profile.read = False
                profile.speak = False

            if "Gujratispeak" in request.POST:
                profile.language = "Gujrati"
                profile.speak = True
                profile.write = False
                profile.read = False

        if "English" in request.POST:
            if "Englishread" in request.POST:
                profile.language = "English"
                profile.read = True
                profile.write = False
                profile.speak = False

            if "Englishwrite" in request.POST:
                profile.language = "English"
                profile.write = True
                profile.read = False
                profile.speak = False

            if "Englishspeak" in request.POST:
                profile.language = "English"
                profile.speak = True
                profile.write = False
                profile.read = False

        profile.save()

        profile = form_techn.save(commit=False)


        if 'PHP' in request.POST:
            php = request.POST['PHPradio']
            if php == "begginer":
                profile.technology = 'PHP'
                profile.ranting = 3

            elif php == "mediator":
                profile.technology = 'PHP'
                profile.ranting = 6

            elif php == "expert":
                profile.technology = 'PHP'
                profile.ranting = 10

            else:
                profile.technology = 'PHP'
                profile.ranting = 3

        if 'Laravel' in request.POST:
            laravel = request.POST['Laravelradio']
            if laravel == "begginer":
                profile.technology = 'Laravel'
                profile.ranting = 3

            elif laravel == "mediator":
                profile.technology = 'Laravel'
                profile.ranting = 6

            elif laravel == "expert":
                profile.technology = 'Laravel'
                profile.ranting = 10

            else:
                profile.technology = 'Laravel'
                profile.ranting = 3

        if 'Mysql' in request.POST:
            mysql = request.POST['Mysql']
            if mysql == "begginer":
                profile.technology = 'Mysql'
                profile.ranting = 3

            elif mysql == "mediator":
                profile.technology = 'Mysql'
                profile.ranting = 6

            elif mysql == "expert":
                profile.technology = 'Mysql'
                profile.ranting = 10

            else:
                profile.technology = 'Mysql'
                profile.ranting = 3

        if 'Oracle' in request.POST:
            oracle = request.POST['Oracle']
            if oracle == "begginer":
                profile.technology = 'Oracle'
                profile.ranting = 3

            elif oracle == "mediator":
                profile.technology = 'Oracle'
                profile.ranting = 6

            elif oracle == "expert":
                profile.technology = 'Oracle'
                profile.ranting = 10

            else:
                profile.technology = 'Oracle'
                profile.ranting = 3
        profile.save()

        return HttpResponseRedirect("/job/list/")

    context["form"] = form
    context["form_acade"] = form_acade
    context["form_exper"] = form_exper
    context["form_langu"] = form_langu
    context["form_techn"] = form_techn
    context["form_refer"] = form_refer
    context["form_prefe"] = form_prefe
    context["data"] = ["Hindi", "Gujrati", "English"]
    context["lang_selected"] = obj_lang.language
    context["tech_selected"] = obj_tech.technology
    context["rating"] =obj_tech.ranting
    context["readed"] = obj_lang.read
    context["writed"] = obj_lang.write
    context["speaked"] = obj_lang.speak
    context["tech"] = ["PHP", "Laravel", "Mysql", "Oracle"]
    context["lang_rws"] = ['read', 'write', 'speak']

    return render(request, "update_view.html", context)




















# from django.shortcuts import get_object_or_404
#
# def fir_create(request,id=None):
#     if id is not None:
#         complaint = get_object_or_404(Complaint, id=id)
#     else:
#         complaint = None
#     form =FirForm(request.POST or None)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.complaint = complaint
#         instance.save()


# def create_view_academic(request, id):
#     if request.user.is_superuser:
#         print("idddddddd..................................", id)
#
#         # if id is not None:
#         #     candidate= get_object_or_404(CandidateMaster, pk=id)
#         # else:
#         #     candidate= None
#         candidate_var = CandidateMaster.objects.get(pk=id)
#
#         context = {}
#         form = AcademicMasterForm(request.POST or None)
#         if form.is_valid():
#
#             print("/./././././/../.", candidate_var, candidate_var.id)
#
#             profile = form.save(commit=False)
#
#             profile.candidate = candidate_var
#
#             print("/./././././/../.", profile, profile.candidate, candidate_var, candidate_var.id)
#             profile.save()
#             # form.save()
#             return HttpResponseRedirect("/job/create_experience/" + str(id) + "/")
#         context["form"] = form
#         return render(request, "create_view_academic.html", context)
#
#     else:
#         return HttpResponseRedirect("/admin/")
#
#
#
#
# def create_view_experience(request,id):
#     if request.user.is_superuser:
#         candidate_var = CandidateMaster.objects.get(pk=id)
#         context ={}
#         form = ExperienceMasterForm(request.POST or None)
#         print("Form data.....", form,"....",id)
#         if form.is_valid():
#             print("IF CONDITION IS TRUE HERE......")
#             profile = form.save(commit=False)
#             profile.candidate = candidate_var
#             profile.save()
#             return HttpResponseRedirect("/job/success/")
#         context["form"] = form
#         return render(request, "create_view.html", context)
#
#     else:
#         return HttpResponseRedirect("/admin/")




def success_view(request):
    return render(request, "success.html")

# class CreateViewClass(CreateView):
#     model = CandidateMaster
#     fields = [
#         'fname',
#         'lname',
#         'surname',
#         'contact_no',
#         'city',
#         'state',
#         'email',
#         'gender',
#         'dob'
#     ]
