from django import forms
from .models import Watch, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Watch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'