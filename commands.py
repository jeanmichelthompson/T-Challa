from openai_client import get_coach_reply

# Dictionary to map commands to their respective responses and descriptions, grouped by category
CATEGORIZED_COMMANDS = {
    "Helpful Links": {
        "!youtube": (
            "https://www.youtube.com/@karkatsg",
            "YouTube channel link"
        ),
        "!twitch": (
            "https://www.twitch.tv/karkatsg",
            "Twitch channel link"
        ),
        "!discord": (
            "https://discord.gg/zq5eznZXVd",
            "Discord invite link"
        ),
        "!twitter": (
            "https://twitter.com/karkatsg",
            "Twitter profile link"
        ),
        "!vodchannel": (
            "https://www.youtube.com/channel/UC00t1W6BxLr0vJoxwLO0O4A/",
            "VOD Channel Link"
        ),
        "!guide": (
            "https://www.youtube.com/watch?v=KHpABbvMSXc",
            "Link to the Panther guide"
        ),
        "!dive": (
            "https://youtu.be/_N3jwHmMgxU",
            "Link to the Dive guide"
        ),
        "!positioning": (
            "https://youtu.be/x8M1Dji02Yk",
            "Link to the Positioning guide"
        ),
        "!mechanics": (
            "https://youtu.be/BcDYSeJcM2w",
            "Link to the Advanced Mechanics guide"
        ),
        "!mentality": (
            "https://youtu.be/7qvFBjG8wIU",
            "Link to the Mentality guide"
        ),
    },
    "FAQs": {
        "!ban": (
            "So far, he's won in high elo on venom, captain america, starlord, punisher, iron man, mantis, and invisible woman.",
            "The characters Karkat switches to if Black Panther is banned"
        ),
        "!schedule": (
            "Karkat doesn't have a fixed schedule since he works full time, but you can check https://discord.com/channels/1318808095081758842/1328061600028033054 for a list of upcoming streams!",
            "When does Karkat stream?"
        ),
        "!fliers": (
            "If you can hit the first spear, you can dash to them, spinning kick to stay at the right height and mark them again, then dash. If they’re not getting pocketed, they should die like this: https://discord.com/channels/1318808095081758842/1318814083142914198/1329143037347238049",
            "How to deal with fliers"
        ),
        "!nerf": (
            "The nerf decreased shield generation when dashing marked targets as well as the maximum shield that can be generated at one time. It makes black panther harder to play, but he’s still extremely strong. The margin for error is just much smaller.",
            "The effects of Panther nerfs"
        ),
        "!buff": (
            "Revert the panther nerfs, fix no-reg, and nerf his direct counters who got buffed like namor and bucky.",
            "Karkat's opinion on buffing Panther"
        ),
        "!swap": (
            "Whether or not to swap ultimately depends on whether or not you prioritize individual wins or improving at a given character, which is why Karkat rarely swaps!",
            "Karkat's philosophy on swapping characters"
        ),
        "!sg": (
            "SG stands for Sanctuary Games which is an indie game studio Karkat started a couple years ago. Still working on their first game, no eta!",
            "What Sanctuary Games (SG) is"
        ),
        "!sens": (
            "DPI: 1600, In-Game: 1.5\nBut sensitivity is personal preference, so use whatever feels most comfortable!",
            "Karkat's sensitivity settings"
        ),
        "!vod": (
            "When we decide to do a vod review, a post will be made in the discord under 'match-id' where the first person to drop a code gets chosen. Must be a ranked panther game and a loss, first come first serve, gets reset every stream! Karkat tries to do at least one vod review stream so if you don’t get reviewed today, be sure to come back!",
            "How to get a VOD reviewed"
        ),
        "!facereveal": (
            "Karkat's face is out there on the internet, so it wouldn’t be a reveal exactly, but he just doesn't have a webcam. He also figures most people watch the stream for the gameplay and don’t really care what he looks like.",
            "Face reveal when?"
        ),
    },
    "General Information": {
        "!bot": (
            "This is a custom bot for the Panthercord that is capable of doing nearly anything we could need. If you have any suggestions for features, feel free to post them in https://discord.com/channels/1318808095081758842/1331419541187854356. Use !help for a list of commands.",
            "Overview of the bot."
        ),
    },
}

# Main function to handle incoming messages
async def handle_message(bot, message):
    msg = message.content.strip()  # Remove leading/trailing whitespace

    # Ignore empty messages
    if not msg:
        return

    # ID of the specific channel where the bot should respond
    response_channel_id = 1331849473680474143

    # Fetch the channel object
    response_channel = bot.get_channel(response_channel_id)
    if response_channel is None:
        print(f"Channel with ID {response_channel_id} not found.")
        return

    # Determine the user to ping
    if message.mentions:
        # Use the first mentioned user in the message
        target_user = message.mentions[0]
    else:
        # Default to the author if no user is mentioned
        target_user = message.author

    # Check for 👀 emoji and respond with the same emoji in the response channel
    if "👀" in msg:  # Check for the emoji itself
        await message.channel.send(f"👀")
        return

    # Split the message to get the command and arguments
    command = msg.split()[0]

    # Search for the command in all categories
    for category in CATEGORIZED_COMMANDS.values():
        if command in category:
            response, _ = category[command]
            await response_channel.send(f"{response}\n{target_user.mention}")
            await message.delete()
            return

    # Map complex commands to their respective handler functions
    complex_commands = {
        "!help": help_command,
        "!hi": hi,
        "!coach": coach_command,
    }

    # Check if the command exists in the complex commands dictionary
    if command in complex_commands:
        await complex_commands[command](bot, message, response_channel, target_user)
        return

# Function to generate and display the categorized help message
async def help_command(bot, message, response_channel, target_user):
    help_message = "**Help Menu**\nUsage: !command @user\nSpecifying a user is optional and will direct the bot to ping that user.\n\n"
    for category_name, commands in CATEGORIZED_COMMANDS.items():
        help_message += f"**{category_name}:**\n"
        for command, (_, description) in commands.items():
            help_message += f"{command} - {description}\n"
        help_message += "\n"
    await response_channel.send(f"{help_message}{target_user.mention}  ")
    await message.delete()


# Hi command
async def hi(bot, message, response_channel, target_user):
    await message.channel.send(f"hi {target_user.mention}  :wave:")

# Coaching commmand
async def coach_command(bot, message, response_channel, target_user):
    # Only allow the command in channel 1334953693073768479:
    required_channel_id = 1334953693073768479
    if message.channel.id != required_channel_id:
        await message.channel.send(
            f"{message.author.mention} Please run the `!coach` command in <#{required_channel_id}>."
        )
        await message.delete()
        return

    # If the command is in the correct channel, proceed:
    prompt_body = message.content[len("!coach"):].strip()
    if not prompt_body:
        await message.channel.send(
            "Please ask a question or provide context after !coach."
        )
        return

    user_name = message.author.display_name
    reply = get_coach_reply(user_name, prompt_body)
    await message.channel.send(reply)

