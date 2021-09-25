#handles image resizing
from io import BytesIO
from PIL import Image

#for creating thumbnails
from django.core.files import File
from django.db import models
from django.db.models.fields import SlugField

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)

    # URL Address Of Name
    slug = models.SlugField()

    #For Ordering Categories
    class Meta:
        #orders categories according to name in ascending order
        ordering = ('name',)
    #// Class Meta

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        """
        Returns The URL Of The Category
        """
        return f'/{self.slug}/'
#// Class Category

#Product Model
class Product(models.Model):

    """
    ManyToOne Relationship i.e Many Products Single Category
    on_delete=models.CASCAD : Deleting one of category deletes all products under that category
    """
    category = models.ForeignKey(Category , related_name='products' , on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    description = models.TextField(blank=True , null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #Images Get Uploaded To Folder : 'uploads'
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    #When new product is created automatically adds date & time to it
    data_added = models.DateTimeField(auto_now_add=True)

    #For Ordering Products
    class Meta:
        #Orders products according to date_added in descending order
        ordering = ('-data_added',)
    #// Class Meta

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        """
        Returns The URL Of The Product
        """
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        """
        Returns image URL if exists
        """
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        """
        If Thumnail exists return thumbnail url if not Creates thumbnail from image & return the url
        """
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)            
                self.save()
            else:    
                return ''

    def make_thumbnail(self, image, size=(300 , 200)):
        """
        Take image input , creates thumbnail & return the thumbnail
        """
        #creates a new object with given image
        img = Image.open(image)

        #Convert To RGB Just To Be Sure Evrything Is Fine
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()

        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

# // Class Product







