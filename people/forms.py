from django import forms
from django.forms.formsets import BaseFormSet
from .models import People, PastHistory

class PeopleForm(forms.Form):
    name = forms.CharField(max_length=30, label="姓名", 
                           error_messages = {'required' : "姓名必須填寫。"},
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    GENDER_CHOICES = (('-----------','-----------'),
                      ('男', '男'),
                      ('女', '女'))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="性別")

    birthday = forms.DateField(error_messages = {'required' : "出生年月日必須填寫。"}, label="出生年月日",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    AGE_CHOICES = (('','-----------'),
                   ('<1', '<1歲'),
                   ('1-14', '1-14歲'),
                   ('15-18', '15-18歲'),
                   ('19-39', '19-39歲'),
                   ('40-64', '40-64歲'),
                   ('>=65', '>=65歲'))
    
    age = forms.ChoiceField(choices=AGE_CHOICES, label="年齡", required = False)


    identity_number = forms.CharField(max_length=30, label="身分證號碼", 
                                      error_messages = {'required' : "身分證號碼必須填寫。"},
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(max_length=30, label="電話號碼",
                            error_messages = {'required' : "電話號碼必須填寫。"},
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    address = forms.CharField(max_length=50, label="住址", required = False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'size':'60'}))
    
    AVERAGE_MONTHLY_INCOME_CHOICES = (('','-----------'),
                                      ('20,000元以下', '20,000元以下'),
                                      ('20,000~29,999元', '20,000~29,999元'),
                                      ('30,000~39,999元', '30,000~39,999元'),
                                      ('40,000~49,999元', '40,000~49,999元'),
                                      ('50,000~59,999元', '50,000~59,999元'),
                                      ('60,000~69,999元', '60,000~69,999元'),
                                      ('70,000~79,999元', '70,000~79,999元'),
                                      ('80,000~89,999元', '80,000~89,999元'),
                                      ('90,000~99,999元', '90,000~99,999元'),
                                      ('100,000元以上', '100,000元以上'))

    average_monthly_income = forms.ChoiceField(choices=AVERAGE_MONTHLY_INCOME_CHOICES, 
                                               label="平均月收入", 
                                               required = False)

    weight = forms.FloatField(required=False, min_value=0, label="體重",
                              widget=forms.NumberInput(attrs={'step': "0.01"}))


    BLOOD_TYPE_CHOICES = (('','-----------'),
                          ('O', 'O型'),
                          ('A', 'A型'),
                          ('B', 'B型'),
                          ('AB', 'AB型')
    )
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES, label="血型", required = False)


   
    past_history = forms.ModelMultipleChoiceField(queryset=PastHistory.objects.all(), required = False, 
                                                  label="過去病史",
                                                  widget=forms.CheckboxSelectMultiple())

    hospital_records = forms.CharField(max_length=50, label="病例醫院", required = False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'size': '100','placeholder': '亞東紀念醫院, 新北市聯合醫院三重院區'}))

    food_allergy_history = forms.CharField(max_length=50, label="是否對哪些食物過敏？", required = False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'size': '100', 'placeholder': '魚, 核果類, 花生, 甲殼類海鮮'}))

    medicine_allergy_history = forms.CharField(max_length=50, label="是否對哪些藥物過敏？", required = False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'size': '100','placeholder': 'Aspirin, Dilantin'}))

    complaint = forms.CharField(max_length=50, label="主訴", required = False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'size': '100'}))

    class Meta:
        model = People
        fields = ['name', 'gender', 'birthday', 'age', 'identity_number', 
                  'phone', 'address', 'average_monthly_income', 'weight',
                  'past_history', 'hospital_records', 'food_allergy_history',
                  'medicine_allergy_history', 'complaint']
    
    def clean_gender(self):
        data = self.cleaned_data.get('gender')
        if data == self.fields['gender'].choices[0][0]:
            raise forms.ValidationError('性別必須填寫。')
        return data

    
    # age = models.CharField(max_length=10)
    # identity_number = models.CharField(max_length=30, db_index=True)
    # phone = models.CharField(max_length=30)
    # address = models.CharField(max_length=50)
    # average_monthly_income = models.CharField(max_length=30, null=True, blank=True)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="緊急聯絡人姓名", 
                           error_messages = {'required' : "緊急聯絡人姓名必須填寫"},
                           widget=forms.TextInput(attrs={'class': 'contact-input'}))

    phone = forms.CharField(max_length=30, label="緊急聯絡人電話",
                            error_messages = {'required' : "緊急聯絡人電話必須填寫。"},
                            widget=forms.TextInput(attrs={'class': 'contact-input'}))

class BaseContactFormSet(BaseFormSet):
    def clean(self):
        """
        Check no same name or phone
        Check that all name have phone, all phone have name
        """
        if any (self.errors):
            return

        names = []
        phones = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']

                # Check no same name or phone
                if name and phone:
                    if name in names:
                        duplicates = True

                    if phone in phones:
                        duplicates = True

                if duplicates:
                    raise forms.ValidationError(
                        '緊急聯絡人的姓名與電話請勿重複。',
                        code='duplicate_links'
                    )

                # Check that all name have phone, all phone have name
                if phone and not name:
                    raise forms.ValidationError(
                        '緊急聯絡人電話必須要有緊急聯絡人姓名',
                        code='missing_name'
                    )
                elif name and not phone:
                    raise forms.ValidationError(
                        '緊急聯絡人必須要有緊急聯絡人電話',
                        code='missing_phone'
                    )  