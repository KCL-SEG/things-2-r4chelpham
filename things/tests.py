from django.test import TestCase
from .forms import ThingForm
# Create your tests here.

class ThingFormTestCase(TestCase):
    def setUp(self):
        self.form_input={
            'name': "John Doe",
            'description': "this is a description",
            'quantity': 30
            }
        
    def test_valid_thing_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)

    def test_form_uses_model_validation(self):
        self.form_input['quantity'] = 51
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

