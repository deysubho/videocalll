import uuid
from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return self.username

class Call(models.Model):
    call_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call {self.call_id}"

class CallLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    call_runtime = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.call.call_id}"