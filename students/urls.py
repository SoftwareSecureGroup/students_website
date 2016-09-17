# coding=utf-8
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.index),
    url(r'^index.html$', views.index),
    # 注册页面
    url(r'^register$', views.register),
    # 登陆界面
    url(r'^login.html$', views.login),
    url(r'^logout.html$', views.logout),
    # 添加学生信息
    url(r'^add$', views.add),

    # 列出第几页的学生信息
    url(r'^detail$', views.detail),
    url(r'^user_index.html$', views.detail),
    url(r'^admin_index.html$', views.detail),
    url(r'^students/(?P<page_no>[0-9]+)$', views.detail, name='detail'),
    # 添加学生信息
    url(r'^students/add$', views.add),
    # 更新学生信息
    url(r'^update$', views.update),
    # 删除学生信息
    url(r'^delete$', views.delete),

    url(r'^user_edit.html$', views.user_edit),

    url(r'^about.html$', views.about),

    url(r'^help.html$', views.help),

    url(r'^admin_edit_oringal.html', views.admin_edit),

    url(r'^reset_password.html$', views.reset_password),

    url(r'^error_page$', views.error_page),

    url(r'^user_info$', views.user_info),

]  # + static(settings.MEDIA_URL)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
