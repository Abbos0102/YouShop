import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

PRODUCTS = [
    {"name": "iPhone 14 Pro", "price": "$999", "desc": "128GB, Deep Purple"},
    {"name": "AirPods Pro", "price": "$249", "desc": "2nd Generation"},
    {"name": "Dior Sauvage", "price": "$120", "desc": "100ml Eau de Parfum"}
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to YouShop! 🛍️\nUse /products to see available items.")

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = "🛒 *Available Products:*\n\n"
    for item in PRODUCTS:
        response += f"📦 *{item['name']}*\n💰 {item['price']}\n📝 {item['desc']}\n\n"
    await update.message.reply_text(response, parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("products", products))
    print("Bot is running...")
    app.run_polling()
