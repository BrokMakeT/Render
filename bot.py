import discord
from discord.ext import commands
import requests
import os

# Cargar el token de Discord desde la variable de entorno
TOKEN = os.getenv('DISCORD_API_KEY')
if not TOKEN:
    raise ValueError("❌ No se encontró el token de Discord. Asegúrate de configurarlo en las variables de entorno.")

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

# URLs de la API
API_URL = 'http://127.0.0.1:8000/api/actualizar_estado/'
INFO_API_URL = 'http://127.0.0.1:8000/api/tarea/{}/'

# Lista de estados válidos y flujo de estados
ESTADOS_VALIDOS = ['iniciado', 'en_proceso', 'Anclaje_completado', 'cancelado', 'completado', 'pendiente_revision', 'reprogramado']
FLUJO_ESTADOS = {
    'pendiente': 'iniciado',
    'iniciado': 'en_proceso',
    'en_proceso': ['completado', 'Anclaje_completado', 'cancelado', 'pendiente_revision', 'reasignado', 'reprogramado']
}

# Evento cuando el bot se conecta
@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    print(f'Comandos cargados: {list(client.commands)}')

# Función para obtener información de la tarea desde la API
async def get_tarea_info(tarea_id):
    try:
        response = requests.get(INFO_API_URL.format(tarea_id))
        if response.status_code == 200:
            return response.json()
        return None
    except requests.ConnectionError:
        return None

# Comando para actualizar el estado de la tarea
@client.command(name='actualizar_estado')
async def actualizar_estado(ctx, tarea_id: int, nuevo_estado: str):
    if nuevo_estado not in ESTADOS_VALIDOS:
        await ctx.send(f"⚠️ Estado inválido. Estados válidos: {', '.join(ESTADOS_VALIDOS)}")
        return

    # Obtener información de la tarea
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

    # Restricciones de estados según la actividad
    if actividad == 'configuración' and nuevo_estado == 'Anclaje_completado':
        await ctx.send("⚠️ No puedes usar **Anclaje_completado** en una tarea con actividad **Configuración**.")
        return
    if actividad == 'anclaje' and nuevo_estado == 'completado':
        await ctx.send("⚠️ No puedes usar **completado** en una tarea con actividad **Anclaje**.")
        return

    # Enviar la actualización a la API
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

# Iniciar el bot (solo una vez, al final del archivo)
client.run(TOKEN)
