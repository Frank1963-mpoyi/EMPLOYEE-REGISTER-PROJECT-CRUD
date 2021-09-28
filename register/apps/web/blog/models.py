import uuid

from django.db                                                      import models
from django.urls                                                    import reverse
from django.core.validators                                         import RegexValidator
from django.db.models.signals                                       import pre_save

from register.core.model_mixins                                     import AuditFields
from register.apps.web.blog.utils                                   import unique_slug_generator, employee_randcode_gen

USERNAME_REGEX     = '^[a-zA-Z0-9.+-]*$'
PHONE_NUMBER_REGEX = '^[ 0-9]+$'


class Position(models.Model):
    
    title                       = models.CharField('TITLE',    max_length=50)

    def __str__(self):
        return self.title


class Employee(AuditFields):

    uuid_code                   = models.UUIDField('UUID CODE',         primary_key=True,           default=uuid.uuid4,     editable=False)

    empl_code                   = models.CharField('CODE',              max_length=100,             blank=False,            default=employee_randcode_gen)
    token_key                   = models.UUIDField('TOKEN',             default=uuid.uuid4,         editable=False,         blank=True, null=True)

    fullname                    = models.CharField('FULLNAME',          max_length=100)
    mobile                      = models.CharField('PHONE NUMBER',      max_length=30,              validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message='Invalid Phone Number', code='invalid_username')], blank=True, null=True)
    position                    = models.ForeignKey(Position,           verbose_name="POSITION",    on_delete=models.CASCADE , null=True, blank=True)
    slug                        = models.SlugField("SLUG",              blank=True, unique=True)

    class Meta:
        app_label           = 'blog'
        db_table            = 'Employee'
        verbose_name_plural = 'employees'

    @property
    def title(self):
        return "title" # this is add the field and value to the model 

    def __str__(self):
        return self.fullname
    
    def get_absolute_url(self):
        return reverse("blog:update",  kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("blog:delete", kwargs={"slug": self.slug})

    
#this is the method to handle pre_save
def employee_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(employee_pre_save_receiver,  sender= Employee)