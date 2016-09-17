from django.http import JsonResponse


def login_success(msg):
    resp = {
        'meta': {
            'code': 200,
            'message': msg
        }
    }
    return JsonResponse(resp)


def login_fail(msg):
    resp = {
        'meta': {
            'code': 401,
            'message': msg
        }
    }
    return JsonResponse(resp)


def add_success(msg):
    resp = {
        'meta': {
            'code': 201,
            'message': msg
        }
    }
    return JsonResponse(resp)


def add_fail(msg):
    resp = {
        'meta': {
            'code': 400,
            'message': msg
        }
    }
    return JsonResponse(resp)


def update_success(msg):
    resp = {
        'meta': {
            'code': 201,
            'message': msg
        }
    }
    return JsonResponse(resp)


def update_fail(msg):
    resp = {
        'meta': {
            'code': 400,
            'message': msg
        }
    }
    return JsonResponse(resp)


def find_success(data):
    resp = {
        'meta': {
            'code': 200
        },
        'data': data
    }
    return JsonResponse(resp)


def register_success(msg):
    resp = {
        'meta': {
            'code': 200,
            'message': msg
        }
    }
    return JsonResponse(resp)


def register_fail(msg):
    resp = {
        'meta': {
            'code': 401,
            'message': msg
        }
    }
    return JsonResponse(resp)


def delete_success(msg):
    resp = {
        'meta': {
            'code': 200,
            'message': msg
        }
    }
    return JsonResponse(resp)


def delete_fail(msg):
    resp = {
        'meta': {
            'code': 401,
            'message': msg
        }
    }
    return JsonResponse(resp)


def get_student_info(student):
    resp = {
        'name': student.name,
        'student_id': student.student_id,
        'gender': student.gender,
        'grade': student.grade,
        'photo': student.photo
    }
    return resp
