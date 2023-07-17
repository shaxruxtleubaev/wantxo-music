from django.db.models import *
from django.utils.timezone import now

class Song(Model):

    name = CharField('Name', max_length=128)
    author = CharField('Author', max_length=128)
    date = DateField('Date', default=now)
    image = ImageField('Image', upload_to='images/%Y/%m/%d')
    song = FileField('Song file', upload_to='songs/%Y/%m/%d')
    lyrics = TextField('Lyrics')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'