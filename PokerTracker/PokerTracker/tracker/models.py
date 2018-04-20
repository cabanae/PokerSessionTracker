from django.db import models
from django.urls import reverse  # Used to generate urls by reversing the URL patterns
from datetime import datetime
from django.db.models import Sum
from datetime import date
from django.contrib.auth.models import User

class Place(models.Model):
    """
    Model representing a place
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    def get_absolute_url(self):
        """
        Returns the url to access a particular placwe instance.
        """
        return reverse('place-detail', args=[str(self.id)])

class Game(models.Model):
    game_type = models.CharField(max_length=200)
    def __str__(self):
        return self.game_type
    def get_absolute_url(self):
        """
        Returns the url to access a particular game instance.
        """
        return reverse('game-detail', args=[str(self.id)])

class Session(models.Model):
    """
    Model representing a Session
    """
    #fields for the db
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(null=True)
    Notes = models.TextField(max_length=1000, blank=True)
    game_type = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(null=True)
    hourly_rate = models.DecimalField(null=True,max_digits=20, decimal_places=5,editable=False)
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
    time_per_session = models.DurationField(null=True,editable=False)
    session_user = models.ForeignKey(User, on_delete=models.SET_NULL, unique=False, null=True,editable=False)

    #def user_default(self,request):
     #   return {"session_user": request.user}
    @property
    def total_time(self):
        #sum of total time, for each user
        for key, val in Session.objects.filter(session_user=self.session_user).aggregate(Sum('time_per_session')).items():
            return val
    def time_diff(self):
        return self.time_end - self.time_start
    def hourly(self):
        #calc total time of session
        timeA = self.time_end - self.time_start
        #convert seconds hours, calc hourly
        total_time_hours = timeA.seconds / 3600.0
        hourly_session = self.amount / total_time_hours
        #save hourly in db
        my_hourly = Session.objects.get(id=self.id)
        my_hourly.hourly_rate = hourly_session
        my_hourly.save()
        #save time diff in db
        my_time = Session.objects.get(id=self.id)
        my_time.time_per_session = timeA
        my_time.save()
        return hourly_session
    def total_money(self):
        #sum of total money earned
        for key, val in Session.objects.filter(session_user=self.session_user).aggregate(Sum('amount')).items():
            sum_total_amount = val
            return val
    def total_hourly(self):
        for key, val in Session.objects.filter(session_user=self.session_user).aggregate(Sum('time_per_session')).items():
            total_time_allsession = val
        for key, val in Session.objects.filter(session_user=self.session_user).aggregate(Sum('amount')).items():
            total_money_all_session = val
        #calc the total hourly for all sessions
        return total_money_all_session / (total_time_allsession.seconds / 3600.0)
    def display_place(self):
        """
        Creates a string for Place. This is required to display palce in Admin.
        """
        return ', '.join([place.name for place in self.place.all()[:3]])

    def display_game(self):
        """
           Creates a string for Game. This is required to display game in Admin.
        """
        return ', '.join([game.name for game in self.game.all()[:3]])
    def get_absolute_url(self):
        """
        Returns the url to access a particular session instance.
        """
        return reverse('session-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)


