from django.db import models,backend,connection
from django.contrib.auth.models import User

class LoginUser(models.Model):
    user=models.ForeignKey(User)
    website = models.CharField('Aadhar Card No.',max_length=100,blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.get_full_name()

class Party(models.Model):
    party_name=models.CharField(max_length=300)
    NATIONAL = 'National Party'
    STATE = 'state'
    party_type_choices = (
        (NATIONAL, 'National Party'),
        (STATE, 'State/Regional Party'),
    )
    party_type = models.CharField(max_length=100,
                                      choices = party_type_choices)
    def __str__(self):              
        return self.party_name
    def num_of_seats(party):
        return party.person_set.count()

class Person(models.Model):

    person_name=models.CharField(max_length=200)
    
    person_position=models.CharField('Post',max_length=200)
    
    person_party=models.ForeignKey(Party)
    
    image= models.ImageField(upload_to='static/chat/images/uploaded_files', blank=True)
    
    person_consti=models.CharField('Constituency',max_length=200)
    
    votes=models.IntegerField('Total_votes',max_length=200)
    def __str__(self):              
        return self.person_name

class Argument(models.Model):

    
    person=models.ForeignKey(Person)    
    
    text=models.CharField('Argument',max_length=1000000,default='')
    
    upvote=models.IntegerField(default=0)
    
    downvote=models.IntegerField(default=0)
    
    time=models.DateTimeField('speaking time')
    def __str__(self):              
        return self.text
        
    def up(self):
        self.upvote+=1
    def down(self):
        self.downvote+=1
class test3(models.Model):
    pass