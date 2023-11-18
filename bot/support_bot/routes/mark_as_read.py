from aiohttp import web
from aiohttp.web_request import Request
from support_bot import db
from support_bot.misc import web_routes, bot

@web_routes.post(f"/tg-bot/mark-as-read")
async def new_message_from_manager(request: Request):
    payload = await request.json()
    chat_id = payload.get("chat_id")
    message_id = payload.get("message_id")
    modified_count = db.message.mark_as_read(chat_id, message_id)
    response = web.json_response({"result": "Marked!", "modified_count": modified_count}, status=200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response