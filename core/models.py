from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255)
    # upload_to is the path to the media folder
    file = models.FileField(upload_to="media/documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file
    
    # def delete(self, *args, **kwargs):
    #     self.file.delete()
    #     super().delete(*args, **kwargs)
        

        
