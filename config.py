import os

api_id = int(os.environ.get("API_ID", "22108820"))
api_hash = os.environ.get("API_HASH", "301a39af78de73406a67c75ad7dd7301")
bot_token = os.environ.get("BOT_TOKEN", "5930704808:AAGsVsZ0L6fX21C-dC6bACltNBgz9R6ibPE")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://ArabMongo1:fadhil123@cluster0.tqvy9uq.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "ArabMongo1")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001940956612"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001651360411"))
channel_log = int(os.environ.get("CHANNEL_LOG", ""))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1972981155"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "15"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "50"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "100"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "100"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "100"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "100"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "100"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "100"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#twinsgirl #twinsboy #twinsask #twinstory #twinspill #fwbkepo").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/1e5d031ea1441896377b5.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/0a8581125639a81a26f86.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/3d79003bb17fc7f7faae1.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "https://telegra.ph//file/ba61980c4f17aa62c8de8.jpg")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "https://telegra.ph//file/3fdd89b5edaf915faed32.jpg")
pic_Daddy_Sugar = os.environ.get("PIC_DADDY_SUGAR", "https://telegra.ph//file/a572dcc61241dec212652.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat FWB TWINS😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya FWB👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post FWB TWINS✨\n\nIni adalah bot Menfes ya FWB, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#Twinsrandom Untuk Random\n#twinsask Untuk Bertanya untuk Bertanya\n#twinstory Untuk Berbagi Cerita\n#twinstory Untuk Berbagi Cerita\n\n\nContoh:\n {mention} Cari Mutualan Dom Depok #twiinsboy/n Contact @kjccaa")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#twinsgirl (untuk cewe) / #twinsboy (untuk cowo) Untuk Mencari Pasangan, Teman , Partner FWB
#twinsask Untuk Bertanya
#twinstory Untuk Berbagi Cerita
#twinstory Untuk Berbagi Cerita

""")
