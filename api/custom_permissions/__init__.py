from .basic_access_permission import BasicAccessPermission
from .is_admin import IsAdminRoleOrSuperuser
from .is_author_or_higher import IsAuthorOrHigherOrReadOnly

__all__ = [
    'BasicAccessPermission',
    'IsAdminRoleOrSuperuser',
    'IsAuthorOrHigherOrReadOnly',
]
