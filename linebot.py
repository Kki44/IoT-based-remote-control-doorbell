from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import FlexSendMessage
from linebot.models import BubbleContainer
from linebot.models import ImageComponent
from linebot.models import URIAction

linebot_api = LineBotApi("cejon4trTMixjusA6HUl99T1rXnAM6F8zdnDBylOtlkIaXIwLoIwud+9RMSkiY7nI1hNbC3gShLjnlF9lrxF6yq+RRKmy4Dz2/0SC3V1MLv4Fd11DGbybjWeagQn7qjn0Hmg1rCP2IudF7G3aftwOgdB04t89/1O/w1cDnyilFU=") #channel acess token
handler = WebhookHandler("d052f047459d090e8e025b7c001f80f4")#channel secret

#linebot_api.broadcast(TextSendMessage(text="kki fuck that shit"))
image_url = 'https://ctl.s6img.com/society6/img/CnFTfKZu5-Aebu2t1YyEdwFKs4M/w_700/prints/~artwork/s6-original-art-uploads/society6/uploads/misc/5653cd36be88468b8387ee851c6e5cc0/~~/buff-cat-meme-prints.jpg'
message = ImageSendMessage(original_content_url=image_url,preview_image_url=image_url)
flex_message = FlexSendMessage(
    alt_text='hello',
    contents=BubbleContainer(
        direction='ltr',
        hero=ImageComponent(
            url='https://ctl.s6img.com/society6/img/CnFTfKZu5-Aebu2t1YyEdwFKs4M/w_700/prints/~artwork/s6-original-art-uploads/society6/uploads/misc/5653cd36be88468b8387ee851c6e5cc0/~~/buff-cat-meme-prints.jpg',
            size='full',
            aspect_ratio='20:13',
            aspect_mode='cover',
            action=URIAction(uri='https://ctl.s6img.com/society6/img/CnFTfKZu5-Aebu2t1YyEdwFKs4M/w_700/prints/~artwork/s6-original-art-uploads/society6/uploads/misc/5653cd36be88468b8387ee851c6e5cc0/~~', label='label')
        )
    )
)
linebot_api.push_message('Uf47f0ad1379edda9d513f101d5f16926',flex_message)