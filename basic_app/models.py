from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Exam(models.Model):
    BRANCH=[('CS','CS'),('ME','ME'),('PIE','PIE'),('EE','EE'),('CE','CE'),('ECE','ECE'),('IT','IT')]
    SEM=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]
    SESSIONAL=[('MidSem 1','MidSem 1'),('MidSem 2','MidSem 2'),('EndSem','EndSem'),('All','All')]
    YEAR=[('2019-20','2019-20'),('2018-19','2018-19'),('2017-18','2017-18')]
    COLLEGE=[('NIT-ALLAHABAD','NIT-ALLAHABAD'),('NIT-BHOPAL','NIT-BHOPAL'),('NIT-CALICUT','NIT-CALICUT'),('NIT-HAMIRPUR','NIT-HAMIRPUR'),
    ('NIT-JAIPUR','NIT-JAIPUR'),('NIT-JALANDHAR','NIT-JALANDHAR'),('NIT-JAMSHEDPUR','NIT-JAMSHEDPUR'),('NIT-KURUKSHETRA','NIT-KURUKSHETRA'),
    ('NIT-NAGPUR','NIT-NAGPUR'),('NIT-ROURKELA','NIT-ROURKELA'),('NIT-SILCHAR','NIT-SILCHAR'),('NIT-KARNATKA','NIT-KARNATKA'),
    ('NIT-WARANGAL','NIT-WARANGAL'),('NIT-DURGAPUR','NIT-DURGAPUR'),('NIT-SRINAGAR','NIT-SRINAGAR'),('NIT-SURAT','NIT-SURAT'),
    ('NIT-TRICHY','NIT-TRICHY'),('NIT-PATNA','NIT-PATNA'),('NIT-RAIPUR','NIT-RAIPUR'),('NIT-AGARTALA','NIT-AGARTALA'),('NIT-ARUNACHALPRADESH','NIT-ARUNACHALPRADESH'),('NIT-DELHI','NIT-DELHI'),
    ('NIT-GOA','NIT-GOA'),('NIT-MANIPUR','NIT-MANIPUR'),('NIT-MEGHALAYA','NIT-MEGHALAYA'),('NIT-MIZORAM','NIT-MIZORAM'),('NIT-NAGALAND','NIT-NAGALAND'),
    ('NIT-PUDUCHERRY','NIT-PUDUCHERRY'),('NIT-SIKKIM','NIT-SIKKIM'),('NIT-UTTARAKHAND','NIT-UTTARAKHAND'),('NIT-ANDHRAPRADESH','NIT-ANDHRAPRADESH')
    ]
    TYPE=[('NOTES','NOTES'),('PAPER','PAPER')]

    name=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='users')
    college=models.CharField(max_length=200,choices=COLLEGE,default='NIT-KURUKSHETRA')
    branch=models.CharField(max_length=200,choices=BRANCH)
    semester=models.PositiveIntegerField(choices=SEM)
    file=models.FileField(null=True)
    published_date=models.DateTimeField(blank=True,null=True)
    sessional=models.CharField(max_length=200,choices=SESSIONAL,null=True)
    year=models.CharField(max_length=200,choices=YEAR,null=True)
    subject=models.CharField(max_length=200,default='All')
    type=models.CharField(max_length=200,choices=TYPE,default='NOTES')
    professor=models.CharField(max_length=200)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('exam_list')

    def __str__(self):
        return self.college+" "+self.branch+str(self.semester)+" "+self.year+" "+self.type+" "+self.subject+" "+str(self.file)+" "+self.name.first_name



class UserProfileInfo(models.Model):

    COLLEGE=[('NIT-ALLAHABAD','NIT-ALLAHABAD'),('NIT-BHOPAL','NIT-BHOPAL'),('NIT-CALICUT','NIT-CALICUT'),('NIT-HAMIRPUR','NIT-HAMIRPUR'),
    ('NIT-JAIPUR','NIT-JAIPUR'),('NIT-JALANDHAR','NIT-JALANDHAR'),('NIT-JAMSHEDPUR','NIT-JAMSHEDPUR'),('NIT-KURUKSHETRA','NIT-KURUKSHETRA'),
    ('NIT-NAGPUR','NIT-NAGPUR'),('NIT-ROURKELA','NIT-ROURKELA'),('NIT-SILCHAR','NIT-SILCHAR'),('NIT-KARNATKA','NIT-KARNATKA'),
    ('NIT-WARANGAL','NIT-WARANGAL'),('NIT-DURGAPUR','NIT-DURGAPUR'),('NIT-SRINAGAR','NIT-SRINAGAR'),('NIT-SURAT','NIT-SURAT'),
    ('NIT-TRICHY','NIT-TRICHY'),('NIT-PATNA','NIT-PATNA'),('NIT-RAIPUR','NIT-RAIPUR'),('NIT-AGARTALA','NIT-AGARTALA'),('NIT-ARUNACHALPRADESH','NIT-ARUNACHALPRADESH'),('NIT-DELHI','NIT-DELHI'),
    ('NIT-GOA','NIT-GOA'),('NIT-MANIPUR','NIT-MANIPUR'),('NIT-MEGHALAYA','NIT-MEGHALAYA'),('NIT-MIZORAM','NIT-MIZORAM'),('NIT-NAGALAND','NIT-NAGALAND'),
    ('NIT-PUDUCHERRY','NIT-PUDUCHERRY'),('NIT-SIKKIM','NIT-SIKKIM'),('NIT-UTTARAKHAND','NIT-UTTARAKHAND'),('NIT-ANDHRAPRADESH','NIT-ANDHRAPRADESH')
    ]
    BRANCH=[('CS','CS'),('ME','ME'),('PIE','PIE'),('EE','EE'),('CE','CE'),('ECE','ECE'),('IT','IT')]
    SEM=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    college=models.CharField(max_length=200,choices=COLLEGE,default='NIT-KURUKSHETRA')
    branch=models.CharField(max_length=200,choices=BRANCH)
    semester=models.PositiveIntegerField(choices=SEM,default=4)
    def __str__(self):
        return self.user.username
