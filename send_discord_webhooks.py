# Send Discord Webhooks
# pip install discord-webhook

from discord_webhook import DiscordWebhook

# Send Simple Webhook
hook = DiscordWebhook(url='Discord webhook api', content="Hello Medium")
hook.execute()

# Send Multiple Webhooks
url = ["webhook_api1, webhook_api2"]
hook = DiscordWebhook(url=url, content="Hello Medium")
hook.execute()

# Send Embed Webhook
hook = DiscordWebhook(url='Discord webhook api', content="Hello Medium")
hook.add_embed(title="Embed Title", description="Embed Description")
hook.execute()

# Send File Webhook
hook = DiscordWebhook(url='Discord webhook api', content="Hello Medium")
hook.add_file(file_path="file_path")
hook.execute()

# Delete Webhook
hook = DiscordWebhook(url='Discord webhook api', content="Hello Medium")
web = hook.execute()
hook.delete(web)
