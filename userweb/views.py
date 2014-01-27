from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
)


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'userweb'}

@view_config(route_name='login', renderer='templates/mytemplate.pt')
def login(request):
    login = 'rhintz42'
    headers = remember(request, login)

    return HTTPFound(location=route_url('user', request), headers=headers)

@view_config(route_name='logout', renderer='templates/mytemplate.pt')
def logout(request):
    headers = forget(request)

    return HTTPFound(location=route_url('user', request), headers=headers)

@view_config(route_name='user', renderer='templates/mytemplate.pt')
def user(request):
    a = authenticated_userid(request)
    return {'project': a}
