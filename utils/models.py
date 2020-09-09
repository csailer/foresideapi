import logging
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AnonymousUser, Group, Permission
from dry_rest_permissions.generics import authenticated_users
from django.utils import timezone
from cuser.middleware import CuserMiddleware


_logger = logging.getLogger(__name__)


class AuditableModel(models.Model):
    """Abstract base class for models that need to be audited.
    """
    # , related_name="%(app_label)s_%(class)s_modified_by"
    create_date = models.DateTimeField(auto_now=False,
                                       auto_now_add=True,
                                       null=True,
                                       blank=True,
                                       verbose_name=_("Created Date"))
    created_by = models.CharField(max_length=100,
                                  blank=True,
                                  null=True,
                                  db_index=True,
                                  verbose_name=_("Created By"))
    modified_date = models.DateTimeField(auto_now=False,
                                         auto_now_add=True,
                                         null=True, blank=True,
                                         verbose_name=_("Modified Date"))
    modified_by = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   db_index=True,
                                   verbose_name=_("Modified By"))



    @staticmethod
    @authenticated_users
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    @authenticated_users
    def has_write_permission(request):
        return True

    @staticmethod
    @authenticated_users
    def has_create_permission(request):
        return True

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        This override tracks the datetime a change was made to an object and the user who made the change
        """
        request = kwargs.pop("request",
                             None)  # Use pop to remove the request Key Word, don't want it flowing to the "super" call

        if request is not None:
            user = request.user
        else:
            try:
                user = CuserMiddleware.get_user()
            except:
                user = None

        if user is not None:
            if isinstance(user, AnonymousUser):
                user = None
        if user is not None:
            if self._state.adding:
                self.created_by = user.username
                self.modified_by = user.username
                self.create_date = timezone.now()
                self.modified_date = timezone.now()
            else:
                self.modified_by = user.username
                self.modified_date = timezone.now()

        super(AuditableModel, self).save(*args, **kwargs)  # Call the base class save() method.
