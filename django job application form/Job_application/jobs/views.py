# from django.core.serializers import json
import json

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.core.paginator import Paginator
from django.template.defaulttags import register

# Create your views here.


from django.views.generic.edit import CreateView
from .models import CandidateMaster, AcademicMaster, ExperienceMaster, LanguageKnownMaster, TechnologyKnownMaster, \
    ReferenceMaster, PreferenceMaster
# from .forms import CandidateMasterForm
from .forms import CandidateMasterForm, AcademicMasterForm, ExperienceMasterForm, LanguageKnownMasterForm, \
    TechnologyKnownMasterForm, TechnologyKnownMasterModelForm, ReferenceMasterForm, PreferenceMasterForm


def create_view(request):

        context = {}
        form = CandidateMasterForm(request.POST or None)
        # form_acade= AcademicMasterForm(request.POST or None)
        form_exper = ExperienceMasterForm(request.POST or None)
        form_langu = LanguageKnownMasterForm(request.POST or None)
        form_refer = ReferenceMasterForm(request.POST or None)
        form_prefe = PreferenceMasterForm(request.POST or None)
        form_techn = TechnologyKnownMasterForm(request.POST or None)
        form_techn_model = TechnologyKnownMasterModelForm(request.POST or None)

        if form.is_valid() and form_exper.is_valid() and form_refer.is_valid() and form_prefe.is_valid():
            intance = form.save(commit=True)

            intance.save()

            for i in range(len(request.POST.getlist("course_name"))):
                AcademicMaster.objects.create(candidate=intance,
                                              name_of_board_university=request.POST.getlist("name_of_board_university")[
                                                  i],
                                              passing_year=request.POST.getlist("passing_year")[i],
                                              course_name=request.POST.getlist("course_name")[i],
                                              percentage=request.POST.getlist("percentage")[i]).save()



            for i in range(len(request.POST.getlist("company_name"))):
                ExperienceMaster.objects.create(candidate=intance, company_name=request.POST.getlist("company_name")[i],
                                                designation=request.POST.getlist("designation")[i],
                                                from_date=request.POST.getlist("from_date")[i],
                                                to_date=request.POST.getlist("to_date")[i]).save()

            # ........


            if "Hindi" in request.POST:
                lang_name = "Hindi"
                lang_read = True if "Hindiread" in request.POST else False
                lang_write = True if "Hindiwrite" in request.POST else False
                lang_speak = True if "Hindispeak" in request.POST else False
                LanguageKnownMaster.objects.create(candidate=intance, language=lang_name, read=lang_read,
                                                   write=lang_write,
                                                   speak=lang_speak).save()

            if "Gujrati" in request.POST:
                lang_name = "Gujrati"
                lang_read = True if "Gujratiread" in request.POST else False
                lang_write = True if "Gujratiwrite" in request.POST else False
                lang_speak = True if "Gujratispeak" in request.POST else False
                LanguageKnownMaster.objects.create(candidate=intance, language=lang_name, read=lang_read,
                                                   write=lang_write,
                                                   speak=lang_speak).save()

            if "English" in request.POST:
                lang_name = "English"
                lang_read = True if "Englishread" in request.POST else False
                lang_write = True if "Englishwrite" in request.POST else False
                lang_speak = True if "Englishspeak" in request.POST else False
                LanguageKnownMaster.objects.create(candidate=intance, language=lang_name, read=lang_read,
                                                   write=lang_write,
                                                   speak=lang_speak).save()

            if 'PHP' in request.POST:
                tech_name = "PHP"
                tech_rating = 0
                php = request.POST['PHPradio']
                if php == "begginer":
                    tech_rating = 3
                elif php == "mediator":
                    tech_rating = 6
                elif php == "expert":
                    tech_rating = 10

                TechnologyKnownMaster.objects.create(candidate=intance, technology=tech_name,
                                                     ranting=tech_rating).save()

            if 'Laravel' in request.POST:
                tech_name = "Laravel"
                tech_rating = 0
                Laravel = request.POST['Laravelradio']
                if Laravel == "begginer":
                    tech_rating = 3
                elif Laravel == "mediator":
                    tech_rating = 6
                elif Laravel == "expert":
                    tech_rating = 10

                TechnologyKnownMaster.objects.create(candidate=intance, technology=tech_name,
                                                     ranting=tech_rating).save()

            if 'Mysql' in request.POST:
                tech_name = "Mysql"
                tech_rating = 0
                Mysql = request.POST['Mysqlradio']
                if Mysql == "begginer":
                    tech_rating = 3
                elif Mysql == "mediator":
                    tech_rating = 6
                elif Mysql == "expert":
                    tech_rating = 10

                TechnologyKnownMaster.objects.create(candidate=intance, technology=tech_name,
                                                     ranting=tech_rating).save()

            if 'Oracle' in request.POST:
                tech_name = "Oracle"
                tech_rating = 0
                Oracle = request.POST['Oracleradio']
                if Oracle == "begginer":
                    tech_rating = 3
                elif Oracle == "mediator":
                    tech_rating = 6
                elif Oracle == "expert":
                    tech_rating = 10

                TechnologyKnownMaster.objects.create(candidate=intance, technology=tech_name,
                                                     ranting=tech_rating).save()

            # .........



            for i in range(len(request.POST.getlist("refe_name"))):
                ReferenceMaster.objects.create(candidate=intance, refe_name=request.POST.getlist("refe_name")[i],
                                               refe_contact_no=request.POST.getlist("refe_contact_no")[i],
                                               refe_relation=request.POST.getlist("refe_relation")[i]).save()

            # ........
            profile = form_prefe.save(commit=False)
            profile.candidate = intance
            profile.save()

            return HttpResponseRedirect("/job/success/")

        context["form"] = form
        # context["form_acade"] = form_acade
        context["form_exper"] = form_exper
        context["form_langu"] = form_langu
        context["form_techn"] = form_techn
        context["form_refer"] = form_refer
        context["form_prefe"] = form_prefe
        context["data"] = ["Hindi", "Gujrati", "English"]
        context["tech"] = ["PHP", "Laravel", "Mysql", "Oracle"]
        context["lang_rws"] = ['read', 'write', 'speak']
        return render(request, "create_view.html", context)



