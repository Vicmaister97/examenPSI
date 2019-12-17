import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import Medico, Paciente, Receta

def poblar():
	m1=Medico.objects.get_or_create(id=1, nombreM='medico1')[0]
	m1.save()

	m2=Medico.objects.get_or_create(id=2, nombreM='medico2')[0]
	m2.save()

	m3=Medico.objects.get_or_create(id=3, nombreM='medico3')[0]
	m3.save()

	m4=Medico.objects.get_or_create(id=4, nombreM='medico4')[0]
	m4.save()


	p1=Paciente.objects.get_or_create(id=1, nombreP='paciente1')[0]
	p1.save()

	p2=Paciente.objects.get_or_create(id=2, nombreP='paciente2')[0]
	p2.save()


	r1=Receta.objects.get_or_create(id=1, medico_id=m1, paciente_id=p1)[0]
	r1.save()

	r2=Receta.objects.get_or_create(id=2, medico_id=m2, paciente_id=p1)[0]
	r2.save()

	r3=Receta.objects.get_or_create(id=3, medico_id=m1, paciente_id=p2)[0]
	r3.save()

	r4=Receta.objects.get_or_create(id=4, medico_id=m2, paciente_id=p2)[0]
	r4.save()

	r5=Receta.objects.get_or_create(id=5, medico_id=m3, paciente_id=p2)[0]
	r5.save()


# Start execution here!
if __name__ == '__main__':
    print('Comenzando script de poblar Aplicacion...')
    poblar()
