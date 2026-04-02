# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         Discord.py Starter Kit                               ║
# ║                     Guided Bot — Documented & Labeled                        ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# This file demonstrates every common Discord message type with detailed
# comments explaining what each part does. Use this to learn, then refer
# to bot.py for the clean version you can copy-paste into your own projects.
#
# Prefix: ?
# Commands: ?text · ?embed · ?components · ?modals · ?ephemeral

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║          IMPORTS                                                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
import discord                  # The main discord.py library
from discord.ext import commands  # Extension that adds command support (prefix commands)
from dotenv import load_dotenv  # Reads variables from your .env file
import os                       # Lets us access environment variables

### Load Environment Variables
# load_dotenv() reads the .env file in the same folder and loads its values
# into the environment so we can access them with os.getenv().

load_dotenv()

### Create the Bot
# command_prefix : The character users type before a command (e.g. ?text)
# intents        : Permissions the bot requests from Discord's gateway. (you can edit this in https://discord.com/developers/applications) .default() covers most needs (messages, guilds, reactions).

bot = commands.Bot(command_prefix="?", intents=discord.Intents.default())


### Event: on_ready
# This prints in the console once when the bot successfully connects to Discord

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  1. PLAIN TEXT                                                               ║
# ║  Command: ?text                                                              ║
# ║  Sends a basic, unformatted text message to the channel                      ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

@bot.command(name="text")       # Registers ?text as a command
async def text(ctx):            # ctx = context — info about who/where the command was used
    await ctx.send("This is a plain text message.")
    # ctx.send() sends a message to the same channel the command was used in.


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  2. EMBED                                                                    ║
# ║  Command: ?embed                                                             ║
# ║  Sends a rich, structured message block with colors, fields, and images.     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

@bot.command(name="embed")
async def embed(ctx):
    # Create the embed object
    # title       : Bold clickable text at the top of the embed (max 256 characters)
    # url         : Makes the title a clickable hyperlink
    # description : Body text below the title (max 4096 characters)
    # color       : The colored stripe on the left side (hex color code)
    em = discord.Embed(
        title="This is your title, it can hold 256 characters",
        url="https://discord.js.org/#/docs/main/stable/class/MessageEmbed",
        description="This is the main body of text, it can hold 4096 characters.",
        color=0x3498DB,
    )

    # Author — shown at the very top of the embed, above the title
    # name     : The author text (max 256 characters)
    # icon_url : A small circular image next to the author name
    em.set_author(name="Author Name, it can hold 256 characters", icon_url="https://i.imgur.com/lm8s41J.png")

    # Thumbnail — small image in the top-right corner of the embed
    em.set_thumbnail(url="http://i.imgur.com/p2qNFag.png")

    # Field (non-inline) — takes the full width of the embed
    # name   : The bold label (max 256 characters)
    # value  : The text below the label (max 1024 characters)
    # inline : If False, the field takes the full width
    em.add_field(name="This is a single field title, it can hold 256 characters", value="This is a field value, it can hold 1024 characters.", inline=False)

    # Inline fields — sit side-by-side (up to 3 per row)
    # inline : If True, fields are displayed next to each other
    em.add_field(name="Inline fields", value="They can have different fields with small headlines.", inline=True)
    em.add_field(name="Masked links", value="You can put [masked links](https://google.com) inside of rich embeds.", inline=True)
    em.add_field(name="Markdown", value="You can put all the *usual* **__Markdown__** inside of them.", inline=True)

    # Image — large image displayed below the fields
    em.set_image(url="http://i.imgur.com/yVpymuV.png")

    # Footer — small text at the very bottom of the embed (max 2048 characters)
    # text     : The footer text
    # icon_url : A small image next to the footer text
    em.set_footer(text="This is the footer text, it can hold 2048 characters", icon_url="http://i.imgur.com/w1vhFSR.png")

    # Timestamp — displayed next to the footer text (shows as a date/time)
    em.timestamp = discord.utils.utcnow()

    # Send the embed by passing it to the embed= parameter
    await ctx.send(embed=em)


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  3. COMPONENTS (Buttons & Select Menus)                                      ║
# ║  Command: ?components                                                        ║
# ║  Sends interactive UI elements that users can click or select from           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# A "View" is a container that holds interactive components (buttons, menus)
# You define each component as a method inside the View class

class ComponentsView(discord.ui.View):

    ### Success Button (Green)
    # label : Text shown on the button
    # style : The button color/type:
    #         primary   = blue   (blurple)
    #         secondary = gray
    #         success   = green
    #         danger    = red
    #         link      = gray with URL (no callback, opens a link)
    # emoji : An emoji shown to the left of the label
    @discord.ui.button(label="Approve", style=discord.ButtonStyle.success, emoji="\u2705")
    async def approve_button(self, interaction, button):
        # interaction.response.send_message() replies to the button click
        # ephemeral=True means only the person who clicked can see the reply
        await interaction.response.send_message("You approved the request!", ephemeral=True)

    ### Danger Button (Red)
    @discord.ui.button(label="Deny", style=discord.ButtonStyle.danger, emoji="\u274C")
    async def deny_button(self, interaction, button):
        await interaction.response.send_message("You denied the request.", ephemeral=True)

    ### Primary Button (Blue)
    @discord.ui.button(label="More Info", style=discord.ButtonStyle.primary, emoji="\u2139\uFE0F")
    async def info_button(self, interaction, button):
        await interaction.response.send_message("Here is some additional info!", ephemeral=True)

    ### Link Button
    # Link buttons open a URL in the user's browser.
    # They do NOT trigger a callback — that's why the method body is empty
    # url : The link that opens when the button is clicked
    @discord.ui.button(label="Visit Website", style=discord.ButtonStyle.link, url="https://discord.com")
    async def link_button(self):
        pass

    ### Select Menu (Dropdown)    
    # placeholder : Gray text shown before a selection is made
    # options     : The list of choices in the dropdown
    #   label       : The text shown for each option
    #   description : Smaller text below the label
    #   emoji       : An emoji shown to the left of the option
    @discord.ui.select(
        placeholder="Pick your favorite color...",
        options=[
            discord.SelectOption(label="Red", description="The color of fire", emoji="\U0001F534"),
            discord.SelectOption(label="Green", description="The color of nature", emoji="\U0001F7E2"),
            discord.SelectOption(label="Blue", description="The color of the ocean", emoji="\U0001F535"),
        ],
    )
    async def select_callback(self, interaction, select):
        # select.values is a list of what the user selected
        await interaction.response.send_message(f"Your favorite color is **{select.values[0]}**!", ephemeral=True)


