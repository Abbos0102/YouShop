from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@you_shopp"
GROUP_LINK = "https://t.me/youshop_support"

# Mahsulotlar ro'yxati
PRODUCTS = [bu
    {"name": "iPhone 14 Pro", "price": "$999", "desc": "128GB, Deep Purple"},
    {"name": "AirPods Pro 2", "price": "$249", "desc": "MagSafe qutisi bilan"},
    {"name": "YSL Parfyum", "price": "$120", "desc": "Libre Intense, 90ml"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "YouShop’ga xush kelibsiz! 🛍️\nMavjud mahsulotlarni ko‘rish uchun /products buyrug‘ini yuboring."
    )

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for p in PRODUCTS:
        keyboard = [
            [InlineKeyboardButton("🛒 Buyurtma berish", url=GROUP_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = f"**{p['name']}**\n{p['desc']}\n💵 Narxi: {p['price']}"
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("products", products))
    app.run_polling()

if __name__ == "__main__":
    main()
