import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model for create other system models."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CatalogModel(BaseModel):
    """Base catalog model for create other system catalogs models."""
    name = models.CharField(max_length=255)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
