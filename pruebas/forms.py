from django import forms
from auth.models import User, Group
from pruebas.models import Detalle


class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
    def save(self, commit=True):
        model = super(DetalleForm, self).save(commit=False)
 
        model.precio = 0 
        model.precio += self.cleaned_data['precio']+133

        if commit:
            model.save()
 
        return model 


class PresupuestoForm(forms.ModelForm):
   def save(self, commit=True):
        model = super(PresupuestoForm, self).save(commit=False)
        #esto no anda, actualiza el list_display en admin pero no en modelo, por q?????!!!!!!!!

        model.total =model.totalPresupuesto()
       
        #while (count < aux ):
        #   model.total =
        #   aux = aux+1
   
        # Save the latitude and longitude based on the form fields
        #model.total =10 #self.cleaned_data['limpieza_obra'] + self.cleaned_data['tareas'] + self.cleaned_data['suelo']
         
        #model.totalHormigon= self.cleaned_data['bases']+self.cleaned_data['vigas_fundacion']+self.cleaned_data['columnas']+self.cleaned_data['vigas_encadenado']+self.cleaned_data['piso']
 
        if commit:
            model.save()
 
        return model 




