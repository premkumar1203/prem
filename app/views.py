import threading
from django.http import JsonResponse
from django.shortcuts import render
from pyexpat.errors import messages
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login
import serial.tools.list_ports
import threading
import serial
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from.models import probecalibration,SavedData
from .models import TableOneData, TableTwoData, TableThreeData, TableFourData, TableFiveData
from django.shortcuts import get_object_or_404
from .models import constvalue
from django.views.decorators.http import require_POST

import json


def home(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        if username == 'admin' and password == 'admin':
            # Redirect to the index page if credentials are correct
            return redirect('index')  # 'index' is the name of the URL pattern for your index page
        else:
            # If the username and password don't match, display an error message
            messages.error(request, 'Invalid username or password')

    return render(request, "app/home.html")



# Use a lock to ensure thread safety when accessing serial_data
serial_data = ""
serial_data_lock = threading.Lock()

serial_thread = None

def read_serial_data(ser):
    global serial_data
    while True:
        try:
            receive = ser.read().decode('ASCII')
            with serial_data_lock:
                serial_data += receive
        except Exception as e:
            # Handle exceptions or log errors here
            pass

@csrf_exempt
def comport(request):
    global serial_thread

    if request.method == 'POST':
        selected_com_port = request.POST.get('com_port')
        selected_baud_rate = request.POST.get('baud_rate')

        try:
            ser = serial.Serial(port=selected_com_port, baudrate=int(selected_baud_rate), bytesize=8, timeout=None, stopbits=1, parity='N')

            # Check if the serial thread is not running, then start it
            if serial_thread is None or not serial_thread.is_alive():
                serial_thread = threading.Thread(target=read_serial_data, args=(ser,))
                serial_thread.daemon = True
                serial_thread.start()

        except Exception as e:
            return JsonResponse({'error': str(e)})

    com_ports = [port.device for port in serial.tools.list_ports.comports()]
    baud_rates = ["4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000"]

    with serial_data_lock:
        data_to_display = serial_data

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'serial_data': data_to_display})

    return render(request, 'app/comport.html', {'com_ports': com_ports, 'baud_rates': baud_rates, 'serial_data': data_to_display})


 

def index(request):
    return render(request,'app/index.html')





def probe1(request):
    if request.method == 'POST':
        probe_id = request.POST.get('probeId')
        a_values = [float(value) for value in request.POST.getlist('a[]')]
        a1_values = [float(value) for value in request.POST.getlist('a1[]')]
        b_values = [float(value) for value in request.POST.getlist('b[]')]
        b1_values = [float(value) for value in request.POST.getlist('b1[]')]
        e_values = [float(value) for value in request.POST.getlist('e[]')]

        print('THESE ARE THE DATA YOU WANT TO DISPLAY:', probe_id, a_values, a1_values, b_values, b1_values, e_values)

        probe, created = probecalibration.objects.get_or_create(probe_id=probe_id)

        probe.low_ref = a_values[0] if a_values else None
        probe.low_count = a1_values[0] if a1_values else None
        probe.high_ref = b_values[0] if b_values else None
        probe.high_count = b1_values[0] if b1_values else None
        probe.coefficent = e_values[0] if e_values else None

        probe.save()


    with serial_data_lock:
        data_to_display = serial_data

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Split the serial data into 11 channels (A-K) using regular expressions
        parts = re.split(r'([A-K])', data_to_display)
        parts = [part for part in parts if part.strip()]  # Remove empty strings

        # Create a dictionary to store data for each channel
        channel_data = {}
        for channel_id, part in zip(parts[0::2], parts[1::2]):
            part = part.replace('+', '')
            channel_data[channel_id] = part

        # Return the channel data as JSON response
        return JsonResponse({'serial_data': channel_data})

    return render(request, 'app/probe/probe1.html', {'serial_data': data_to_display})


def probe2(request):
    if request.method == 'POST':
        probe_id = request.POST.get('probeId')
        a_values = [float(value) for value in request.POST.getlist('a[]')]
        a1_values = [float(value) for value in request.POST.getlist('a1[]')]
        b_values = [float(value) for value in request.POST.getlist('b[]')]
        b1_values = [float(value) for value in request.POST.getlist('b1[]')]
        e_values = [float(value) for value in request.POST.getlist('e[]')]

        print('THESE ARE THE DATA YOU WANT TO DISPLAY:', probe_id, a_values, a1_values, b_values, b1_values, e_values)

        probe, created = probecalibration.objects.get_or_create(probe_id=probe_id)

        probe.low_ref = a_values[0] if a_values else None
        probe.low_count = a1_values[0] if a1_values else None
        probe.high_ref = b_values[0] if b_values else None
        probe.high_count = b1_values[0] if b1_values else None
        probe.coefficent = e_values[0] if e_values else None

        probe.save()

    with serial_data_lock:
        data_to_display = serial_data

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Split the serial data into 11 channels (A-K) using regular expressions
        parts = re.split(r'([A-K])', data_to_display)
        parts = [part for part in parts if part.strip()]  # Remove empty strings

        # Create a dictionary to store data for each channel
        channel_data = {}
        for channel_id, part in zip(parts[0::2], parts[1::2]):
            part = part.replace('+', '')
            channel_data[channel_id] = part

        # Return the channel data as JSON response
        return JsonResponse({'serial_data': channel_data})

    return render(request, 'app/probe/probe2.html', {'serial_data': data_to_display})