#     ..............................List view...................................


def list_view(request):
    context = {}
    if request.GET:
        if "search" in request.GET:
            search = request.GET.get("search")
            print("search value///////", search)
            obj_cand = CandidateMaster.objects.filter(Q(fname__icontains=search) | Q(lname__icontains=search) |
                                                      Q(surname__icontains=search) | Q(contact_no__icontains=search) |
                                                      Q(city__icontains=search) | Q(state__icontains=search) |
                                                      Q(email__icontains=search) | Q(gender__icontains=search) |
                                                      Q(dob__icontains=search))
            context["cand"] = obj_cand
            context["sort"] = "ASC"

        elif "field" in request.GET:
            field = request.GET.get("field")
            sort = request.GET.get("sort")
            print("search value///////", field)
            if sort == "ASC":
                obj_cand = CandidateMaster.objects.all().order_by(field).values()
                context["cand"] = obj_cand
                context["sort"] = "DESC"

            else:
                obj_cand = CandidateMaster.objects.all().order_by("-" + field).values()
                context["cand"] = obj_cand
                context["sort"] = "ASC"




    else:
        context["cand"] = CandidateMaster.objects.all()
        context["sort"] = "ASC"
        context["acad"] = AcademicMaster.objects.all()


    return render(request, "list_view.html", context)


# .................................pagination view.........................
def pagination_view(request):
    context = {}
    obj_cand = CandidateMaster.objects.all()
    p = Paginator(obj_cand, 5)
    page_no = request.GET.get("page")
    no_of_pages = p.num_pages
    lst = list(range(1, no_of_pages + 1))
    print("no of pages??????", no_of_pages, lst)
    try:
        obj_page = p.get_page(page_no)
    except:
        obj_page = p.page(1)

    context["obj_page"] = obj_page
    context["no_of_pages"] = lst
    return render(request, "pagination_view.html", context)



