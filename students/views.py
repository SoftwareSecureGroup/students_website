from hashlib import sha1

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from json_resp.response import *
from models import Admin, Student


def is_admin(request):
    if 'admin_id' in request.session:
        return True
    if 'student_id' in request.session:
        return False
    return None


def err_return(msg):
    return HttpResponseRedirect('error_page?msg=' + msg)


def index(request):
    if 'student_id' in request.session or 'admin_id' in request.session:
        context = {'is_admin': is_admin(request)}
        return render_to_response('index.html', context)
    else:
        return HttpResponseRedirect('login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        args = request.POST
        uuid = args['student_id']
        try:
            s = Student.objects.get(student_id=uuid)
        except Student.DoesNotExist:
            s = None

        if s is not None:
            return register_fail('This id has already registered')
        else:
            if args['name'] == '' or args['student_id'] == '' or \
                            args['grade'] == '' or args['gender'] == '' or \
                            args['password'] == '':
                return register_fail('Don\'t have enough information')

            s = Student()
            s.student_id = uuid
            s.name = args['name']
            s.gender = args['gender']
            s.grade = args['grade']
            s.photo = args['photo']
            s.password = hashlib.sha1(args['password']).hexdigest()
            s.save()
            return register_success('Register success')
    else:
        return render_to_response('register.html')


@csrf_exempt
def login(request):
    if 'student_id' in request.session:
        del request.session['student_id']
    if 'admin_id' in request.session:
        del request.session['admin_id']
    if request.method == 'POST':
        uuid = request.POST["student_id"]
        password = request.POST["password"]
        try:
            s = Student.objects.get(student_id=uuid)
            if s.password == sha1(password).hexdigest():
                request.session['student_id'] = uuid
                return HttpResponseRedirect('detail')
            else:
                return err_return('Login fail! Password is incorrect!')
        except Student.DoesNotExist:
            try:
                adm = Admin.objects.get(admin_id=uuid)
                if adm.password == sha1(password).hexdigest():
                    request.session['admin_id'] = uuid
                    return HttpResponseRedirect('detail')
            except Admin.DoesNotExist:
                return err_return('Login fail!')
            return err_return('Login fail! No such admin!')
    else:
        return render_to_response('login.html')


def logout(request):
    if 'student_id' in request.session:
        del request.session['student_id']
    if 'admin_id' in request.session:
        del request.session['admin_id']

    return HttpResponseRedirect('login.html')


def detail(request, page_no=1):
    if 'student_id' in request.session or 'admin_id' in request.session:
        student_list = Student.objects.all()
	if "search" in request.GET:
	    search = request.GET['search']
            student_list = Student.objects.filter(Q(student_id__icontains=search) | Q(name__icontains=search) | Q(gender__icontains=search) | Q(grade__icontains=search))
        paginator = Paginator(student_list, 10)
        try:
            students = paginator.page(page_no)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            students = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            students = paginator.page(paginator.num_pages)

        data = [get_student_info(s) for s in students]

        context = {'students': students}

        if is_admin(request):
            return render_to_response('admin_index.html', context)
        else:
            return render_to_response('user_index.html', context)

    else:
        return HttpResponseRedirect('login.html')


@csrf_exempt
def add(request):
    if request.method == 'POST':
        args = request.POST
        uuid = args['student_id']
        try:
            s = Student.objects.get(student_id=uuid)
        except Student.DoesNotExist:
            s = None

        if s is not None:
            return err_return('This id has already registered')
        else:
            if args['name'] == '' or args['student_id'] == '' or \
                            args['grade'] == '' or args['gender'] == '' or \
                            args['password'] == '':
                return err_return('Don\'t have enough information')

            s = Student()
            s.student_id = uuid
            s.name = args['name']
            s.gender = args['gender']
            s.grade = args['grade']
            if request.FILES.has_key('photo'):
                s.photo = request.FILES.get('photo')
            s.password = sha1(args['password']).hexdigest()
            s.save()
            return HttpResponseRedirect('admin_index.html')
    else:
        return render_to_response('register.html')


@csrf_exempt
def update(request):
    if 'student_id' in request.session or 'admin_id' in request.session:
        if request.method == 'POST':
            args = request.POST
            uuid = args['student_id']
            if uuid == '':
                return err_return('Update fail! No enough input')

            if 'student_id' in request.session and uuid != request.session['student_id']:
                return err_return('Update fail! You con\'t change the information of this student')

            try:
                s = Student.objects.get(student_id=uuid)

                if 'name' in args and args['name'] != "":
                    s.name = args['name']
                if 'gender' in args and args['gender'] != "":
                    s.gender = args['gender']
                if 'grade' in args and args['grade'] != "":
                    s.grade = args['grade']
                if request.FILES.has_key('photo'):
                    s.photo = request.FILES.get('photo')

                if 'password' in args and args['password'] is not '':
                    if 'admin_id' in request.session:
                        s.password = sha1(args['password']).hexdigest()
                    else:
                        return err_return('Please login as an admin!')

                s.save()
                return HttpResponseRedirect('user_index.html')
            except Student.DoesNotExist:
                return err_return('Update fail! No such student')
        else:
            return err_return('Update fail! No enough input')

    else:
        return err_return('You should login first')


@csrf_exempt
def delete(request):
    if 'admin_id' in request.session:

        if request.method == 'GET':
            uuid = request.GET['student_id']
            if uuid == "":
                return err_return('No enough input')

            try:
                s = Student.objects.get(student_id=uuid)
                s.delete()
                return delete_success('Delete Success')
            except Student.DoesNotExist:
                return err_return('No such student')

        else:
            return err_return('No enough input')

    else:
        return err_return('You should login first')


def user_edit(request):
    if "student_id" in request.session or "admin_id" in request.session:
        if is_admin(request):
            uuid = request.GET['student_id']
        else:
            uuid = request.session['student_id']
        try:
            s = Student.objects.get(student_id=uuid)
            context = {'student': s}
            if is_admin(request):
                return render_to_response('admin_edit.html', context)
            else:
                return render_to_response('user_edit.html', context)
        except Student.DoesNotExist:
            return err_return('No such student')
    else:
        return HttpResponseRedirect('login.html')

def user_info(request):
    if "student_id" in request.session or "admin_id" in request.session:
	uuid = request.GET['student_id']
        try:
            s = Student.objects.get(student_id=uuid)
            context = {'student': s, 'is_admin': is_admin(request)}
            return render_to_response('user_info.html', context)
        except Student.DoesNotExist:
            return err_return('No such student')
    else:
        return HttpResponseRedirect('login.html')

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        oringal_password = request.POST['oringal_password']
        new_password = request.POST['new_password']
        if 'student_id' in request.session:
            uuid = request.session['student_id']
            try:
                s = Student.objects.get(student_id=uuid)
                if s.password == sha1(oringal_password).hexdigest():
                    s.password = sha1(new_password).hexdigest()
                    s.save()
                    return HttpResponseRedirect('user_index.html')
                else:
                    return err_return("Password error!")
            except Student.DoesNotExist:
                return err_return("No such student!")

        elif 'admin_id' in request.session:
            uuid = request.session['admin_id']
            try:
                adm = Admin.objects.get(admin_id=uuid)
                if adm.password == sha1(oringal_password).hexdigest():
                    adm.password = sha1(new_password).hexdigest()
                    adm.save()
                    return HttpResponseRedirect('admin_index.html')
                else:
                    return err_return("Password error!")
            except Admin.DoesNotExist:
                return err_return("No such admin!")

    return render_to_response('reset_password.html')


def error_page(request):
    if request.method == 'GET':
        if 'msg' in request.GET:
            msg = request.GET['msg']
            context = {'msg': msg}
            return render_to_response('errors/404.html', context)
    else:
        pass


def about(request):
    if 'student_id' in request.session or 'admin_id' in request.session:
        context = {'is_admin': is_admin(request)}
        return render_to_response('about.html', context)
    else:
        return HttpResponseRedirect('login.html')


def help(request):
    if 'student_id' in request.session or 'admin_id' in request.session:
        context = {'is_admin': is_admin(request)}
        return render_to_response('help.html', context)
    else:
        return HttpResponseRedirect('login.html')


def admin_edit(request):
    return render_to_response('admin_edit_oringal.html')
