from django.shortcuts import render
from django.http import HttpResponse

def input (req):
    data = {}
    if req.method == 'POST':
            name = req.POST['name']
            fname = req.POST['fname']
            contact_num = req.POST['contact_number']
            email = req.POST['email']
            linkdin = req.POST['linkdin']
            job_title = req.POST['job_title']
            address = req.POST['address']
            objective = req.POST['objective']
            institute = req.POST['institute']
            faculty = req.POST['faculty']
            start_date_edu = req.POST['start_date_edu']
            end_date_edu = req.POST['end_date_edu']
            details_edu = req.POST['details_edu']
            lang1 = req.POST['lang1']
            lang2 = req.POST['lang2']
            lang2 = req.POST['lang2']
            soft1 = req.POST['soft1']
            soft2 = req.POST['soft2']
            tech1 = req.POST['tech1']
            tech2 = req.POST['tech2']
            company_name = req.POST['company_name']
            job_title_2 = req.POST['job_title_2']
            start_date_train = req.POST['start_date_train']
            end_date_train = req.POST['end_date_train']
            details_train = req.POST['details_train']
            course_name = req.POST['course_name']
            course_provider = req.POST['course_provider']
            int1 = req.POST['int1']
            int2 = req.POST['int2']
            
            data = {
            'name': name,
            'fname': fname,
            'contact_num': contact_num,
            'email': email,
            'linkdin': linkdin,
            'job_title': job_title,
            'address': address,
            # 'nationality': nationality,
            # 'birthday': birthday,
            # 'blood_group': blood_group,
            'objective': objective,
            'institute': institute,
            'faculty': faculty,
            'start_date_edu': start_date_edu,
            'end_date_edu': end_date_edu,
            'details_edu': details_edu,
            'lang1': lang1,
            'lang2': lang2,
            'soft1': soft1,
            'soft2': soft2,
            'tech1': tech1,
            'tech2': tech2,
            'company_name': company_name,
            'job_title_2': job_title_2,
            'start_date_train': start_date_train,
            'end_date_train': end_date_train,
            'details_train': details_train,
            'course_name': course_name,
            'course_provider': course_provider,
            'int1': int1,
            'int2': int2
        }
            
    if 'btn' in req.POST:
            return render(req, 'cv.html', data)
    return render(req, 'input.html', data)
