from django.db import migrations, models


def upload_to(instance, filename):
    return f"uploads/{instance.customer_name}/{filename}"


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254, db_index=True)),
                ("customer_name", models.CharField(max_length=100, db_index=True)),
                ("attachment", models.FileField(upload_to=upload_to, blank=True, null=True)),
                (
                    "request_type",
                    models.CharField(
                        max_length=50,
                        choices=[
                            ("Technical Support", "Technical Support"),
                            ("Billing", "Billing"),
                            ("General Inquiry", "General Inquiry"),
                        ],
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        max_length=50,
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In Progress"),
                            ("Resolved", "Resolved"),
                            ("Closed", "Closed"),
                        ],
                        default="Pending",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
