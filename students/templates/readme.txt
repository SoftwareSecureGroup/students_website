登陆：
login.html:管理员/用户的登录页
index.html：管理员 / 用户登陆后，最先看到的欢迎页


查看（搜索）所有学生信息：
admin_index.html:管理员在这里查看所有学生
user_index.html：用户在这里查看所有学生，比admin_index只是少几个按钮


添加/编辑学生：
admin_edit.html：用于管理员添加新学生、编辑学生信息。用户不能访问


修改自己的信息（在导航栏的下拉框那儿）：
user_edit.html:用户跳转到这儿修改个人基本信息
admin_edit_myself.html：管理员跳转到这儿修改个人基本信息（和user_edit可以合并？）
reset_password.html: 管理员/用户在这里修改自己的密码


相关界面：
help.html：系统相关信息
about.html：开发者相关信息


错误页：
403，404，500，503


其他：
导航单独拿出来比较好，毕竟管理员和用户看到的是不一样的。
我没试 怕弄乱了
