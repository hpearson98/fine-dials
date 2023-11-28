from django import forms
from .models import Watch, Brand, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Watch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = (
            'user',
            'created_on',
            'watch',
        )
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'review': 'Leave a review!',
        }