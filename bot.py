import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix="?", intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f"{bot.user} is online.")


# ── Plain Text ──

@bot.command(name="text")
async def text(ctx):
    await ctx.send("Hello! This is a plain text message.")


# ── Embed ──

@bot.command(name="embed")
async def embed(ctx):
    em = discord.Embed(
        title="This is your title, it can hold 256 characters",
        url="https://discord.js.org/#/docs/main/stable/class/MessageEmbed",
        description="This is the main body of text, it can hold 4096 characters.",
        color=0x3498DB,
    )
    em.set_author(name="Author Name, it can hold 256 characters", icon_url="https://i.imgur.com/lm8s41J.png")
    em.set_thumbnail(url="http://i.imgur.com/p2qNFag.png")
    em.add_field(name="This is a single field title, it can hold 256 characters", value="This is a field value, it can hold 1024 characters.", inline=False)
    em.add_field(name="Inline fields", value="They can have different fields with small headlines.", inline=True)
    em.add_field(name="Masked links", value="You can put [masked links](https://google.com) inside of rich embeds.", inline=True)
    em.add_field(name="Markdown", value="You can put all the *usual* **__Markdown__** inside of them.", inline=True)
    em.set_image(url="http://i.imgur.com/yVpymuV.png")
    em.set_footer(text="This is the footer text, it can hold 2048 characters", icon_url="http://i.imgur.com/w1vhFSR.png")
    em.timestamp = discord.utils.utcnow()
    await ctx.send(embed=em)


# ── Components (Buttons & Select Menu) ──

class ComponentsView(discord.ui.View):
    @discord.ui.button(label="Approve", style=discord.ButtonStyle.success, emoji="\u2705")
    async def approve_button(self, interaction, button):
        await interaction.response.send_message("You approved the request!", ephemeral=True)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.danger, emoji="\u274C")
    async def deny_button(self, interaction, button):
        await interaction.response.send_message("You denied the request.", ephemeral=True)

    @discord.ui.button(label="More Info", style=discord.ButtonStyle.primary, emoji="\u2139\uFE0F")
    async def info_button(self, interaction, button):
        await interaction.response.send_message("Here is some additional info!", ephemeral=True)

    @discord.ui.button(label="Visit Website", style=discord.ButtonStyle.link, url="https://discord.com")
    async def link_button(self):
        pass

    @discord.ui.select(
        placeholder="Pick your favorite color...",
        options=[
            discord.SelectOption(label="Red", description="The color of fire", emoji="\U0001F534"),
            discord.SelectOption(label="Green", description="The color of nature", emoji="\U0001F7E2"),
            discord.SelectOption(label="Blue", description="The color of the ocean", emoji="\U0001F535"),
        ],
    )
    async def select_callback(self, interaction, select):
        await interaction.response.send_message(f"Your favorite color is **{select.values[0]}**!", ephemeral=True)


@bot.command(name="components")
async def components(ctx):
    await ctx.send("**Component Demo** — Try the buttons and menu below:", view=ComponentsView())


# ── Modals ──

class DemoModal(discord.ui.Modal, title="Title"):
    text_input = discord.ui.TextInput(
        label="Text Input",
        placeholder="This is a basic text input.",
        min_length=1,
        max_length=4000,
    )
    longer_input = discord.ui.TextInput(
        label="Longer Input",
        style=discord.TextStyle.long,
        placeholder="This is a paragraph text input, that isn't required",
        required=False,
    )
    another_input = discord.ui.TextInput(
        label="Another One??!",
        placeholder="This is a short input that isn't required and has a min length!",
        required=False,
        min_length=15,
        max_length=4000,
    )

    async def on_submit(self, interaction):
        await interaction.response.send_message(
            f"**Modal Submitted!**\n"
            f"**Text Input:** {self.text_input}\n"
            f"**Longer Input:** {self.longer_input}\n"
            f"**Another One??!:** {self.another_input}",
            ephemeral=True,
        )


class ModalButton(discord.ui.View):
    @discord.ui.button(label="Open Modal", style=discord.ButtonStyle.success)
    async def modal_button(self, interaction, button):
        await interaction.response.send_modal(DemoModal())


@bot.command(name="modals")
async def modals(ctx):
    await ctx.send("Click the button below to open the form:", view=ModalButton())


# ── Ephemeral ──

@bot.command(name="ephemeral")
async def ephemeral(ctx):
    await ctx.send("Only you can see this message!", ephemeral=True, delete_after=None)


bot.run(os.getenv("DISCORD_TOKEN"))
