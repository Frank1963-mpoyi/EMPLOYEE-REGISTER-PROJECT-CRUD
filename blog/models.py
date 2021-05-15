from    django.db               import          models
from    core.model_mixins       import          AuditFields 

from    django.urls             import          reverse





class Position(models.Model):
    
    title       = models.CharField('TITLE',    max_length=50)

    def __str__(self):
        return self.title




class Employee(AuditFields):
    
    fullname    = models.CharField('FULLNAME',       max_length=100)
    empl_code   = models.CharField('EMPLOYEE CODE',  max_length=3)
    mobile      = models.CharField('MOBILE',         max_length=15)
    position    = models.ForeignKey(Position,       on_delete=models.CASCADE , null=True, blank=True)
    slug        = models.SlugField()

    def __str__(self):
        return self.fullname
    


    def get_absolute_url(self):
        return reverse("blog:update",  kwargs={"slug": self.slug})


    def get_delete_url(self):
        return reverse("blog:delete", kwargs={"slug": self.slug})
    
    