from django.test import TestCase
import unittest
from alimentos.models import  Persona

class testPersona(unittest.TestCase):
    def test_crear(self):
        persona = Persona.objects.create(rut='22-5',
                                     nombre='Lucas',
                                     apellidos='Alvarez Rosas',
                                     email='LC@gmail.com',
                                     direccion='jose ramirez 123',
                                     cargo='usuario',
                                     comuna='sn bernardo',
                                     telefono='987675434',
                                     tipo='usuario'
                                     )
        persona.save()
        self.assertTrue(Persona,True)

    def test_val_rut(self):
        persona = Persona.objects.get(rut = '1-1')
        self.assertEquals(persona.rut,'1-1')