def probe3(request):
    return render(request,'app/probe/probe3.html')
def probe4(request):
    return render(request,'app/probe/probe4.html')
def probe5(request):
    return render(request,'app/probe/probe5.html')
def probe6(request):
    return render(request,'app/probe/probe6.html')

def probe(request):
    return render(request,'app/probe.html')




@csrf_exempt
def trace(request, row_id=None):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            print(f'received_data',request.body)

            # Process received_data and save to the database for each table
            for item_id, rows in received_data.items():
                for row in rows:
                    values = row['values']

                    if item_id == 'tableBody-1':
                        table_data = TableOneData.objects.create(
                            part_name=values[0],
                            customer_name=values[1],
                            part_model=values[2],
                            part_no=values[3]
                        )
                        table_data.save()

                    elif item_id == 'tableBody-2':
                        table_data = TableTwoData.objects.create(
                            batch_no=values[0]
                        )
                        table_data.save()

                    elif item_id == 'tableBody-3':
                        table_data = TableThreeData.objects.create(
                            machine_no=values[0],
                            machine_name=values[1]
                        )
                        table_data.save()

                    elif item_id == 'tableBody-4':
                        table_data = TableFourData.objects.create(
                            operator_no=values[0],
                            operator_name=values[1]
                        )
                        table_data.save()

                    elif item_id == 'tableBody-5':
                        table_data = TableFiveData.objects.create(
                            vendor_code=values[0],
                            email=values[1]
                        )
                        table_data.save()

            return JsonResponse({'message': 'Data received and saved successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    elif request.method == 'GET':
        try:
            # Fetch stored data for tableBody-1 from your database or any storage mechanism
            # Replace this with your actual logic to fetch data for tableBody-1
            table_body_1_data = TableOneData.objects.all()
            table_body_2_data = TableTwoData.objects.all()
            table_body_3_data = TableThreeData.objects.all()
            table_body_4_data = TableFourData.objects.all()
            table_body_5_data = TableFiveData.objects.all()
            # Pass the retrieved data for tableBody-1 to the template for rendering
            return render(request, 'app/trace.html', {'table_body_1_data': table_body_1_data,'table_body_2_data':table_body_2_data,'table_body_3_data': table_body_3_data,'table_body_4_data': table_body_4_data,'table_body_5_data': table_body_5_data})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            received_data = json.loads(request.body)

            for item_id, row_ids in received_data.items():
                if item_id == 'tableBody-1':
                    TableOneData.objects.filter(id__in=row_ids).delete()
                elif item_id == 'tableBody-2':
                    TableTwoData.objects.filter(id__in=row_ids).delete()
                elif item_id == 'tableBody-3':
                    TableThreeData.objects.filter(id__in=row_ids).delete()
                elif item_id == 'tableBody-4':
                    TableFourData.objects.filter(id__in=row_ids).delete()
                elif item_id == 'tableBody-5':
                    TableFiveData.objects.filter(id__in=row_ids).delete()

            return JsonResponse({'message': 'Data deleted successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



                                
    else:
        return render(request, 'app/trace.html')







            





@csrf_exempt
def parameter(request):
    if request.method == 'GET':
        try:

            table_body_1_data = TableOneData.objects.all()

            # Dynamically filter constvalue objects based on the model_id parameter
            model_id = request.GET.get('model_name')

            print('your selected model from web page is:', model_id)

            if model_id:
                # Filter constvalue objects based on the model_id
                paraname = constvalue.objects.filter(model_id=model_id).values('parameter_name')
                print('your filtered values are:', paraname)

                # Return filtered parameter names as JSON
                return JsonResponse({'paraname': list(paraname)})
            else:
                paraname = []  # If no model is selected, set paraname to an empty list

            return render(request, 'app/parameter.html', {
                'table_body_1_data': table_body_1_data,
                'paraname': paraname,
                'selected_model_id': model_id,
            })
        

        except Exception as e:
            print(f'Exception: {e}')
            return HttpResponse(f'Error: {str(e)}', status=500)


    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(f'Your values to get from frontend: {request.body}')

            model_id = data.get('modelId')
            print('Model ID:', model_id)

            parameter_value = data.get('parameterValue')
            print('Parameter Name:', parameter_value)
            

            # Create a ConstValue instance associated with the selected model
            const_value_instance = constvalue.objects.create(model_id=model_id, parameter_name=parameter_value)
            print("Your values in my server:", const_value_instance)    
            const_value_instance.save()

            

            return JsonResponse({'success': True, 'message': 'Data saved successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return render(request, 'app/parameter.html')
