from django.db import migrations, models
import django.db.models.deletion


def seed_booking_options(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Location = apps.get_model('Bookings', 'Location')
    Destination = apps.get_model('Bookings', 'Destination')
    Accommodation = apps.get_model('Bookings', 'Accommodation')
    Vehicle = apps.get_model('Bookings', 'Vehicle')

    user, _ = User.objects.get_or_create(
        username='wonderwaves_seed',
        defaults={'email': 'bookings@wonderwaves.local'},
    )

    location_names = [
        'Diani',
        'Mombasa',
        'Malindi',
        'Lamu',
        'Maasai Mara',
        'Mount Kenya',
        'Lake Nakuru',
        'Nairobi',
    ]
    locations = {}

    for name in location_names:
        locations[name], _ = Location.objects.get_or_create(name=name)

    destinations = [
        ('Diani Beach', 'Diani', 'coastal', 'Soft sand, snorkeling, beach resorts, and south coast sunsets.', '18500.00'),
        ('Fort Jesus', 'Mombasa', 'historical', 'A coastal heritage tour through Mombasa Old Town and Fort Jesus.', '12000.00'),
        ('Malindi Marine Park', 'Malindi', 'coastal', 'Marine parks, golden beaches, and relaxed seaside days.', '16800.00'),
        ('Lamu Island', 'Lamu', 'historical', 'Dhow trips, Swahili architecture, and quiet waterfront stays.', '24000.00'),
        ('Maasai Mara Reserve', 'Maasai Mara', 'safari', 'Open savannah drives, wildlife viewing, and lodge stays.', '32000.00'),
        ('Mount Kenya Trail', 'Mount Kenya', 'backpacking', 'Forest trails, guided hikes, and mountain adventure routes.', '26000.00'),
        ('Lake Nakuru National Park', 'Lake Nakuru', 'safari', 'Birdwatching, rhino sightings, and lakeside drives.', '21000.00'),
        ('Nairobi National Park', 'Nairobi', 'safari', 'A city-side wildlife escape with easy transfer access.', '14500.00'),
    ]

    for name, location_name, category, description, price in destinations:
        destination, _ = Destination.objects.get_or_create(
            name=name,
            location=locations[location_name],
            defaults={'user': user},
        )
        destination.user = user
        destination.category = category
        destination.description = description
        destination.estimated_price = price
        destination.save()

    accommodations = [
        ('Diani Reef Hotel', 'Diani', 'hotel', '9500.00'),
        ('Diani Beach Airbnb Villa', 'Diani', 'airbnb', '7200.00'),
        ('Mombasa Ocean Hotel', 'Mombasa', 'hotel', '8200.00'),
        ('Nyali Airbnb Apartment', 'Mombasa', 'airbnb', '5800.00'),
        ('Malindi Bay Hotel', 'Malindi', 'hotel', '8800.00'),
        ('Malindi Garden Airbnb', 'Malindi', 'airbnb', '6400.00'),
        ('Lamu Seafront Hotel', 'Lamu', 'hotel', '11000.00'),
        ('Lamu Old Town Airbnb', 'Lamu', 'airbnb', '7900.00'),
        ('Mara Safari Lodge', 'Maasai Mara', 'hotel', '14500.00'),
        ('Mara Camp Airbnb', 'Maasai Mara', 'airbnb', '9800.00'),
        ('Mount Kenya Lodge', 'Mount Kenya', 'hotel', '12000.00'),
        ('Nanyuki Airbnb Cabin', 'Mount Kenya', 'airbnb', '7600.00'),
        ('Nakuru Lake Hotel', 'Lake Nakuru', 'hotel', '9000.00'),
        ('Nakuru Town Airbnb', 'Lake Nakuru', 'airbnb', '5200.00'),
        ('Nairobi Safari Hotel', 'Nairobi', 'hotel', '10000.00'),
        ('Nairobi Westlands Airbnb', 'Nairobi', 'airbnb', '6800.00'),
    ]

    for name, location_name, stay_type, price in accommodations:
        accommodation, _ = Accommodation.objects.get_or_create(
            name=name,
            location=locations[location_name],
            defaults={'user': user, 'type': stay_type, 'price_per_night': price},
        )
        accommodation.user = user
        accommodation.type = stay_type
        accommodation.price_per_night = price
        accommodation.save()

    vehicles = [
        ('Diani SUV Cruiser', 'Diani', 'suv', 5, '6500.00'),
        ('Diani Family Van', 'Diani', 'van', 8, '9000.00'),
        ('Mombasa Coast SUV', 'Mombasa', 'suv', 5, '6200.00'),
        ('Mombasa Group Bus', 'Mombasa', 'bus', 30, '18000.00'),
        ('Malindi Beach Van', 'Malindi', 'van', 8, '8500.00'),
        ('Malindi SUV Hire', 'Malindi', 'suv', 5, '6300.00'),
        ('Lamu Transfer Van', 'Lamu', 'van', 8, '7800.00'),
        ('Mara Safari SUV', 'Maasai Mara', 'suv', 6, '12000.00'),
        ('Mara Tour Bus', 'Maasai Mara', 'bus', 32, '22000.00'),
        ('Mount Kenya SUV', 'Mount Kenya', 'suv', 5, '9800.00'),
        ('Mount Kenya Trek Van', 'Mount Kenya', 'van', 10, '11500.00'),
        ('Nakuru SUV Hire', 'Lake Nakuru', 'suv', 5, '7000.00'),
        ('Nakuru Tour Bus', 'Lake Nakuru', 'bus', 30, '19000.00'),
        ('Nairobi City SUV', 'Nairobi', 'suv', 5, '6000.00'),
        ('Nairobi Shuttle Van', 'Nairobi', 'van', 10, '8000.00'),
        ('Nairobi Group Bus', 'Nairobi', 'bus', 35, '20000.00'),
    ]

    for name, location_name, vehicle_type, capacity, price in vehicles:
        vehicle, _ = Vehicle.objects.get_or_create(
            name=name,
            defaults={
                'user': user,
                'location': locations[location_name],
                'vehicle_type': vehicle_type,
                'capacity': capacity,
                'price_per_day': price,
            },
        )
        vehicle.user = user
        vehicle.location = locations[location_name]
        vehicle.vehicle_type = vehicle_type
        vehicle.capacity = capacity
        vehicle.price_per_day = price
        vehicle.save()


def unseed_booking_options(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0006_destination_details_booking_payment_status_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bookings.location'),
        ),
        migrations.RunPython(seed_booking_options, unseed_booking_options),
    ]
