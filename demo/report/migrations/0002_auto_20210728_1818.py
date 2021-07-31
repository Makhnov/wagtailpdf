# Generated by Django 3.2.3 on 2021-07-28 18:18

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportpage',
            name='address_left',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportpage',
            name='address_right',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportpage',
            name='content',
            field=wagtail.core.fields.StreamField([('chapter', wagtail.core.blocks.CharBlock(form_classname='full title')), ('columns', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('sub_heading', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock())])), ('competences', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('sub_heading', wagtail.core.blocks.CharBlock(required=False)), ('entries', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()), ('kind', wagtail.core.blocks.ChoiceBlock(choices=[('table-content', 'Table content'), ('heading', 'Heading titles'), ('multi-columns', 'Multi-column text'), ('internal-links', 'Internal links'), ('style', 'Page style')]))], label='Entry')))])), ('offers', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('sub_heading', wagtail.core.blocks.CharBlock(required=False)), ('entries', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()), ('price', wagtail.core.blocks.IntegerBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))], label='Entry')))]))], blank=True),
        ),
    ]
