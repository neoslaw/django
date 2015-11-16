#coding: utf-8
#python 2 only!
from __future__ import unicode_literals, absolute_import
from django.utils.encoding import python_2_unicode_compatible
####################################################################################
from django.utils.translation import ugettext_lazy as _  #pootle do prowadzenia tlumaczen
from django.core.urlresolvers import reverse_lazy # zamienia nazwe widoku podając ewentuale parametry na konkretna sciezke.
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(_("first_name"),max_length=20)
    last_name = models.CharField(_("last_name"), max_length=50)

    def __str__(self):
        return _("{first_name} {last_name}").format(first_name=self.first_name, last_name=self.last_name,)

    class Meta:
        ordering = ('last_name', 'first_name')  #w jaki sposob maja byc sortowane dane domyslnie w bazie
        verbose_name = _('author')              #Raczej dopelniacz niz mianownik
        verbose_name_plural = _('authors')

@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
@python_2_unicode_compatible
class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Book(models.Model):
    '''
    Cos w rodzaju rekopisu.
    '''
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
    #author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('self:book-detail', kwargs={'pk':self.id})

@python_2_unicode_compatible
class BookEdition(models.Model):
    '''
    Wydanie okreslonej ksiazki
    '''
    book = models.ForeignKey(Book, related_name='editions')
    publisher = models.ForeignKey(Publisher)
    date = models.DateField()
    isbn = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book, publisher=self.publisher)

COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard')
#(wartosc_w_bazie, wartosc_wyswietlania)
)

@python_2_unicode_compatible
class BookItem(models.Model):
    '''
    Konkretny egzemplarz
    '''
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition,
                                           cover=self.get_cover_type_display())



