import discord
from discord.ext import commands
import requests

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv('DISCORD_API_KEY')
CHANNEL_ID = 1333257844866285668
API_URL = 'http://127.0.0.1:8000/api/actualizar_estado/'  # Actualización del estado
INFO_API_URL = 'http://127.0.0.1:8000/api/tarea/{}/'      # Obtener información de la tarea

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

ESTADOS_VALIDOS = ['iniciado', 'en_proceso', 'Anclaje_completado', 'cancelado','completado', 'pendiente_revision', 'reprogramado']

FLUJO_ESTADOS = {
    'pendiente': 'iniciado',
    'iniciado': 'en_proceso',
    'en_proceso': ['completado', 'Anclaje_completado', 'cancelado', 'pendiente_revision', 'reasignado', 'reprogramado']
}

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

async def get_tarea_info(tarea_id):
    """Obtiene la información actual de la tarea desde la API."""
    try:
        response = requests.get(INFO_API_URL.format(tarea_id))
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.ConnectionError:
        return None

# Comando para actualizar el estado de la tarea

@client.command(name='actualizar_estado')
async def actualizar_estado(ctx, tarea_id: int, nuevo_estado: str):
    if nuevo_estado not in ESTADOS_VALIDOS:
        await ctx.send(f"⚠️ Estado inválido. Estados válidos: {', '.join(ESTADOS_VALIDOS)}")
        return
    
    # Obtener la información actual de la tarea
    tarea_info = await get_tarea_info(tarea_id)
    if not tarea_info:
        await ctx.send("❌ No se pudo obtener información de la tarea. Verifica el ID o la conexión a la API.")
        return
    
    estado_actual = tarea_info.get('estado', 'pendiente')
    actividad = tarea_info.get('actividad', '').lower()

    # Verificación del flujo de estados
    if estado_actual in FLUJO_ESTADOS:
        proximo_estado = FLUJO_ESTADOS[estado_actual]
        if isinstance(proximo_estado, list) and nuevo_estado not in proximo_estado:
            await ctx.send(f"⚠️ El estado **{nuevo_estado}** no es válido después de **{estado_actual}**.")
            return
        elif isinstance(proximo_estado, str) and nuevo_estado != proximo_estado:
            await ctx.send(f"⚠️ Debes pasar primero por el estado **{proximo_estado}**.")
            return
    
    # Verificación de actividad y restricción de estados
    if actividad == 'configuración' and nuevo_estado == 'Anclaje_completado':
        await ctx.send("⚠️ No puedes usar **Anclaje_completado** en una tarea con actividad **Configuración**.")
        return
    if actividad == 'anclaje' and nuevo_estado == 'completado':
        await ctx.send("⚠️ No puedes usar **completado** en una tarea con actividad **Anclaje**.")
        return
    
    # Si pasa las validaciones, enviamos la solicitud a la API
    data = {'id': tarea_id, 'estado': nuevo_estado}
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            await ctx.send(f"✅ Tarea **{tarea_id}** actualizada a **{nuevo_estado}** correctamente.")
        else:
            await ctx.send(f"❌ No se pudo actualizar la tarea. Detalle: {response.text}")
    except requests.ConnectionError:
        await ctx.send("🚫 No se pudo conectar con el servidor. Verifica que la API esté en línea.")
    except Exception as e:
        await ctx.send(f"❌ Error al actualizar la tarea: {e}")

client.run(TOKEN)

async def get_tarea_info(tarea_id):
    """Obtiene la información actual de la tarea desde la API."""
    try:
        url = INFO_API_URL.format(tarea_id)
        print(f"Consultando la URL: {url}")  # Depuración
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")  # Depuración
        print(f"Respuesta: {response.text}")  # Depuración completa
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.ConnectionError as e:
        print(f"Error de conexión: {e}")  # Depuración
        return None
