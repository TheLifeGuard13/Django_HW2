from django import forms

from catalog.models import Products, Contacts, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_actual':
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(StyleFormMixin, forms.ModelForm):
    words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Products
        fields = 'name', 'description', 'preview', 'category', 'price'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.words:
            if cleaned_data.lower() == word:
                raise forms.ValidationError('Недоступное наименование продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if set(cleaned_data.lower().split(' ')) & set(self.words):
            raise forms.ValidationError('Описание содержит запрещенные слова')
        return cleaned_data


class ContactsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            "description",
            "category",
            "is_published",
        )
