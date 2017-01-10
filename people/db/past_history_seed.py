from people.models import PastHistory

past_history = ['腦血管疾病', '心臟疾病', '肺臟疾病', '糖尿病', '高血壓',
          '肝臟疾病', '腎臟疾病', '惡性腫瘤', '癲癇', '氣喘', '精神疾病', 
          'HIV(+)', '肺結核']

for i, disease in enumerate(past_history):
    past_history = PastHistory.objects.create(name=disease)

