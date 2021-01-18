from    django.db            import     models
from    core.model_mixins    import     AuditFields 




class Position(models.Model):
    
    title       = models.CharField('TITLE',    max_length=50)

    def __str__(self):
        return self.title




class Employee(AuditFields):
    
    fullname    = models.CharField('FULLNAME',       max_length=100)
    empl_code   = models.CharField('EMPLOYEE CODE', max_length=3)
    mobile      = models.CharField('MOBILE',         max_length=15)
    position    = models.ForeignKey(Position, on_delete=models.CASCADE , null=True, blank=True)


    def __str__(self):
        return self.fullname



