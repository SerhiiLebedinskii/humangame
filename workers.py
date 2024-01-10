ocupations = [{
  'title': 'engineer',
  'salary': 1000,
  'time': 160,
  'education_required': True,
  'education_type': 'technical'
},
{
  'title': 'teacher',
  'salary': 800,
  'time': 120,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'doctor',
  'salary': 1000,
  'time': 80,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'manager',
  'salary': 800,
  'time': 240,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'cleaner',
  'salary': 600,
  'time': 120,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'zoo_keeper',
  'salary': 1000,
  'time': 160,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'hairdresser',
  'salary': 800,
  'time': 240,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'nail_master',
  'salary': 2000,
  'time': 320,
  'education_required': False,
  'education_type': ''
}]


def workertime(education,time):
  if education == 'with_education':
    print(workers.get('with_education').get(time)) 
    print(workers.get('time').get(time)) 
  elif education == 'without_education':
    print(workers.get('without_education').get(time))
    print(workers.get('time').get(time))
  else:
    print('error')

workertime('without_education','nail_master')




