from django.db import models

# Create your models here.

class City(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
            return self.name

class Genre(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
            return self.name

class Album(models.Model):
      released_date = models.DateTimeField()
      album_name  = models.CharField(max_length=50)
      artist_name  = models.CharField(max_length=50)
      city = models.ForeignKey(City, on_delete=models.CASCADE)

      def __str__(self):
            return self.album_name + " " + self.artist_name + " " + self.city.name
      
class Song(models.Model):
      related_model = models.ForeignKey(Album, on_delete=models.CASCADE)
      song_name = models.CharField(max_length=255)
      time = models.FloatField()
      genre = models.ManyToManyField(Genre)

      def __str__(self):
            return self.related_model.album_name + " " + self.song_name + " " + str(self.time)