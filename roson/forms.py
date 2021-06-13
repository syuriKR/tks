from django import forms
from django.forms.widgets import RadioSelect

class PriceForm(forms.Form):
    price = forms.IntegerField(label='値段',min_value=200,max_value=1000)

class CalorieForm(forms.Form):
    calorie = forms.IntegerField(label='カロリー',min_value=200,max_value=1000)

class button(forms.Form):
    data = [
        ('0','値段高い順'),
        ('1','値段安い順'),
        ('2','カロリー多い順'),
        ('3','カロリー少ない順')
    ]
    data2 = [
        ('0','お惣菜'),
        ('1','お惣菜サラダ'),
        ('2','弁当'),
        ('3','チルド弁当'),
        ('4','デザート'),
        ('5','揚げ物'),
        ('6','冷凍食品'),
        ('7','グラタン'),
        ('8','インスタント'),
        ('9','粉もの'),
        ('10','麺類'),
        ('11','おにぎり'),
        ('12','パスタ'),
        ('13','サラダ'),
        ('14','スープ')
    ]
    choice = forms.ChoiceField(label='ソート',choices=data)
    choice2 = forms.ChoiceField(label='ジャンル',choices=data2)