from django.db import models
import json



  
class probecalibration(models.Model):
    probe_id = models.CharField(max_length=50, unique=True)
    low_ref = models.JSONField(default=list)  # Storing a_values as a JSON array
    low_count = models.JSONField(default=list)  # Storing a1_values as a JSON array
    high_ref = models.JSONField(default=list)  # Storing b_values as a JSON array
    high_count = models.JSONField(default=list)  # Storing b1_values as a JSON array
    coefficent = models.JSONField(default=list)  # Storing e_values as a JSON array



class ItemData(models.Model):
    item_number = models.IntegerField()  # Identifier for the item
    data = models.TextField()  # Store item data as text

    def __str__(self):
        return f"Item {self.item_number}"



class TableOneData(models.Model):
    part_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    part_model = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)  # Ensure that 'id' is used as the primary key
    part_no = models.CharField(max_length=100)    
    is_selected = models.BooleanField(default=False)  # This field represents the checkbox state


class sonapariya(models.Model):
    model = models.ForeignKey(TableOneData, on_delete=models.CASCADE)
    parameter_name = models.CharField(max_length=100)


class TableTwoData(models.Model):
    batch_no = models.CharField(max_length=100)

class TableThreeData(models.Model):
    machine_no = models.CharField(max_length=100)
    machine_name = models.CharField(max_length=100)

class TableFourData(models.Model):
    operator_no = models.CharField(max_length=100)
    operator_name = models.CharField(max_length=100)

class TableFiveData(models.Model):
    vendor_code = models.CharField(max_length=100)
    email = models.EmailField()

class SavedData(models.Model):
    # Define your model fields here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as needed


class SavedParameter(models.Model):
    parameter_name = models.CharField(max_length=255)
    part_model = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.parameter_name} - {self.part_model}"
    
class paraname(models.Model):
    parameter_name = models.CharField(max_length=255)
        
class serverparameter(models.Model):
    model_name = models.CharField(max_length=255)
    parameter_name = models.CharField(max_length=255)

class viewvalues(models.Model):
    parameter_name = models.CharField(max_length=255)


class kanish(models.Model):
    model_name = models.ForeignKey(TableOneData, on_delete=models.CASCADE)
    parameter_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model_name.model_name} - {self.parameter_name}"    
    
class constvalue(models.Model):
    model_id = models.CharField(max_length=255)
    parameter_name = models.CharField(max_length=255)


class captvalues(models.Model):
    model_id = models.CharField(max_length=255)
    parameter_name = models.CharField(max_length=255)
    single_radio = models.BooleanField(default=False)
    analog_zero = models.FloatField(blank=True, null=True)
    reference_value = models.FloatField(blank=True, null=True)
    double_radio = models.BooleanField(default=False)
    high_mv = models.FloatField(blank=True, null=True)
    low_mv = models.FloatField(blank=True, null=True)    
    probe_no = models.FloatField()
    measurement_mode = models.CharField(max_length=50)
    nominal = models.FloatField()
    usl = models.FloatField()
    lsl = models.FloatField()
    mastering = models.FloatField()
    step_no = models.FloatField()
    hide_checkbox = models.BooleanField(default=False)
    sr_no = models.IntegerField(default=0)

def __str__(self):
        return f'{self.model_id} - {self.parameter_name}'
