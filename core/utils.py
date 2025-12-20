from urllib.parse import urlparse
from django.core.exceptions import ValidationError

def validate_cloud_storage_url(value):
    """
    Validator to ensure URLs are from trusted cloud storage domains.
    """
    trusted_domains = [
        'drive.google.com',
        'dropbox.com',
        'onedrive.live.com',
        's3.amazonaws.com',
        'storage.googleapis.com',
    ]
    
    parsed_url = urlparse(value)
    domain = parsed_url.netloc
    
    if not any(domain.endswith(trusted) for trusted in trusted_domains):
        raise ValidationError(
            f"URL must be from a trusted cloud storage provider. Trusted domains are: {', '.join(trusted_domains)}"
        )
