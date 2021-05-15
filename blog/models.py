from    django.db            import     models
from    core.model_mixins    import     AuditFields 
from    django.utils.text    import     slugify



class Position(models.Model):
    
    title       = models.CharField('TITLE',    max_length=50)

    def __str__(self):
        return self.title




class Employee(AuditFields):
    
    fullname    = models.CharField('FULLNAME',       max_length=100)
    empl_code   = models.CharField('EMPLOYEE CODE',  max_length=3)
    mobile      = models.CharField('MOBILE',         max_length=15)
    position    = models.ForeignKey(Position,       on_delete=models.CASCADE , null=True, blank=True)
    # slug        = models.SlugField('SLUG',          max_length=200)

    def __str__(self):
        return self.fullname
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug=slugify(self.fullname)
    #     super().save(*args, **kwargs)



