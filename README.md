# Wagtail menu app

This is just a test and not very useful yet.  
I'm not a Wagtail or Django expert => Don't use that app in production.

The code ist mostly inspired / stolen from a [blopost](http://jordijoan.me/simple-orderable-menus-wagtail/) and the Wagtail demo app.

The app provides the possibility to add Menus as Wagtail snippets.


## Usage

1. Add app to your wagtail project
2. Enable it in your settings.py
3. Run migration

After that you can create menus in the Wagtail admin under the snippets section.

To render you menu in your template you have to load the tag.
```
{% load menu_tags %}
```
Add
```
{% menu "Name of your menu" %}
```
where you want your menu to be rendered.
