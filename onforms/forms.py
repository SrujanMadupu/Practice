from django import forms 


class CustomBioForm(forms.Form):
	first_name = forms.CharField(max_length=120,
		widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name'}))
	extra_field_count = forms.CharField(widget=forms.HiddenInput())


	def __init__(self,*args,**kwargs):
		extra_fields = kwargs.pop('extra',0)


		super(CustomBioForm,self).__init__(*args,**kwargs)
		self.fields['extra_field_count'].initial = extra_fields

		for index in range(int(extra_fields)):
			self.fields['first_name_{index}'.format(index=index)] = forms.CharField()

class BusinessInformationForm(forms.Form):

	official_name = forms.CharField(max_length=255, label='Business Name', 
		widget=forms.TextInput(attrs={'placeholder': 'Business Name'}))
	short_name = forms.CharField(required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Alternate business name 1'}))

	address = forms.CharField(max_length=255, required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Business Address 1'}))

	city = forms.CharField(max_length=255, required=False,
	   widget=forms.TextInput(attrs={'placeholder': 'City'}))

	state = forms.CharField(required=False,
		widget=forms.TextInput(attrs={'placeholder': 'State'}))

	phone = forms.CharField(required=False,
		widget=forms.TextInput(attrs={'placeholder': 'Phone Number(s)'}))

	web_page = forms.CharField(required=False,
		widget=forms.TextInput(attrs={'placeholder': 'Business URL(s)'}))

	zip_code = forms.CharField(required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'zip'}))


class PersonalInfo(forms.Form):
	name = forms.CharField(max_length=120,
		widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
	age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Your age'}))



