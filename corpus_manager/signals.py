import asyncio
import aiohttp
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ParallelText

API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi"
headers = {
    "Authorization": "Bearer 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"
}

async def query(payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=headers, json=payload) as response:
            return await response.json()

@receiver(post_save, sender=ParallelText)
def post_save_operation(sender, instance, created, **kwargs):
    if created:
        print("A new item has been inserted into the database.")

        empty_hi_text_rows = ParallelText.objects.filter(hi_text__exact="")

        data = {
            "inputs": [i for i in empty_hi_text_rows.values_list("en_text", flat=True)]
        }

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        output = loop.run_until_complete(query(data))

        output = [i['translation_text'] for i in output]

        for obj, translation in zip(empty_hi_text_rows, output):
            obj.hi_text = translation
            obj.save()
        print("The Hindi translations have been added to the database.")
