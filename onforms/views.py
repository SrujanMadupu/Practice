from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
# Create your views here
from .models import Biodata
from .forms import CustomBioForm ,BusinessInformationForm
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet

# class RequiredFormSet(BaseFormSet):
#     def add_form(self, **kwargs):
#         # add the form
#         tfc = self.total_form_count()
#         self.forms.append(self._construct_form(tfc, **kwargs))
#         self.forms[tfc].is_bound = False

#         # make data mutable
#         self.data = self.data.copy()

#         # increase hidden form counts
#         total_count_name = '%s-%s' % (self.management_form.prefix, TOTAL_FORM_COUNT)
#         initial_count_name = '%s-%s' % (self.management_form.prefix, INITIAL_FORM_COUNT)
#         self.data[total_count_name] = self.management_form.cleaned_data[TOTAL_FORM_COUNT] + 1
#         self.data[initial_count_name] = self.management_form.cleaned_data[INITIAL_FORM_COUNT] + 1

#     def add_fields(self, form, index):
#         super(RequiredFormSet, self).add_fields(form, index)
#         form.empty_permitted = False







def CustomBioView(request):

	if request.method == 'POST':
		customform = CustomBioForm(request.POST)
		if customform.is_valid():
			print(customform)
			return HttpResponse("your data successfully added")
		else:
			print("your form is not valid")

	form = BusinessInformationForm
	return render(request,'onforms/bioform.html',{'form':form})
