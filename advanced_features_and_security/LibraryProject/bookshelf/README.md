Managing Permission and Group in Django
Creating and Configure Group with Assigned Persmissioins:
The application has the following groups:

Editors Group:
Editors have can_edit and can_create permissions

Viewers Group:
Viewers have can_view permission only

Admins Group:
Admins have can_create, can_edit and can_view permissions

Enforncing persmissions:
We enforce the permissions using the @permission_required(bookshelf.permission, raise_exception=True) decorator