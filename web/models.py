from django.db import models
import uuid
from django.utils.text import slugify 

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable= False, unique= True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique= True,blank=True)
    is_private = models.BooleanField(default= False)
                                     

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(self,*args, **kwargs)
    
    def __str__(self):
        return self.name
        
    
    #Contact form
class ContactForm(models.Model):
    contact_form_uuid= models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    #Eso es para ver el objeto por nombre
    def __str__(self):
        return self.customer_name