from django.db import models
import uuid
from users.models import Profile

from django.db.models.deletion import CASCADE


# Create your models here.


class Tutorial(models.Model):

    INSTRUMENT = (
        ('drums', 'Drums'),
        ('piano', 'Piano'),
        ('bass',  'Bass Guitar'),
        ('guitar', ' Guitar'),
        ('sax', 'Saxophone'),
        ('percusion', 'Percusion'),
        ('singing', 'Vocal Coach'),
    )

    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True, default = 'default.jpg')
    specialty = models.CharField(max_length=100, null=True, blank=True, choices= INSTRUMENT)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    totalVote = models.IntegerField(default=0, )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']


    def __str__(request):
        return request.name

    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ' '
        return img


   # @property
    #def calculateRevieweCount(self):
    #    liked = review.filter(value = 'up').count()
    #    disliked = review.filter(value = 'down').count()

    #    totalLikes = liked.count()
    #    totalDislikes = disliked.count()

    #    self.like = totalLikes
    #    self.dislikes = totalDislikes
    #    self.save()






class Review(models.Model):

    RESPONSE = (
        ('up', 'Like' ),
        ('down', 'Dislike')
    )

    #owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    tutorial = models.ForeignKey(Tutorial, on_delete= models.CASCADE, )
    name = models.CharField(max_length=200, blank=False, null=True)
    body = models.TextField(blank=False, null=True, )
    like = models.CharField( max_length=100, choices=RESPONSE, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    #class Meta:
        #unique_together = [['owner', 'tutorial']]     #retricting a owner to leave only one review per project
    
    class Meta:
        ordering = ['-created']

    def __str__(request):
        return str(request.like)
    
    #@property
    #def likedCount(self):

        liked = self.like(value = 'up')
        totalLiked = liked.count()
        return totalLiked
    
   # @property
   # def dislikedCount(self):
        disliked = self.like(value = 'down')
        totalDisliked =disliked.count()
        return totalDisliked



class Tag(models.Model):
    name = models.CharField(max_length=200, )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(request):
        return str(request.name)




# class Reply(models.Model):
#     owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True )
#     body = models.TextField(blank=False, null=True, )
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     class Meta:
#         verbose_name_plural = 'Replies'
    
#     def __str__(self):
#         return self.body

    