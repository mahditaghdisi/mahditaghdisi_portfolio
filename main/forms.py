from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "description"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "field-input", "required": True, "autocomplete": "name",
            }),
            "phone": forms.TextInput(attrs={
                "class": "field-input", "required": True, "autocomplete": "tel",
            }),
            "description": forms.Textarea(attrs={
                "class": "field-input field-textarea", "rows": 4,
            }),
        }

    def __init__(self, *args, lang="fa", **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            "fa": {"name": "نام", "phone": "شماره تماس", "description": "توضیحات پروژه (اختیاری)"},
            "en": {"name": "Name", "phone": "Phone", "description": "Project description (optional)"},
        }[lang]
        for field_name, label in labels.items():
            self.fields[field_name].label = label
        self.fields["description"].required = False
