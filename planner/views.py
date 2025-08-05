from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Location
from .optimization import calculate_optimal_route
from django.contrib import messages
from django.conf import settings
import json
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import io

def home(request):
    trips = Trip.objects.all().order_by('-created_at')
    return render(request, 'planner/home.html', {'trips': trips})

def plan_trip(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_location = request.POST.get('start_location')
        locations = request.POST.getlist('locations[]')
        lats = request.POST.getlist('lat[]')
        lngs = request.POST.getlist('lng[]')
        start_lat = request.POST.get('start_lat')
        start_lng = request.POST.get('start_lng')
        
        if title and start_location and locations and all([lats, lngs, start_lat, start_lng]):
            trip = Trip.objects.create(
                title=title,
                start_location=start_location
            )
            
            # Create start location
            start = Location.objects.create(
                trip=trip,
                name=start_location,
                address=start_location,
                latitude=float(start_lat),
                longitude=float(start_lng),
                order=0
            )
            
            # Create location objects
            location_objects = [start]
            for i, (loc_name, lat, lng) in enumerate(zip(locations, lats, lngs), 1):
                location = Location.objects.create(
                    trip=trip,
                    name=loc_name,
                    address=loc_name,  # We can enhance this by getting formatted address from Google Places
                    latitude=float(lat),
                    longitude=float(lng),
                    order=i
                )
                location_objects.append(location)
            
            # Calculate optimal route
            optimal_route = calculate_optimal_route(location_objects)
            
            # Update order based on optimal route
            for i, location in enumerate(optimal_route):
                location.order = i
                location.save()
            
            return redirect('view_itinerary', trip_id=trip.id)
        else:
            messages.error(request, 'Please fill all required fields and select locations from suggestions')
    
    return render(request, 'planner/plan_trip.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def view_itinerary(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    locations = trip.locations.all()
    
    # Prepare locations for JSON
    locations_data = [{
        'name': loc.name,
        'address': loc.address,
        'latitude': loc.latitude,
        'longitude': loc.longitude
    } for loc in locations]
    
    return render(request, 'planner/view_itinerary.html', {
        'trip': trip,
        'locations': locations,
        'locations_json': json.dumps(locations_data),
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def download_pdf(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    locations = trip.locations.all()
    
    # Create the PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    elements.append(Paragraph(trip.title, title_style))
    elements.append(Spacer(1, 12))
    
    # Starting point
    elements.append(Paragraph(f"Starting Location: {trip.start_location}", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    # Locations table
    data = [['Stop', 'Location', 'Address']]
    for i, loc in enumerate(locations, 1):
        data.append([str(i), loc.name, loc.address])
    
    table = Table(data, colWidths=[40, 200, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)
    
    # Build PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{trip.title}_itinerary.pdf"'
    response.write(pdf)
    
    return response
        'locations': locations
    })
