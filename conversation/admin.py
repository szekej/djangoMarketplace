from django.contrib import admin

from conversation.models import ConversationMessage, Conversation

# Register your models here.

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