# ...........................Delete view.............................

def delete_view(request, id):
    context = {}
    # obj = get_object_or_404(CandidateMaster, id=id)

    obj = CandidateMaster.objects.filter(id=id).first()

    print("deleted object//////", obj)
    if request.method == 'POST':
        print("Helloooo")
        obj.delete()
        print("deleted object..........", obj)
        return HttpResponseRedirect("/job/list/")
    return render(request, "delete_view.html", context)


# .................update view........................

def update_view(request, id):
    context = {}
    obj_cand = CandidateMaster.objects.filter(id=id).first()

    obj_acad_first = AcademicMaster.objects.filter(candidate=obj_cand).first()
    obj_acad_all = AcademicMaster.objects.filter(candidate=obj_cand).order_by('id')
    obj_acad = obj_acad_all[1:]


    obj_expe_first = ExperienceMaster.objects.filter(candidate=obj_cand).first()
    obj_expe_all = ExperienceMaster.objects.filter(candidate=obj_cand).order_by('id')
    obj_expe = obj_expe_all[1:]


    print("object:::::", obj_cand)
    print("object acade first:::::", obj_acad_first)
    print("object acade all :::::", obj_acad_all)
    print("object acade remaining  all :::::", obj_acad)
    print("object fisrt:::::", obj_expe_first)
    print("object fisrt:::::", obj_expe_all)
    print("object all:::::", obj_expe)
    print("object remaining all :::::", obj_expe)

    val = LanguageKnownMaster.objects.filter(candidate=obj_cand).values()
    obj_lang = list(val)
    main_list=[]
    for i in range(len(obj_lang)):
        lst = {}

        lst['language'] = obj_lang[i]['language']
        print("//////////////////////////////",lst['language'])
        lst['read'] = 'false' if obj_lang[i]['read'] == False else 'true'
        lst['write'] = 'false' if obj_lang[i]['write'] == False else 'true'
        lst['speak'] = 'false' if obj_lang[i]['speak'] == False else 'true'

        main_list.append(lst)



    print("_________________________________", obj_lang[0]['language'])
    print("_________________________________", main_list)



    val = TechnologyKnownMaster.objects.filter(candidate=obj_cand).values()
    obj_tech = list(val)
    print("_________________________________", obj_tech[0]['technology'])
    print("object:::::", obj_tech)

    obj_refe_first = ReferenceMaster.objects.filter(candidate=obj_cand).first()
    obj_refe_all = ReferenceMaster.objects.filter(candidate=obj_cand).order_by('id')
    obj_refe = obj_refe_all[1:]

    print("object fisrt:::::", obj_refe_first)
    print("object all:::::", obj_refe_all)
    print("object remaining all :::::", obj_refe)

    obj_pref = PreferenceMaster.objects.filter(candidate=obj_cand).first()

    print("object:::::", obj_pref)

    print("whole object:::", LanguageKnownMaster.objects.all().filter(candidate=obj_cand))
    # print("updated value language object.....", obj_lang.language,obj_lang.read,obj_lang.write, obj_lang.speak)
    # print("updated value  technology object.....", obj_tech.technology,  obj_tech.ranting)

    form = CandidateMasterForm(request.POST or None, instance=obj_cand)
    form_acade = AcademicMasterForm(request.POST or None)
    form_exper = ExperienceMasterForm(request.POST or None)
    form_langu = LanguageKnownMasterForm(request.POST or None)
    form_techn = TechnologyKnownMasterModelForm(request.POST or None)
    form_refer = ReferenceMasterForm(request.POST or None)
    form_prefe = PreferenceMasterForm(request.POST or None, instance=obj_pref)

    if form.is_valid() and form_acade.is_valid() and form_exper.is_valid() and form_refer.is_valid() and form_prefe.is_valid():
        form.save()
        form_prefe.save()


        len_of_already = len(AcademicMaster.objects.filter(candidate=obj_cand))
        len_of_getting = len(request.POST.getlist("course_name"))

        if len_of_already == len_of_getting:
            obj = AcademicMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)
            print(" first condition is true here.......................")
            for i in range(len_of_already):
                id = obj[i].id
                print("///////", obj, obj[i], i, id)

                obj_acad = AcademicMaster.objects.filter(id=id).first()
                print("///////", obj_acad)
                # obj_acad.candidate = obj_cand
                obj_acad.course_name = request.POST.getlist("course_name")[i]
                obj_acad.name_of_board_university = request.POST.getlist("name_of_board_university")[i]
                obj_acad.passing_year = request.POST.getlist("passing_year")[i]
                obj_acad.percentage = request.POST.getlist("percentage")[i]
                obj_acad.save()

        elif len_of_already > len_of_getting:
            print("second condition is true here.......................")
            obj = AcademicMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_getting):
                id = obj[i].id

                obj_acad = AcademicMaster.objects.filter(id=id).first()
                print("///////", obj_acad)
                # obj_acad.candidate = obj_cand
                obj_acad.course_name = request.POST.getlist("course_name")[i]
                obj_acad.name_of_board_university = request.POST.getlist("name_of_board_university")[i]
                obj_acad.passing_year = request.POST.getlist("passing_year")[i]
                obj_acad.percentage = request.POST.getlist("percentage")[i]
                obj_acad.save()

            for i in range(len_of_getting, len_of_already - len_of_getting + 1):
                id = obj[i].id
                obj_acad = AcademicMaster.objects.filter(id=id)
                obj_acad[0].delete()

        elif len_of_already < len_of_getting:
            print(" third condition is true here.......................")
            obj = AcademicMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_already):
                id = obj[i].id
                obj_acad = AcademicMaster.objects.filter(id=id).first()

                # obj_acad.candidate = obj_cand
                obj_acad.course_name = request.POST.getlist("course_name")[i]
                obj_acad.name_of_board_university = request.POST.getlist("name_of_board_university")[i]
                obj_acad.passing_year = request.POST.getlist("passing_year")[i]
                obj_acad.percentage = request.POST.getlist("percentage")[i]
                obj_acad.save()



            for i in range(len_of_already, len_of_getting - len_of_already + 1):

                AcademicMaster.objects.create(candidate=obj_cand,
                                              name_of_board_university=request.POST.getlist("name_of_board_university")[
                                                  i],
                                              passing_year=request.POST.getlist("passing_year")[i],
                                              course_name=request.POST.getlist("course_name")[i],
                                              percentage=request.POST.getlist("percentage")[i]).save()



        len_of_already = len(ExperienceMaster.objects.filter(candidate=obj_cand))
        len_of_getting = len(request.POST.getlist("company_name"))

        if len_of_already == len_of_getting:
            obj = ExperienceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)
            print(" first condition is true here.......................")
            for i in range(len_of_already):
                id = obj[i].id
                print("///////", obj, obj[i], i, id)

                obj_expe = ExperienceMaster.objects.filter(id=id).first()
                print("///////", obj_expe)
                # obj_acad.candidate = obj_cand
                obj_expe.company_name = request.POST.getlist("company_name")[i]
                obj_expe.designation = request.POST.getlist("designation")[i]
                obj_expe.from_date = request.POST.getlist("from_date")[i]
                obj_expe.to_date = request.POST.getlist("to_date")[i]
                obj_expe.save()



        elif len_of_already > len_of_getting:
            print("second condition is true here.......................")
            obj = ExperienceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_getting):
                id = obj[i].id

                obj_expe = ExperienceMaster.objects.filter(id=id).first()
                print("///////", obj_acad)

                obj_expe.company_name = request.POST.getlist("company_name")[i]
                obj_expe.designation = request.POST.getlist("designation")[i]
                obj_expe.from_date = request.POST.getlist("from_date")[i]
                obj_expe.to_date = request.POST.getlist("to_date")[i]
                obj_expe.save()
                # obj_acad.candidate = obj_cand

            for i in range(len_of_getting, len_of_already - len_of_getting + 1):
                id = obj[i].id
                obj_expe = ExperienceMaster.objects.filter(id=id)
                obj_expe[0].delete()



        elif len_of_already < len_of_getting:
            print(" third condition is true here.......................")
            obj = ExperienceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_already):
                id = obj[i].id
                obj_expe = ExperienceMaster.objects.filter(id=id).first()

                print("@@@@@@@@@@@@@@@@", obj, id)

                # obj_acad.candidate = obj_cand
                obj_expe.company_name = request.POST.getlist("company_name")[i]
                obj_expe.designation = request.POST.getlist("designation")[i]
                obj_expe.from_date = request.POST.getlist("from_date")[i]
                obj_expe.to_date = request.POST.getlist("to_date")[i]
                obj_expe.save()



            for i in range(len_of_already, len_of_getting - len_of_already + 1):

                ExperienceMaster.objects.create(candidate=obj_cand,
                                                company_name=request.POST.getlist("company_name")[i],
                                                designation=request.POST.getlist("designation")[i],
                                                from_date=request.POST.getlist("from_date")[i],
                                                to_date=request.POST.getlist("to_date")[i]).save()



        len_of_already = len(LanguageKnownMaster.objects.filter(candidate=obj_cand))
        obj = LanguageKnownMaster.objects.filter(candidate=obj_cand)
        obj = list(obj)

        lst_lang= ["Hindi", "Gujrati", "English"]

        for i in range(len_of_already):
            id = obj[i].id
            obj_lang = LanguageKnownMaster.objects.filter(id=id).first()
            for lang in lst_lang:
                if lang in request.POST and obj_lang.language == lang:
                    lang_read = True if lang+"read" in request.POST else False
                    lang_write = True if lang+"write" in request.POST else False
                    lang_speak = True if lang+"speak" in request.POST else False
                    obj_lang.language = lang
                    obj_lang.read = lang_read
                    obj_lang.write = lang_write
                    obj_lang.speak = lang_speak
                    obj_lang.save()

                elif lang in request.POST and obj_lang.language != lang:
                    lang_read = True if lang + "read" in request.POST else False
                    lang_write = True if lang + "write" in request.POST else False
                    lang_speak = True if lang + "speak" in request.POST else False
                    LanguageKnownMaster.objects.create(candidate=obj_cand,
                                                    language=lang,
                                                    read=lang_read,
                                                    write=lang_write,
                                                    speak=lang_speak).save()
                elif lang not in request.POST and obj_lang.language == lang:
                    obj_lang.delete()

        len_of_already = len(TechnologyKnownMaster.objects.filter(candidate=obj_cand))
        obj = TechnologyKnownMaster.objects.filter(candidate=obj_cand)
        obj = list(obj)


        lst_tech=["PHP", "Laravel", "Mysql", "Oracle"]

        for i in range(len_of_already):
            id = obj[i].id
            obj_tech = TechnologyKnownMaster.objects.filter(id=id).first()
            for tech in lst_tech:
                if tech in request.POST and obj_tech.technology == tech:
                    tech_name = tech
                    tech_rating = 0
                    rating = request.POST[tech+'radio']
                    if rating == "begginer":
                        tech_rating = 3
                    elif rating == "mediator":
                        tech_rating = 6
                    elif rating == "expert":
                        tech_rating = 10


                    obj_tech.technology = tech_name
                    obj_tech.ranting = tech_rating
                    obj_tech.save()

                elif tech in request.POST and obj_tech.technology != tech:
                    tech_name = tech
                    tech_rating = 0
                    rating = request.POST[tech+'radio']
                    if rating == "begginer":
                        tech_rating = 3
                    elif rating == "mediator":
                        tech_rating = 6
                    elif rating == "expert":
                        tech_rating = 10
                    TechnologyKnownMaster.objects.create(candidate=obj_cand, technology=tech_name,
                                                             ranting=tech_rating).save()



                elif tech not in request.POST and obj_tech.technology == tech:
                    obj_tech.delete()



        len_of_already = len(ReferenceMaster.objects.filter(candidate=obj_cand))
        len_of_getting = len(request.POST.getlist("refe_name"))

        if len_of_already == len_of_getting:
            obj = ReferenceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)
            print(" first condition is true here.......................")
            for i in range(len_of_already):
                id = obj[i].id
                print("///////", obj, obj[i], i, id)

                obj_refe = ReferenceMaster.objects.filter(id=id).first()
                print("///////", obj_expe)
                # obj_acad.candidate = obj_cand
                obj_refe.refe_name = request.POST.getlist("refe_name")[i]
                obj_refe.refe_contact_no = request.POST.getlist("refe_contact_no")[i]
                obj_refe.refe_relation = request.POST.getlist("refe_relation")[i]
                obj_refe.save()



        elif len_of_already > len_of_getting:
            print("second condition is true here.......................")
            obj = ReferenceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_getting):
                id = obj[i].id

                obj_refe = ReferenceMaster.objects.filter(id=id).first()
                print("///////", obj_expe)
                # obj_acad.candidate = obj_cand
                obj_refe.refe_name = request.POST.getlist("refe_name")[i]
                obj_refe.refe_contact_no = request.POST.getlist("refe_contact_no")[i]
                obj_refe.refe_relation = request.POST.getlist("refe_relation")[i]
                obj_refe.save()
                # obj_acad.candidate = obj_cand

            for i in range(len_of_getting, len_of_already - len_of_getting + 1):
                id = obj[i].id
                obj_refe = ReferenceMaster.objects.filter(id=id)
                obj_refe[0].delete()



        elif len_of_already < len_of_getting:
            print(" third condition is true here.......................")
            obj = ReferenceMaster.objects.filter(candidate=obj_cand)
            obj = list(obj)

            for i in range(len_of_already):
                id = obj[i].id
                obj_refe = ReferenceMaster.objects.filter(id=id).first()

                print("@@@@@@@@@@@@@@@@", obj, id)

                # obj_acad.candidate = obj_cand
                obj_refe.refe_name = request.POST.getlist("refe_name")[i]
                obj_refe.refe_contact_no = request.POST.getlist("refe_contact_no")[i]
                obj_refe.refe_relation = request.POST.getlist("refe_relation")[i]
                obj_refe.save()



            for i in range(len_of_already, len_of_getting - len_of_already + 1):
                print("third inside condition is true here.......................", i,
                      request.POST.getlist("passing_year")[i])

                ReferenceMaster.objects.create(candidate=obj_cand,
                                               refe_name=request.POST.getlist("refe_name")[i],
                                               refe_contact_no=request.POST.getlist("refe_contact_no")[i],
                                               refe_relation=request.POST.getlist("refe_relation")[i]).save()



        return HttpResponseRedirect("/job/list/")

    context["form"] = form
    context["obj_acad_first"] = obj_acad_first
    context["obj_acad"] = obj_acad
    context["obj_expe_first"] = obj_expe_first
    context["obj_expe"] = obj_expe
    context["obj_lang"] = main_list
    context["obj_tech"] = obj_tech
    context["obj_refe_first"] = obj_refe_first
    context["obj_refe"] = obj_refe
    context["form_prefe"] = form_prefe
    context["data"] = ["Hindi", "Gujrati", "English"]
    context["tech"] = ["PHP", "Laravel", "Mysql", "Oracle"]
    context["lang_rws"] = ['read', 'write', 'speak']

    return render(request, "update_view.html", context)



def success_view(request):
    return render(request, "success.html")