@bot.command(name="components")
async def components(ctx):
    # Attach the View to the message with view=
    await ctx.send("**Component Demo** \u2014 Try the buttons and menu below:", view=ComponentsView())


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  4. MODALS (Pop-up Forms)                                                    ║
# ║  Command: ?modals                                                            ║
# ║  Opens a pop-up form where users can type text input                         ║
# ║                                                                              ║
# ║  NOTE: Modals can ONLY be triggered from an interaction (button click,       ║
# ║  select menu, or slash command). They cannot be sent directly from a         ║
# ║  prefix command. That's why we use a button to open it.                      ║
# ║                                                                              ║
# ║  Example based on: https://docs.discordnet.dev/guides/int_basics/modals      ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# Define the modal (the pop-up form itself)
# title : The text shown at the very top of the pop-up window
class DemoModal(discord.ui.Modal, title="Title"):

    # TextInput — a text field inside the modal
    #
    # All available parameters:
    # label       : The label above the text box (shown in uppercase on Discord)
    # placeholder : Gray hint text inside the text box (disappears when typing)
    # style       : TextStyle.short = single line (default)
    #               TextStyle.long  = multi-line paragraph box
    # required    : If True (default), the user MUST fill this in to submit
    #               If False, the field is optional
    # min_length  : Minimum number of characters allowed
    # max_length  : Maximum number of characters allowed
    # default     : Pre-filled text that appears in the box

    ### Field 1: Basic Short Input (Required)
    # A single-line text input that is required (default behavior)
    # min_length=1, max_length=4000 shows the hint:
    #   "Must be between 1 and 4000 in length."
    text_input = discord.ui.TextInput(
        label="Text Input",
        placeholder="This is a basic text input.",
        min_length=1,
        max_length=4000,
    )

    ### Field 2: Paragraph Input (Optional) 
    # A multi-line paragraph box. required=False makes it optional.
    # The asterisk (*) next to the label disappears when required=False.
    longer_input = discord.ui.TextInput(
        label="Longer Input",
        style=discord.TextStyle.long,
        placeholder="This is a paragraph text input, that isn't required",
        required=False,
    )

    ### Field 3: Short Input with Min Length (Optional)
    # A short input that is NOT required, but IF the user types something,
    # it must be at least 15 characters. This shows the hint:
    #   "Must be between 15 and 4000 in length."
    another_input = discord.ui.TextInput(
        label="Another One??!",
        placeholder="This is a short input that isn't required and has a min length!",
        required=False,
        min_length=15,
        max_length=4000,
    )

    # on_submit runs when the user clicks the "Submit" button on the modal
    async def on_submit(self, interaction):
        # Access each field's value using self.<variable_name>
        # Fields the user left blank will be an empty string
        await interaction.response.send_message(
            f"**Modal Submitted!**\n"
            f"**Text Input:** {self.text_input}\n"
            f"**Longer Input:** {self.longer_input}\n"
            f"**Another One??!:** {self.another_input}",
            ephemeral=True,
        )


# A button view whose only job is to open the modal above
# Modals CANNOT be opened directly from a prefix command — they require an interaction (button, select menu, or slash command) to trigger them.
class ModalButton(discord.ui.View):
    @discord.ui.button(label="Open Modal", style=discord.ButtonStyle.success)
    async def modal_button(self, interaction, button):
        # Send the modal to the user who clicked the button
        await interaction.response.send_modal(DemoModal())


@bot.command(name="modals")
async def modals(ctx):
    # We send a message with a button; the button opens the modal
    await ctx.send("Click the button below to open the form:", view=ModalButton())


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  5. EPHEMERAL                                                                ║
# ║  Command: ?ephemeral                                                         ║
# ║  Sends a message that only the user who ran the command can see.             ║
# ║                                                                              ║
# ║  NOTE: True ephemeral messages (interaction.response.send_message with       ║
# ║  ephemeral=True) only work with interactions (slash commands, buttons).      ║
# ║  With prefix commands, ctx.send(ephemeral=True) is a close equivalent —      ║
# ║  it sends a message only visible to the command author.                      ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

@bot.command(name="ephemeral")
async def ephemeral(ctx):
    await ctx.send("Only you can see this message!", ephemeral=True, delete_after=None)
    # ephemeral=True  → Only the command author sees this message
    # delete_after    → How many seconds before auto-deleting (None = never)


### Run the Bot
# os.getenv("DISCORD_TOKEN") pulls the token from your .env file.
# NEVER paste your actual token directly into your code.

bot.run(os.getenv("DISCORD_TOKEN"))
