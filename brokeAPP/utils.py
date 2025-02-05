from mailjet_rest import Client
from django.conf import settings


MAILJET_API_KEY = '84fcb24e7287379c43123e6b882746a7'
MAILJET_API_SECRET = '3fd7b61ca969df6e54209c67da69313e'


def enviar_correo_mailjet(destinatario, asunto, mensaje, archivo_adjunto_b64=None, archivo_nombre=None):
    mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')
    email_data = {
        'Messages': [
            {
                "From": {
                    "Email": "pepeulmo@gmail.com",
                    "Name": "brokeee"
                },
                "To": [
                    {
                        "Email": destinatario,
                        "Name": "Destinatario"
                    }
                ],
                "Subject": asunto,
                "TextPart": mensaje,
                "HTMLPart": f"<p>{mensaje}</p>"
            }
        ]
    }

    if archivo_adjunto_b64 and archivo_nombre:
        email_data['Messages'][0]['Attachments'] = [
            {
                "ContentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "Filename": archivo_nombre,
                "Base64Content": archivo_adjunto_b64
            }
        ]

    result = mailjet.send.create(data=email_data)
    return result.status_code == 200