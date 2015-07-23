# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_external', models.URLField(
                    help_text=b'Set an external link if you want the link to point somewhere outside the CMS.',
                    null=True, verbose_name=b'External link', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Navigation menu',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('linkfields_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='menu.LinkFields')),
            ],
            options={
                'verbose_name': 'Menu item',
            },
            bases=('menu.linkfields',),
        ),
        migrations.AddField(
            model_name='linkfields',
            name='link_document',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True,
                                    to='wagtaildocs.Document',
                                    help_text=b'Choose an existing document if you want the link to open a document.',
                                    null=True),
        ),
        migrations.AddField(
            model_name='linkfields',
            name='link_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True,
                                    to='wagtailcore.Page',
                                    help_text=b'Choose an existing page if you want the link to point somewhere inside the CMS.',
                                    null=True),
        ),
        migrations.CreateModel(
            name='MenuMenuItem',
            fields=[
                ('menuitem_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='menu.MenuItem')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('parent', modelcluster.fields.ParentalKey(related_name='menu_items', to='menu.Menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('menu.menuitem', models.Model),
        ),
    ]
