from typing import Any
import helpers
from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDORS_DIR = getattr(settings, 'STATICFILES_VENDORS_DIR')


VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map",

}

class Command(BaseCommand):
        
        def handle(self , *args, **options : Any):
            self.stdout.write("Starting vendor pull...")
            completed_urls = []
            for name , url in VENDOR_STATICFILES.items():
                    out_path = STATICFILES_VENDORS_DIR / name
                    dl_success = helpers.download_to_local(url, out_path)
                    if dl_success:
                        completed_urls.append(url)
                    else:
                          self.stdout.write(
                                self.style.ERROR(f"Failed to download {url} to {out_path}")
                                )
            if set(completed_urls) == set(VENDOR_STATICFILES.values()):
                self.stdout.write(
                     self.style.SUCCESS("All vendor files downloaded successfully.")
                     )

            else:
                self.stdout.write(
                                self.style.WARNING("Some vendor files failed to download. Please check the logs.")
                            )
