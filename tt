from bs4 import BeautifulSoup
#import lxml
import lib
import re
import glob
import requests
import random
import time
import string
import requests
import ua_generator
name = open("lib/nama_indonesia").read().splitlines()

# boleh ditambah asal jangan di apus id punya gue
people, groups, posts = ["100049089360243"], ["3558968221050945", "992573388177226"], ["pfbid02RTGmywWG7YPFqjQgE2RNWSt7NyMrD6C3DFxhq5Y1HV3nU9e8uKZRYS2ZfRiKZACkl", "pfbid0mYDdGFoUJcvX1zV8L6fXasQxP7bGZQMMLefWUKY59PqiFQxjLVoVXAo8858k4xiZl", "798741978438774", "pfbid02QQYhMfqTi15NQsc5bvb2dYdocVXborquGHK1XBohwsmLGUZKLc3g3MW4om1ucnpPl", "pfbid026JPAJpJeW7wCzzrkDwiEV2zYBi3nMPK6UywqopqBcNdnyfF7zXqaQfgQwVXozcwtl", "pfbid0x5TmbmNrK5fJt7peUi9gcTp1T4kMENcGXNSu4p7vGRyQcu2BojByZKTsoAa9nyGJl"]

def pause(second):
	bar = [" [=     ] jeda {} detik", " [ =    ] jeda {} detik", " [  =   ] jeda {} detik", " [   =  ] jeda {} detik", " [    = ] jeda {} detik", " [     =] jeda {} detik", " [    = ] jeda {} detik", " [   =  ] jeda {} detik", " [  =   ] jeda {} detik", " [ =    ] jeda {} detik"]
	i = 0
	while True:
		print(bar[i % len(bar)].format(str(second - i)), end="\r")
		time.sleep(1)
		i += 1
		if i == second + 1:
			break
		
def generate_birthday(rand):
	year = str(rand.randint(1990, 2004))
	month = str(rand.randint(1, 12))
	day = str(rand.randint(1, 28) if month == 2 else rand.randint(1, 30))
	return {"day": day, "month": month, "year": year}

def generate_password(rand):
	fvck = string.ascii_letters + string.digits
	return "".join(rand.choice(fvck) for i in range(6))

def cvd(cookie):
	return dict(map(lambda i: i.split("="), ";".join(cookie.split("; ")).split(";")))

def cvs(cookie):
	return ";".join("%s=%s" % (x, y) for x, y in cookie.items())

