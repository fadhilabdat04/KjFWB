import os

api_id = int(os.environ.get("API_ID", "22108820"))
api_hash = os.environ.get("API_HASH", "301a39af78de73406a67c75ad7dd7301")
bot_token = os.environ.get("BOT_TOKEN", "6692168439:AAGg0afMKxJh2y_rsV6BHVDPwc64qgxDZ1c")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://doadmin:7P4N61cvJnu9532z@mongodb2-7a545cbe.mongo.ondigitalocean.com/admin?tls=true&authSource=admin")
db_name = os.environ.get("DB_NAME", "doadmin")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001509543098"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001961436814"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001915672497"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6103178771"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "15"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "100"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "500"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "500"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "500"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "500"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "500"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "500"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#fwbcantik #fwbganteng #fwbgalau #fwbrandom #fwbpap #fwbkepo").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/67693ef3e1a1bf41c4632.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/4d228a9ac5ea990d9c381.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/3779f7368bed17557c71a.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "https://telegra.ph//file/44e90c837fdded8a9bb8d.jpg")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "https://telegra.ph//file/225355e06d730073285b2.jpg")
pic_Daddy_Sugar = os.environ.get("PIC_DADDY_SUGAR", "https://telegra.ph//file/f2a63f456933489e80cf0.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat FWB😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya FWB👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post FWB base✨\n\nIni adalah bot Menfes ya FWB, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#fwbrandom Untuk Random\n#fwbkepo untuk Bertanya\n#fwbgalau untuk Berbagi Cerita\n#fwbpap untuk ngirim pap kecuali pap kemaluan\n\nContoh:\n {mention} Cari Mutualan Dom Depok #fwbganteng/n Contact @Stevvano")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#fwbcantik Untuk Cewek
#fwbganteng Untuk Cowok
#fwbgalau Untuk Curhat
#fwbrandom Untuk Random
#fwbkepo Bertanya
#fwbpap untuk pap rate kecuali pap kemaluan

""")
