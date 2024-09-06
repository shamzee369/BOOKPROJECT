from django.db import models





class author(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return '{}'.format(self.name)

class book(models.Model):
    title=models.CharField(max_length=200,null=True)
    # author=models.CharField(max_length=200)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_meadia')
    quantity=models.IntegerField()

    author=models.ForeignKey(author,on_delete=models.CASCADE)
    

    def __str__(self):
        return '{}'.format(self.title)
    
