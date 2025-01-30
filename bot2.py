await message.reply("No links Found in this text",quote=True)
        return
    for short_link in links:
        try:
            short_link2 = await
      get_shortlink(short_link)
            
async def get_shortlink(short_link):
    url2 = API_URL2
    params = {'api': API_KEY2, 'url2': short_link}
    
