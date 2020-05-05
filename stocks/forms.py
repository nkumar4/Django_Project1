from django import forms
from .models import Company


class ListForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["ticker", "co_name", "latest_price", "previous_price", "pe_ratio", "marketcap", "change"]