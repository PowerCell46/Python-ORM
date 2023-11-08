class UserProfile(models.Model):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(to=UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=UserProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self) -> None:
        self.is_read = True

    def mark_as_unread(self) -> None:
        self.is_read = False

    def reply_to_message(self, reply_content: str, receiver: UserProfile) -> object:
        return Message(sender=self.receiver, receiver=receiver, content=reply_content).save()

    def forward_message(self, sender: UserProfile, receiver: UserProfile) -> object:
        return Message(sender=sender, receiver=receiver, content=self.content).save()
