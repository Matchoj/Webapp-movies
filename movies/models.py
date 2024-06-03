from django.db import models

class Info(models.Model):
    Kinds = {
        (0, "Familly"),
        (1, "Anime"),
        (2, "Sci-fi"),
        (3, "Fantasy"),
        (4, "Comedy"),
        (5, "Drama"),
        (6, "Horror")
    }
    Ages = {
        (0, "+7"),
        (1, "+13"),
        (2, "+18")
    }

    kind = models.PositiveSmallIntegerField(default=0, choices=Kinds)
    age = models.PositiveSmallIntegerField(default=0, choices=Ages)

    def beckone(self):
        x = self.Kinds
        x1 = self.Ages
        y = next((t for t in x if t[0] == self.kind))
        y1 = next((t for t in x1 if t[0] == self.age))
        text = "Kind: {} | Age: {} ".format(y[1],y1[1])
        return text

    def __str__(self):
        return "{}".format(self.beckone())



class Movie(models.Model):
    title= models.CharField(max_length=80,blank=False,unique=True)
    year= models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    rating = models.DecimalField(max_digits=4,decimal_places=2)
    pictures= models.ImageField(upload_to="Images",null=True,blank=True)
    spec_info=models.OneToOneField(Info, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return "{} ({}) ".format(self.title,self.year)

class Comment(models.Model):

    comment= models.CharField(max_length=500,blank = False, unique= True)
    rate = models.DecimalField(max_digits=4,decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)