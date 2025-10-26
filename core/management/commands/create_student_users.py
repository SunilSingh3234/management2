from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Student
User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample User accounts for existing Student records. Password is "studentpass" for all created users.'

    def handle(self, *args, **options):
        students = Student.objects.filter(user__isnull=True)[:50]
        if not students:
            self.stdout.write(self.style.WARNING('No students without users found.'))
            return
        for i, s in enumerate(students, start=1):
            username = f"student{i}"
            if User.objects.filter(username=username).exists():
                self.stdout.write(f"User {username} exists, skipping.")
                continue
            user = User.objects.create(username=username, email=(s.email or f'{username}@example.com'))
            user.set_password('studentpass')
            user.save()
            s.user = user
            s.save()
            self.stdout.write(self.style.SUCCESS(f'Created user {username} for student {s.enrollment_no}'))
        self.stdout.write(self.style.SUCCESS('Done. All created users have password "studentpass".'))
