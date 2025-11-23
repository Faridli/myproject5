from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from tasks.models import ForceMember
from tasks.forms import ForceModelForm,CompanySelectForm, PresentModelForm, PermanentModelForm
from django.db.models import Count, Prefetch, Q


# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------
def Dashboard(request):
   
    return render(request, 'dashboard/dashboard.html')

# ---------------------------------------------------
# Bn HQ
# ---------------------------------------------------
def Br(request):
    return render(request, 'bnhq/list.html')
# ---------------------------------------------------
# Force Bio Data Entry 
# ---------------------------------------------------
def Force_bio(request):
    if request.method == 'POST':
        force_form = ForceModelForm(request.POST)
        present_form = PresentModelForm(request.POST)
        permanent_form = PermanentModelForm(request.POST)

        # Form validation
        if force_form.is_valid() and present_form.is_valid() and permanent_form.is_valid():
            # Save ForceMember
            force = force_form.save()
            # force.company.add(Company.objects.get(id=1))

            # Save PresentAddress
            present = present_form.save(commit=False)
            present.member = force
            present.save()

            # Save PermanentAddress
            permanent = permanent_form.save(commit=False)
            permanent.member = force
            permanent.save()

            # Success message
            messages.success(request, "saved successfully!")
            return redirect('force-bio')

        else:
            # Debug: print form errors to console
            messages.error(request, "Please fix the errors!")
            print("errors:", force_form.errors)
            print("errors:", present_form.errors)
            print("errors:", permanent_form.errors)

    else:
        force_form = ForceModelForm()
        present_form = PresentModelForm()
        permanent_form = PermanentModelForm()

    context = {
        'force_form': force_form,
        'present_form': present_form,
        'permanent_form': permanent_form,
    }
    return render(request, 'dashboard/bio.html', context)

# ---------------------------------------------------
# 
# ---------------------------------------------------
# views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

def Force_detail(request):
    members = ForceMember.objects.all().select_related(
        'present_address', 'permanent_address'
    )

    # Handle AJAX POST
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        member = get_object_or_404(ForceMember, id=member_id)

        form = CompanySelectForm(request.POST, instance=member)

        if form.is_valid():
            form.save()

            # AJAX request → return JSON
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "company_name": member.company  # updated value
                })

            return redirect("force-detail")

        else:
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({"success": False})

    # For GET request → load table
    forms_dict = {m.id: CompanySelectForm(instance=m) for m in members}

    return render(request, "bnhq/force_detail.html", {
        "members": members,
        "forms_dict": forms_dict,
    })


#.......................
# Address................
# ....................... 

def Address(request, member_id):
    m = get_object_or_404(ForceMember, id=member_id)

    context = {
        "m": m,
        "present_dict": {
            "House": m.present_address.house,
            "Road": m.present_address.road,
            "Sector": m.present_address.sector,
            "Village": m.present_address.village,
            "Post": m.present_address.post,
            "District": m.present_address.district,
        },
        "permanent_dict": {
            "House": m.permanent_address.house,
            "Road": m.permanent_address.road,
            "Sector": m.permanent_address.sector,
            "Village": m.permanent_address.village,
            "Post": m.permanent_address.post,
            "District": m.permanent_address.district,
        },
        "service_dict": {
            "Svc Join": m.svc_join,
            "RAB Join": m.rab_join, 
            "Mother_unit":m.mother_unit,
            "NID": m.nid,
            "Birth Day": m.birth_day,
            "WF Phone": m.wf_phone,
        },
    }
    return render(request, "bnhq/address.html", context)







