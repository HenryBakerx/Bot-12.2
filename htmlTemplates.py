css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
</style>
'''

# Replace with your actual GitHub raw image URLs below
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://github.com/HenryBakerx/Bot-12.2/blob/c523a838e3444f7e8116ce311eccf13d191f2109/images/citiz%20logo.png" 
             style="max-height:78px; max-width:78px; border-radius:50%; object-fit:cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://github.com/HenryBakerx/Bot-12.2/blob/c523a838e3444f7e8116ce311eccf13d191f2109/images/bouwer.png" 
             style="max-height:78px; max-width:78px; border-radius:50%; object-fit:cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
