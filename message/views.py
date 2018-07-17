from django.shortcuts import render

# Create your views here.
from collections import OrderedDict
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user_profile.models import Profile, Follow
from message.models import Message


def getConversations(request):
    sender = request.user
    participants = [sender]
    followings = Follow.objects.filter(follower=sender)
    for following in followings:
        participants.append(following.following)
    conversations = OrderedDict()
    conv_messages = Message.objects.filter(sender__in=participants, receiver__in=participants).order_by("id")
    for conv_message in conv_messages:
        conv_participants = [conv_message.sender, conv_message.receiver]
        last_message = \
            Message.objects.filter(sender__in=conv_participants, receiver__in=conv_participants).order_by("-id")[
                0].msg_content
        if conv_participants[0] == request.user:
            try:
                if not conversations[conv_participants[1]]:
                    contact_profile = Profile.objects.get(user=conv_participants[1])
                    conversations[conv_participants[1]] = {"profile": contact_profile, "last_message": last_message}
            except KeyError:
                contact_profile = Profile.objects.get(user=conv_participants[1])
                conversations[conv_participants[1]] = {"profile": contact_profile, "last_message": last_message}
        else:
            try:
                if not conversations[conv_participants[0]]:
                    contact_profile = Profile.objects.get(user=conv_participants[0])
                    conversations[conv_participants[0]] = {"profile": contact_profile, "last_message": last_message}
            except KeyError:
                contact_profile = Profile.objects.get(user=conv_participants[0])
                conversations[conv_participants[0]] = {"profile": contact_profile, "last_message": last_message}
    for participant in participants:
        if participant != request.user:
            contact_profile = Profile.objects.get(user=participant)
            try:
                if not conversations[participant]:
                    conversations[participant] = {"profile": contact_profile, "last_message": "Nothing to show"}
            except KeyError:
                conversations[participant] = {"profile": contact_profile, "last_message": "Nothing to show"}
    return conversations


def chat(request):
    conversations = getConversations(request)
    current_user_profile = Profile.objects.get(user=request.user)

    context = {"conversations": conversations, "sender_user_profile": current_user_profile}
    return render(request, "chat.html", context)


def chatFriend(request, username):
    sender = request.user
    receiver = User.objects.get(username=username)
    current_user_profile = Profile.objects.get(user=request.user)
    receiver_user_profile = Profile.objects.get(user=receiver)
    current_participants = [sender, receiver]
    messages = Message.objects.filter(sender__in=current_participants, receiver__in=current_participants).order_by("id")
    conversations = getConversations(request)

    context = {"messages": messages, "receiver": receiver, "sender_user_profile": current_user_profile,
               "receiver_user_profile": receiver_user_profile, "conversations": conversations}
    return render(request, "chatFriend.html", context)


def newMessage(request, username):
    sender = request.user
    receiver = User.objects.get(username=username)
    message = request.POST.get("sender_message")
    Message.objects.create(
        sender=sender,
        receiver=receiver,
        msg_content=message)
    return redirect("/account/chat/{}".format(username))
