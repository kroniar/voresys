from celery import shared_task


@shared_task(bind=True)
def organization_scoped_placeholder(self, organization_id: int, task_id: str):
    """Foundation signature for future work; resolve tenant before any resource access."""
    return {"organization_id": organization_id, "task_id": task_id, "status": "not-implemented"}
