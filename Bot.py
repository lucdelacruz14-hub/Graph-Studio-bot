import discord
import replicate
import os

# ⚠️ REMPLACE CES DEUX LIGNES PAR TES PROPRES CLÉS ⚠️

os.environ["REPLICATE_API_TOKEN"] = "

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Graph Studio est prêt ! Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Commande pour les LOGOS (format carré 1:1)
    if message.content.startswith('!logo '):
        prompt = message.content[6:]
        await message.channel.send(f"🎨 **Graph Studio** génère ton logo... (Patientez ~10s)")
        
        try:
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={
                    "prompt": f"3D logo design, {prompt}, extruded, bevel, metallic texture, rim light, neon glow, dark gradient background, octane render, unreal engine 5, high contrast, sharp edges, 8k",
                    "aspect_ratio": "1:1",
                    "output_format": "png"
                }
            )
            embed = discord.Embed(title="✨ Logo généré par Graph Studio", color=0xff00ff)
            embed.set_image(url=output[0])
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f"❌ Erreur : {e}")

    # Commande pour les BANNIÈRES (format 16:9 pour Discord/RageUI)
    elif message.content.startswith('!banniere '):
        prompt = message.content[10:]
        await message.channel.send(f"🎨 **Graph Studio** génère ta bannière FiveM... (Patientez ~10s)")
        
        try:
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={
                    "prompt": f"cinematic gaming banner, {prompt}, smoke effects, neon lighting, depth of field, dynamic composition, octane render, unreal engine 5, 8k",
                    "aspect_ratio": "16:9",
                    "output_format": "png"
                }
            )
            embed = discord.Embed(title="✨ Bannière générée par Graph Studio", color=0x00ffff)
            embed.set_image(url=output[0])
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f"❌ Erreur : {e}")

client.run(DISCORD_TOKEN)