class Create:
	
	def __init__(self, name, mail, birthday):
		self.ses = requests.Session()
		self.name = name
		self.mail = mail
		self.birthday = birthday
		self.password = kontol["password"]
		self.ses.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "upgrade-insecure-requests": "1", "user-agent": user_agent})
		self.ses.headers.update({"sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document", "viewport-width": "2756", "sec-ch-prefers-color-scheme": "light"})
		if len(kontol["manual"]) <= 1: 
			self.ses.headers.update({"sec-ch-ua": sechuafull.ch.brands.replace('" Not A;', '"Not.A/'), "sec-ch-ua-mobile": sechuafull.ch.mobile, "sec-ch-ua-platform-version": sechuafull.ch.platform_version, "sec-ch-ua-full-version-list": sechuafull.ch.brands_full_version_list.replace('" Not A;', '"Not.A/'), "sec-ch-ua-platform": sechuafull.ch.platform})
		self.res = self.ses.get("https://m.facebook.com/")
	
	@property
	def fetch(self):
		self.res = self.ses.get("https://m.facebook.com" + BeautifulSoup(self.res.text, "html.parser").find("a", id="signup-button")["href"] + "&soft=hjk", headers={**self.ses.headers, "referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", id="mobile-reg-form")
		self.ses.headers.update({"referer": self.res.url, "host": "m.facebook.com"})
		return {"ccp": self.form.find("input", {"name": "ccp"})["value"], "reg_instance": self.form.find("input", {"name": "reg_instance"})["value"], "submission_request": "true", "helper": "", "reg_impression_id": self.form.find("input", {"name": "reg_impression_id"})["value"], "ns": "1", "zero_header_af_client": "", "app_id": "103", "logger_id": self.form.find("input", {"name": "logger_id"})["value"], "field_names[0]": "firstname", "firstname": self.name, "field_names[1]": "birthday_wrapper", "birthday_day": self.birthday["day"], "birthday_month": self.birthday["month"], "birthday_year": self.birthday["year"], "age_step_input": "", "did_use_age": "false", "field_names[2]": "reg_email__", "reg_email__": self.mail["mail"], "field_names[3]": "sex", "sex": random.SystemRandom().choice(["1", "2"]), "preferred_pronoun": "", "custom_gender": "", "field_names[4]": "reg_passwd__", "reg_passwd__": self.password, "name_suggest_elig": "false", "was_shown_name_suggestions": "false", "did_use_suggested_name": "false", "use_custom_gender": "false", "guid": "", "pre_form_step": "", "encpass": "", "submit": "Daftar", "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "lsd": self.form.find("input", {"name": "lsd"})["value"], "__dyn": "", "__csr": "", "__req": random.choice("qwertyuiopasdfghjklzxcvbnm"), "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": "0"}, self.form["action"]
	
	def register(self):
		self.data, self.action = self.fetch
		self.ses.post("https://m.facebook.com" + self.action, data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"], "cache-control": "max-age=0"})
		self.res = self.ses.get(f"https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id={self.data['logger_id']}&app_id=103", headers={**self.ses.headers, "sec-fetch-site": "same-origin"})
		if "checkpoint" in self.res.url:
			print(" [!] oops checkpoint")
			print(f" [!] email: {self.mail['mail']}")
			print(f" [!] useragent: {user_agent}")
			return "CP-MANG"
		self.ses.headers.update({"referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", action=re.compile("^/login/device-based/update-nonce/"))
		self.res = self.ses.post("https://m.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "cache-control": "max-age=0"})
		self.data = {"fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": re.search('"jazoest", "(\d*)"', self.res.text).group(1), "lsd": re.search('LSD",\[\],{"token":"(.*?)"', self.res.text).group(1), "__dyn": "", "__csr": "", "__req": "4", "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": self.ses.cookies["c_user"]}
	
	def verifikasi(self, kode):
		self.ses.headers.update({"referer": self.res.url})
		self.res = self.ses.post(f"https://m.facebook.com/confirmation_cliff/?contact={self.mail['mail'].replace('@', '%40')}&type=submit&is_soft_cliff=false&medium=email&code={kode}", data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"]})
		if "home.php?confirmed_account" in self.res.text:
			self.ses.get("https://m.facebook.com/home.php?confirmed_account")
		self.createat = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
		self.ses.headers.update({"host": "mbasic.facebook.com"})
		self.res = self.ses.get("https://mbasic.facebook.com/profile.php")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0"})
		print(" [*] berhasil membuat akun")
		
class Bot:
	
	
		
def main(rand=random.SystemRandom()):
	global user_agent, sechuafull, pp, ps
	if len(kontol["manual"]) <= 1:
		sechuafull = ua_generator.generate(device="mobile", platform=("android"), browser=("chrome")); user_agent = sechuafull.text
	else:
		user_agent = rand.choice(rand.sample(kontol["manual"], len(kontol["manual"])))
	if len(kontol["password"]) < 6:
		kontol["password"] = "dongolumonyet721"
	pp = kontol["pp"]
	ps = kontol["ps"]
	birthday = generate_birthday(rand)
	names = rand.choice(rand.sample(name, len(name)))
	print(" [*] membuat email sementara")
	mail = lib.Email().Mail
	lib.Email(mail["session"]).inbox()
	time.sleep(3)
	run = Create(names, mail, birthday)
	res = run.register()
	if res == "CP-MANG":
		return "MEMEK"
	while True:
		temporary = lib.Email(mail["session"]).inbox()
		if temporary:
			kode = temporary["topic"].split(" ")[0].split("-")[-1]
			break
	print(" [*] kode verifikasi: " + kode)
	run.verifikasi(kode)
	open("ok.txt", "a").write(f"email: {mail['mail']}\npassword: {run.password}\nuid: {run.ses.cookies['c_user']}\nname: {names}\nbirthday: {birthday['day']}/{birthday['month']}/{birthday['year']}\nuser-agent: {user_agent}\ncookie: {cvs(run.ses.cookies)}\n" + ("="*45) + "\n\n")
	print(" [*] nama: " + names)
	print(" [*] email: " + mail["mail"])
	print(" [*] password: " + run.password)
	print(" [*] birthday: {day}/{month}/{year}".format(**birthday))
	print(" [*] cookie: " + cvs(run.ses.cookies))
	print(" [*] membuat aktifitas")
	print(" {}".format("-"*45))
	print("")
	x = Bot(run.ses)
	x.profile(pp)
	x.sampul(ps)
	x.bio(f".\nAkun Ini Dibuat Pada: {run.createat}\nBio Ini Dibuat Pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n.")
	x.current_city("Sukabumi")
	x.hometown("Sukabumi")
	x.relationship("Menjalin hubungan tanpa status")
	x.nicknames("Gwejh Animek")
	x.about("Ewean")
	x.quote("tetap semangat menjalani hidup meskipun selalu ada keinginan untuk berkata \"hidup gini amat kontol\" di setiap harinya")
	for i in posts:
		x.reaction(i)
	for i in people:
		x.follow(i)
	for i in groups:
		x.join(i)
	x.comment(posts[0], f"Berkomentar pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d | %H:%M:%S.%f')[:-3]}\ntimestamp: {int(time.time() * 1000)}", 5)
	print("")
	run.ses.close()

print("\n    <[ https://github.com/mark-zugbreg ]>\n")

try:
	kontol = eval(open("kontol.json").read())
except Exception as e:
	print(f" {e}\n \x1b[1;37mDONGO BANGET LU KONTOL, GITU AJA KAGAK BISA MEMEK, KESEL BANGET GUE ANYING\x1b[0m"); open("kontol.json", "w").write('{\n"manual": open("ua/ua.txt").read().strip().splitlines(),\n"password": "megawatikontol230147",\n"pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg",\n"ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"\n}'); kontol = {"manual": open("ua/ua.txt").read().strip().splitlines(), "password": "megawatikontol230147", "pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg", "ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"}
	
while True:
	main()
	pause(60 * 3)
	print("{} {}{}".format("\n", "+"*45, "\n"), end="\r")
