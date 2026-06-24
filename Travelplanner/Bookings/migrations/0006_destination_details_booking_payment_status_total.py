# Generated manually to align destination and booking data with the landing page.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0005_accommodation_user_destination_user_vehicle_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='category',
            field=models.CharField(choices=[('coastal', 'Coastal'), ('safari', 'Safari'), ('historical', 'Historical Tour'), ('backpacking', 'Backpacking')], default='coastal', max_length=20),
        ),
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='estimated_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Card'), ('mobile_money', 'Mobile Money'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash')], default='mobile_money', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
