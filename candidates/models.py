from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
#from clients.models import ClientProfile 


class Candidate(models.Model):
    #candidateid = models.AutoField(primary_key=True)
    #clientid = models.IntegerField(default="")
    candidatefirstname = models.CharField(max_length=255)
    candidatemiddlenames = models.CharField(max_length=255, blank=True, null=True)
    candidatefamilyname = models.CharField(max_length=255)
    candidatesalutation = models.CharField(max_length=255, blank=True, null=True)
    candidateemail = models.CharField(max_length=255, blank=True, null=True)

    referencestatus = models.IntegerField(default=3, db_column='ReferenceStatus')
    referencerequested = models.DateTimeField(default=timezone.now)
    referencereceived = models.DateTimeField(default=timezone.now, db_column='ReferenceReceived')

    passportstatus = models.IntegerField(default=3, db_column='PassportStatus')  # Field name made lowercase.
    passportchecked = models.DateTimeField(default=timezone.now, db_column='PassportChecked')

    ccjstatus = models.IntegerField(default=3, db_column='CCJ')
    ccjrequestmade = models.DateTimeField(default=timezone.now, db_column='ccjrequestmade')
    ccjchecked = models.DateTimeField(default=timezone.now, db_column='ccjChecked')
  
    righttoworkstatus = models.IntegerField(default=3, db_column='RightToWork')
    righttoworkrequestmade = models.DateTimeField(default=timezone.now, db_column='righttoworkrequestmade')
    righttoworkchecked = models.DateTimeField(default=timezone.now, db_column='RightToWorkChecked')
   
    enhanceddbsstatus= models.IntegerField(default=3, db_column='EnhancedDBS')
    enhanceddbsrequestmade = models.DateTimeField(default=timezone.now, db_column='enhanceddbsrequestmade')
    enhanceddbschecked = models.DateTimeField(default=timezone.now, db_column='EnhanceddbsChecked')
 
    dbsstatus = models.IntegerField(default=3, db_column='DBS')
    dbsrequestmade = models.DateTimeField(default=timezone.now, db_column='dbsrequestmade')
    dbschecked = models.DateTimeField(default=timezone.now, db_column='dbsChecked')

    dob = models.DateTimeField(default=timezone.now, db_column='dob')

    dvlc = models.IntegerField(default=1, db_column='dvlc')
    dvlcpoints = models.IntegerField(default=0, db_column='dvlcpoints')
 
    #client = models.ForeignKey(ClientProfile, default="", on_delete=models.CASCADE)
    #client = models.ForeignKey(User, default="", db_column='clientid',on_delete=models.CASCADE)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
  
    class Meta:
        managed = True
        db_table = 'candidate'
        #unique_together = (('candidateid', 'clientid'),)

    def __str__(self):
        return self.candidatefirstname+" "+self.candidatefamilyname

    def get_absolute_url(self):
        return reverse('candidates-detail', kwargs={'pk': self.pk}) 

   # def get_absolute_url(self):
    #   return reverse('admin-page:index') 
        #return reverse('admin-page:index', kwargs={'pk': self.pk}) 
        #return reverse('admin-page:index', current_app=self.name)

    #def get_absolute_url(self):
     #   return reverse('client-name', {self.username})
        #return reverse('client-name', kwargs={'pk': self.pk}) 

        