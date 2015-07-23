from django.db import models
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel


class LinkFields(models.Model):
    """
    Represents a link to an external page, a document or a Wagtail page
    """
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set an external link if you want the link to point somewhere outside the CMS.'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing page if you want the link to point somewhere inside the CMS.'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing document if you want the link to open a document.'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external


class MenuItem(LinkFields):
    @property
    def url(self):
        return self.link

    @property
    def title(self):
        title = 'No title'
        if self.link_external:
            title = self.link_external
        elif self.link_page:
            title = self.link_page.title
        elif self.link_document:
            title = self.link_document.title
        return title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Menu item"
        # description = "Items appearing in the menu"


class MenuMenuItem(Orderable, MenuItem):
    parent = ParentalKey(to='menu.Menu', related_name='menu_items')


class MenuManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(menu_name=name)


@register_snippet
class Menu(models.Model):
    objects = MenuManager()
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    @property
    def items(self):
        return self.menu_items.all()

    def __unicode__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Navigation menu"
        # description = "Navigation menu"


Menu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel(Menu, 'menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]
