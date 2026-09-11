from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [("auth", "0012_alter_user_first_name_max_length")]
    operations = [
        migrations.CreateModel(name="Organization", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=120)), ("slug", models.SlugField(max_length=140, unique=True)), ("created_at", models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name="Permission", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("code", models.CharField(max_length=80, unique=True)), ("name", models.CharField(max_length=120))]),
        migrations.CreateModel(name="Role", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=40)), ("organization", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="roles", to="organizations.organization")), ("permissions", models.ManyToManyField(blank=True, related_name="roles", to="organizations.permission"))]),
        migrations.CreateModel(name="Membership", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("created_at", models.DateTimeField(auto_now_add=True)), ("organization", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="memberships", to="organizations.organization")), ("role", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="memberships", to="organizations.role")), ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="memberships", to="auth.user"))]),
        migrations.AddConstraint(model_name="role", constraint=models.UniqueConstraint(fields=("organization", "name"), name="unique_role_per_organization")),
        migrations.AddConstraint(model_name="membership", constraint=models.UniqueConstraint(fields=("user", "organization"), name="unique_organization_membership")),
    ]
